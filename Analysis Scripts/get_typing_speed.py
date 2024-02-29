import sys
import os
import json
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import numpy as np
import csv
import matplotlib.ticker as mticker
def read_session_mapping():
    """
    {
        "abs33":{'A': [1,'High'], 'B': [2,'Sober']}
    }
    """
    
    session_mapping={}
    with open("../session_mapping.csv",'r',encoding="utf8") as data:
        for line in csv.DictReader(data):
            session_mapping[line['participant id']] = {line["session 1 problem set"]: [1,line['session 1 type']],
                                                       line["session 2 problem set"]: [2,line['session 2 type']]}
    return session_mapping
def get_problem_boundary(participant_id, problem_set):
    """
    Return the starting time for each problem

    input: abs33 A
    output: ["20230405222337", "20230405224107", "20230405225652"]
    """
    list = []
    try:
        list = os.listdir("../test_data/" + participant_id + "-" + problem_set)
    except:
        print("")
    boundaries = ["null", "null", "null"]
    
    problem1files = []
    problem2files = []
    problem3files = []
    for i in list:
        if not i.startswith("problem"):
            continue
        if i.startswith("problem1easy_"):
            problem1files.append(i[13:-3])
        elif i.startswith("problem2easy_"):
            problem2files.append(i[13:-3])
        elif i.startswith("problem3medium_"):
            problem3files.append(i[15:-3])
    if problem1files:
        problem1files.sort()
        boundaries[0] = problem1files[0]
    if problem2files:
        problem2files.sort()
        boundaries[1] = problem2files[0]
    if problem3files:
        problem3files.sort()
        boundaries[2] = problem3files[0]
    
    return boundaries


def read_and_divide_keystrokes(participant_id, problem_set, divide_or_not = True):
    """
    If divide_or_not == True, divide the keystrokes into three problems
    """
    boundaries = None
    if divide_or_not:
        boundaries = get_problem_boundary(participant_id, problem_set)
        if "null" in boundaries:
            print("Problem boundaries not found for " + participant_id + " " + problem_set)
            return []
    if not os.path.isfile("./keystrokes_files/" + participant_id + "-" + problem_set ):
        print("Keystrokes file not found for " + participant_id + " " + problem_set)
        return []
    
    lines = []
    with open("./keystrokes_files/" + participant_id + "-" + problem_set, "r") as f:
        for line in f:
            lines.append(json.loads(line))

    if not divide_or_not:
        return lines
    
    divided_keystrokes = [[],[],[]]
    for i in lines:
        raw_timestamp = i["timestamp"][:-5]
        parsed_timestamp = raw_timestamp.replace("-","")
        parsed_timestamp = parsed_timestamp.replace(":","")
        parsed_timestamp = parsed_timestamp.replace("T","")
        if parsed_timestamp < boundaries[1]:
            divided_keystrokes[0].append(i)
        elif parsed_timestamp >= boundaries[1] and parsed_timestamp < boundaries[2]:
            divided_keystrokes[1].append(i)
        elif parsed_timestamp >= boundaries[2]:
            divided_keystrokes[2].append(i)

    return divided_keystrokes

    
