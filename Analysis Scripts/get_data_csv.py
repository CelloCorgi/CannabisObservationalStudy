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

def read_correctness_scores():
    """
    {
        "abs33": {'setA-easy1': ['20230704220331', 0.75]
                  'setA-easy2': ['20230704233323', 0.50]}
    }
    """
    highest_scores = {}
    last_scores = {}
    with open("scores/highest_and_last_scores","r") as f:
        for line in f:
            participant_id, problem, best_time, best_score, last_time, last_score = line.rstrip().split()
            if participant_id == 'participant_id':
                continue
            if participant_id in highest_scores.keys():
                highest_scores[participant_id][problem] = [best_time, eval(best_score)]
                last_scores[participant_id][problem] = [last_time, eval(last_score)]
            else:
                highest_scores[participant_id] = {}
                highest_scores[participant_id][problem] = [best_time, eval(best_score)]
                last_scores[participant_id] = {}
                last_scores[participant_id][problem] = [last_time, eval(last_score)]
    return highest_scores,last_scores

    

def write_to_csv():
    fields = ["participant_id", "session", "session_type", "problem_set", "problem_num", "best_time", "best_score", "last_time", "last_score"]
    rows = []
    session_mapping = read_session_mapping()
    best_scores, last_scores = read_correctness_scores()
    for participant_id in best_scores.keys():
        print(participant_id)
        session_A, session_A_type = session_mapping[participant_id]['A']
        session_B, session_B_type = session_mapping[participant_id]['B']
        if 'setA-easy1' in best_scores[participant_id]:
            row = [participant_id, session_A, session_A_type, 'A', '1', best_scores[participant_id]['setA-easy1'][0], best_scores[participant_id]['setA-easy1'][1], last_scores[participant_id]['setA-easy1'][0], last_scores[participant_id]['setA-easy1'][1]]
            rows.append(row)
        else:
            print('setA-easy1 Not Found for ' + participant_id)
        if 'setA-easy2' in best_scores[participant_id]:
            row = [participant_id, session_A, session_A_type, 'A', '2', best_scores[participant_id]['setA-easy2'][0], best_scores[participant_id]['setA-easy2'][1], last_scores[participant_id]['setA-easy2'][0], last_scores[participant_id]['setA-easy2'][1]]
            rows.append(row)
        else:
            print('setA-easy2 Not Found for ' + participant_id)
        if 'setA-medium3' in best_scores[participant_id]:
            row = [participant_id, session_A, session_A_type, 'A', '3', best_scores[participant_id]['setA-medium3'][0], best_scores[participant_id]['setA-medium3'][1], last_scores[participant_id]['setA-medium3'][0], last_scores[participant_id]['setA-medium3'][1]]
            rows.append(row)
        else:
            print('setA-medium3 Not Found for ' + participant_id)
        if 'setB-easy1' in best_scores[participant_id]:
            row = [participant_id, session_B, session_B_type, 'B', '1', best_scores[participant_id]['setB-easy1'][0], best_scores[participant_id]['setB-easy1'][1], last_scores[participant_id]['setB-easy1'][0], last_scores[participant_id]['setB-easy1'][1]]
            rows.append(row)
        else:
            print('setB-easy1 Not Found for ' + participant_id)
        if 'setB-easy1-lax' in best_scores[participant_id]:
            row = [participant_id, session_B, session_B_type, 'B', '1-lax', best_scores[participant_id]['setB-easy1-lax'][0], best_scores[participant_id]['setB-easy1-lax'][1], last_scores[participant_id]['setB-easy1-lax'][0], last_scores[participant_id]['setB-easy1-lax'][1]]
            rows.append(row)
        else:
            print('setB-easy1-lax Not Found for ' + participant_id)
        if 'setB-easy2' in best_scores[participant_id]:
            row = [participant_id, session_B, session_B_type, 'B', '2', best_scores[participant_id]['setB-easy2'][0], best_scores[participant_id]['setB-easy2'][1], last_scores[participant_id]['setB-easy2'][0], last_scores[participant_id]['setB-easy2'][1]]
            rows.append(row)
        else:
            print('setB-easy2 Not Found for ' + participant_id)
        if 'setB-medium3' in best_scores[participant_id]:
            row = [participant_id, session_B, session_B_type, 'B', '3', best_scores[participant_id]['setB-medium3'][0], best_scores[participant_id]['setB-medium3'][1], last_scores[participant_id]['setB-medium3'][0], last_scores[participant_id]['setB-medium3'][1]]
            rows.append(row)
        else:
            print('setB-medium3 Not Found for ' + participant_id)
        
    with open('analysis/correctness_scores.csv', 'w+') as f:
        csvwriter = csv.writer(f) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)

write_to_csv()