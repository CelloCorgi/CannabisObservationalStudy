import csv
import sys
import os


def read_session_mapping():
    """
    {
        "abs33":{'A': [1,'High'], 'B': [2,'Sober']}
    }
    """
    
    session_mapping={}
    with open("./session_mapping.csv",'r',encoding="utf8") as data:
        for line in csv.DictReader(data):
            session_mapping[line['participant id']] = {line["session 1 problem set"]: [1,line['session 1 type']],
                                                       line["session 2 problem set"]: [2,line['session 2 type']]}
    return session_mapping

def read_speed_analysis():
    return_list = []
    with open("./keystrokes/speed_analysis","r") as f:
        for line in f:
            participant_id, problem_set, problem, total_num_typing_keystrokes, total_num_deletes, total_seconds, total_idle_time, total_active_time, typing_speed= line.rstrip().split()
            if participant_id == 'participant_id':
                continue
            else:
               return_list.append([participant_id, problem_set, problem, total_num_typing_keystrokes, total_num_deletes, total_seconds, total_idle_time, total_active_time, typing_speed]) 
    return return_list

    

def write_to_csv():
    fields = ["participant_id", "session", "session_type", "problem_set", "problem_num","total_num_typing_keystrokes", "total_num_deletes", "total_seconds", "total_idle_time", "total_active_time", "typing_speed"]
    rows = []
    session_mapping = read_session_mapping()
    speed_analysis= read_speed_analysis()
    
    for item in speed_analysis:
        participant_id, problem_set, problem, total_num_typing_keystrokes, total_num_deletes, total_seconds, total_idle_time, total_active_time, typing_speed = item
        session, session_type = session_mapping[participant_id][problem_set]
        rows.append([participant_id, session, session_type, problem_set, problem, total_num_typing_keystrokes, total_num_deletes, total_seconds, total_idle_time, total_active_time, typing_speed])

    with open('analysis/speed_analysis.csv', 'w+') as f:
        csvwriter = csv.writer(f) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)

write_to_csv()