def divide_into_buckets(timestamps, interval):
    start_time = datetime.strptime(timestamps[0]['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")
    end_time = datetime.strptime(timestamps[-1]['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")
    total_seconds = (end_time - start_time).total_seconds()
    num_buckets = int(total_seconds // interval) + 1
    
    buckets = [[] for _ in range(num_buckets)]  # Create empty buckets
    
    for timestamp in timestamps:
        dt = datetime.strptime(timestamp['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")  # Convert timestamp string to datetime object
        total_seconds = (dt - start_time).total_seconds()  # Calculate total seconds from start_time
        
        bucket_index = int(total_seconds // interval)  # Determine the bucket index for the current timestamp
        buckets[bucket_index].append(timestamp)  # Add the timestamp to the corresponding bucket
    
    return buckets


def filter_typing_keystrokes(keystrokes):
    result = []
    for keystroke in keystrokes:
        if keystroke["command"] == "type" or keystroke["command"] == "$type":
            result.append(keystroke)
    return result


def calculate_total_idle_time(typing_keystrokes, threshold = 8):
    """
    Calculate the total idle time defined as any interval > threshold(unit: s) between two typing keystrokes
    """

    timestamps = []
    for k in typing_keystrokes:
        timestamps.append(datetime.strptime(k["timestamp"][:-5], "%Y-%m-%dT%H:%M:%S"))

    total_idle_time = timedelta()
    previous_timestamp = None

    for timestamp in timestamps:
        if previous_timestamp is not None:
            time_difference = timestamp - previous_timestamp
            if time_difference.total_seconds() > threshold:
                total_idle_time += time_difference

        previous_timestamp = timestamp

    return total_idle_time


def calculate_typing_speed(keystrokes, threshold = 8):
    """
    total_typing_count/(endtime-starttime-total_idle_time(using threshold))
    """
    typing_keystrokes = filter_typing_keystrokes(keystrokes)
    total_idle_time = calculate_total_idle_time(typing_keystrokes, threshold).total_seconds()

    start_time = datetime.strptime(typing_keystrokes[0]['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")
    end_time = datetime.strptime(typing_keystrokes[-1]['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")
    total_seconds = (end_time - start_time).total_seconds()
    
    total_num_deletes = count_deletes(keystrokes)
    active_time = total_seconds-total_idle_time
    typing_speed = len(typing_keystrokes)/active_time
    return len(typing_keystrokes), total_num_deletes, total_seconds, total_idle_time, active_time, typing_speed

def plot_active_diagram_for_all():
    list = os.listdir("./keystrokes_files/")
    for session in list:
        dash_index = session.find('-')
        if dash_index == -1:
            continue
        participant_id = session[:dash_index]
        problem_set = session[-1]
        try:
            plot_active_diagram_for_one_session(participant_id, problem_set, bucket_size = 15)
        except:
            print("Error with " + participant_id + "-" + problem_set + ": Plot diagram")
            continue

def plot_active_diagram_for_one_session(participant_id, problem_set, bucket_size = 15):
    """
    bucket_size: 15s
    """

    divided_keystrokes = read_and_divide_keystrokes(participant_id ,problem_set, True)

    each_problem_type_buckets = []
    each_problem_delete_buckets = []
    indices = []
    for problem_keystrokes in divided_keystrokes:
        if not len(problem_keystrokes):
            each_problem_type_buckets.append([])
            each_problem_delete_buckets.append([])
        
            indices.append([])
            continue
        type_count_buckets = []
        delete_count_buckets = []
        buckets = divide_into_buckets(problem_keystrokes, bucket_size)
        for bucket in buckets:
            type_count = 0
            delete_count = 0
            for command in bucket:
                if command['command'] == '$type' or command['command'] =="type":
                    type_count += 1
                if command['command'] == 'deleteLeft':
                    delete_count += 1
            type_count_buckets.append(type_count)
            delete_count_buckets.append(delete_count)

        each_problem_type_buckets.append(type_count_buckets)
        each_problem_delete_buckets.append(delete_count_buckets)
        
        indices.append(list(range(len(type_count_buckets))))
        #indices.append(range(0,bucket_size*len(type_count_buckets),bucket_size))
        #print(indices)
        
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), gridspec_kw={'width_ratios': [3, 3, 4]})
    # Plot the first bar graph in the first subplot
    axes[0].bar(indices[0], each_problem_type_buckets[0], width=0.6,label="Type")
    axes[0].bar(indices[0], each_problem_delete_buckets[0], width=0.6,label="Delete", bottom = each_problem_type_buckets[0])
    axes[0].set_xlabel('Time('+ str(bucket_size) + 's)')
    axes[0].set_ylabel('Keystrokes')
    axes[0].set_title('Problem 1')

    # Plot the second bar graph in the second subplot
    axes[1].bar(indices[1], each_problem_type_buckets[1], width=0.6,label="Type")
    axes[1].bar(indices[1], each_problem_delete_buckets[1], width=0.6,label="Delete", bottom = each_problem_type_buckets[1])
    axes[1].set_xlabel('Time('+ str(bucket_size) + 's)')
    axes[1].set_ylabel('Keystrokes')
    axes[1].set_title('Problem 2')

    # Plot the third bar graph in the third subplot
    axes[2].bar(indices[2], each_problem_type_buckets[2], width=0.6,label="Type")
    axes[2].bar(indices[2], each_problem_delete_buckets[2], width=0.6,label="Delete", bottom = each_problem_type_buckets[2])
    axes[2].set_xlabel('Time('+ str(bucket_size) + 's)')
    axes[2].set_ylabel('Keystrokes')
    axes[2].set_title('Problem 3')


   

    fig.suptitle("Participant_id: " + participant_id + "   Problem set: " + problem_set)

    plt.tight_layout()
    plt.savefig('./active_diagrams/' + participant_id + "_" + problem_set +  '.png')
    
def count_deletes(keystrokes):
    count = 0

    for keystroke in keystrokes:
        if keystroke["command"] == "deleteLeft":
            count += 1

    return count


def analyze_typing_for_one_session(participant_id, problem_set, threshold = 8):
    divided_keystrokes = read_and_divide_keystrokes(participant_id ,problem_set, True)
    return_dict = {"problem1":{}, "problem2":{}, "problem3":{}}
    for i in range(3):
        if not len(divided_keystrokes[i]):
            return_dict["problem"+str(i+1)] = {"total_num_typing_keystrokes":0,
                                         "total_num_deletes": 0,
                                         "total_seconds":0,
                                         "total_idle_time": 0,
                                         "total_active_time": 0,
                                         "typing_speed": 0}
            continue
        total_num_typing_keystrokes, total_num_deletes, total_seconds, total_idle_time, active_time, typing_speed = calculate_typing_speed(divided_keystrokes[i], threshold)
        return_dict["problem"+str(i+1)] = {"total_num_typing_keystrokes":total_num_typing_keystrokes,
                                         "total_num_deletes": total_num_deletes,
                                         "total_seconds":total_seconds,
                                         "total_idle_time": total_idle_time,
                                         "total_active_time": active_time,
                                         "typing_speed": typing_speed}
    return return_dict

def analyze_typing_for_all():
    return_dict = {}
    list = os.listdir("./keystrokes_files/")
    for session in list:
        dash_index = session.find('-')
        if dash_index == -1:
            continue
        participant_id = session[:dash_index]
        problem_set = session[-1]
        try:
            result = analyze_typing_for_one_session(participant_id, problem_set, threshold=8)
            if participant_id in return_dict.keys():
                return_dict[participant_id][problem_set] = result
            else:
                return_dict[participant_id] = {}
                return_dict[participant_id][problem_set] = result
        except:
            print("Error with " + participant_id + "-" + problem_set + ": Analyzing speed" )
            continue
    
    # write result to file
    with open("./speed_analysis","w+")as f:
        f.write("participant_id\tproblem_set\tproblem\ttotal_num_typing_keystrokes\ttotal_num_deletes\ttotal_seconds\ttotal_idle_time\ttotal_active_time\ttyping_speed\n")
        for participant_id in return_dict.keys():
            for problem_set in return_dict[participant_id].keys():
                dict = return_dict[participant_id][problem_set]
                for i in dict.keys():
                    f.write(participant_id + "\t\t\t" + problem_set + "\t\t\t" + i + "\t\t\t")
                    f.write(str(dict[i]["total_num_typing_keystrokes"]) + "\t\t\t\t\t\t")
                    f.write(str(dict[i]["total_num_deletes"]) + "\t\t\t\t")
                    f.write(str(dict[i]["total_seconds"]) + "\t\t\t")
                    f.write(str(dict[i]["total_idle_time"]) + "\t\t\t")
                    f.write(str(dict[i]["total_active_time"]) + "\t\t")
                    f.write(str(dict[i]["typing_speed"]) + "\n")


def plot_aggregated_diagram():
    def divide_keystrokes_into_num_of_buckets(timestamps, num_buckets):
        start_time = datetime.strptime(timestamps[0]['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")
        end_time = datetime.strptime(timestamps[-1]['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")
        total_time = (end_time - start_time).total_seconds()
        interval = total_time/num_buckets
    
        buckets = [[] for _ in range(num_buckets)]  # Create empty buckets
    
        for timestamp in timestamps:
            dt = datetime.strptime(timestamp['timestamp'][:-5], "%Y-%m-%dT%H:%M:%S")  # Convert timestamp string to datetime object
            total_seconds = (dt - start_time).total_seconds()  # Calculate total seconds from start_time
        
            bucket_index = min(int(total_seconds / interval), num_buckets - 1)  # Determine the bucket index for the current timestamp
            buckets[bucket_index].append(timestamp)  # Add the timestamp to the corresponding bucket
    
        return buckets
    
    def get_aggregated_buckets_from(participant_id, problem_set):
        divided_keystrokes = read_and_divide_keystrokes(participant_id ,problem_set, True)

        each_problem_type_buckets = []
        each_problem_delete_buckets = []
        indices = []
        for problem_keystrokes in divided_keystrokes:
            if not len(problem_keystrokes):
                each_problem_type_buckets.append([])
                each_problem_delete_buckets.append([])
        
                indices.append([])
                continue
            type_count_buckets = []
            delete_count_buckets = []
            buckets = divide_keystrokes_into_num_of_buckets(problem_keystrokes, 80)
            for bucket in buckets:
                type_count = 0
                delete_count = 0
                for command in bucket:
                    if command['command'] == '$type' or command['command'] =="type":
                        type_count += 1
                    if command['command'] == 'deleteLeft':
                        delete_count += 1
                type_count_buckets.append(type_count)
                delete_count_buckets.append(delete_count)

            each_problem_type_buckets.append(type_count_buckets)
            each_problem_delete_buckets.append(delete_count_buckets)
            indices.append(range(80))
        return [indices, each_problem_type_buckets, each_problem_delete_buckets]
        

    list = os.listdir("./keystrokes_files/")
    session_mapping=read_session_mapping()

    aggregated_indices, aggregated_each_problem_type_buckets, aggregated_each_problem_delete_buckets = [],[[0 for i in range(80)] for j in range(3)],[[0 for i in range(80)] for j in range(3)]
    for session in list:
        dash_index = session.find('-')
        if dash_index == -1:
            continue
        participant_id = session[:dash_index]
        problem_set = session[-1]
        if participant_id=='bnhmj':
            continue
        if session_mapping[participant_id][problem_set][1]=='High':
            continue
        indices, each_problem_type_buckets, each_problem_delete_buckets = None, None, None
        indices, each_problem_type_buckets, each_problem_delete_buckets = get_aggregated_buckets_from(participant_id, problem_set)
        
        
        for j in range(3):
            for i in range(len(aggregated_each_problem_type_buckets)):
                aggregated_each_problem_type_buckets[j][i]+=each_problem_type_buckets[j][i]
                aggregated_each_problem_delete_buckets[j][i]+=each_problem_delete_buckets[j][i]
            aggregated_indices = indices[j]
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), gridspec_kw={'width_ratios': [3, 3, 4]})
    # Plot the first bar graph in the first subplot
    axes[0].bar(aggregated_indices[0], aggregated_each_problem_type_buckets[0], width=0.6,label="Type")
    axes[0].bar(aggregated_indices[0], aggregated_each_problem_delete_buckets[0], width=0.6,label="Delete", bottom = aggregated_each_problem_type_buckets[0])
    axes[0].set_xlabel('Time(')
    axes[0].set_ylabel('Keystrokes')
    axes[0].set_title('Problem 1')

    # Plot the second bar graph in the second subplot
    axes[1].bar(aggregated_indices[1], aggregated_each_problem_type_buckets[1], width=0.6,label="Type")
    axes[1].bar(aggregated_indices[1], aggregated_each_problem_delete_buckets[1], width=0.6,label="Delete", bottom = aggregated_each_problem_type_buckets[1])
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('Keystrokes')
    axes[1].set_title('Problem 2')

    # Plot the third bar graph in the third subplot
    axes[2].bar(aggregated_indices[2], aggregated_each_problem_type_buckets[2], width=0.6,label="Type")
    axes[2].bar(aggregated_indices[2], aggregated_each_problem_delete_buckets[2], width=0.6,label="Delete", bottom = aggregated_each_problem_type_buckets[2])
    axes[2].set_xlabel('Time(''s)')
    axes[2].set_ylabel('Keystrokes')
    axes[2].set_title('Problem 3')

    plt.tight_layout()
    plt.savefig('./active_diagrams/aggregated.png')

if __name__ == '__main__':
    #analyze_typing_for_all()
    #print(analyze_typing_for_one_session("oo753", "B", threshold=8))
    #plot_active_diagram_for_one_session("oo753", "B", 15)
    #plot_active_diagram_for_all()
    plot_aggregated_diagram()

