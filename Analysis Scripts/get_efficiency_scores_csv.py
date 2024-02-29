import csv
import sys
import os
import re

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
    with open("./scores/efficiency_plus_scores","r") as f:
        for line in f:
            participant_id, problem, best_or_last, timestamp, correctness_score, test01, test02, test03, test04, test05, test06, test07, test08, test09, test10, test11= line.rstrip().split()
            if participant_id == 'participant_id':
                continue
            else:
               return_list.append([participant_id, problem, best_or_last, timestamp, correctness_score, test01, test02, test03, test04, test05, test06, test07, test08, test09, test10, test11]) 
    return return_list

    

def write_to_csv():
    fields = ["participant_id","session", "session_type", "problem set", "problem", "best_or_last", "test01time", "test01error", "test02time", "test02error", "test03time", "test03error", "test04time", "test04error", "test05time", "test05error", "test06time", "test06error", "test07time", "test07error", "test08time", "test08error", "test09time", "test09error", "test10time", "test10error", "test11time", "test11error"]
    rows = []
    session_mapping = read_session_mapping()
    speed_analysis= read_speed_analysis()
    
    for item in speed_analysis:
        participant_id, problem, best_or_last, timestamp, correctness_score, test01, test02, test03, test04, test05, test06, test07, test08, test09, test10, test11 = item
        problem_set = problem[3]
        session, session_type = session_mapping[participant_id][problem_set]
        
        if problem.endswith('x'):
            problem = "1-lax"
        else:
            problem = problem[-1]
        row = [participant_id, session, session_type, problem_set, problem, best_or_last]
        for test in [test01,test02,test03,test04,test05,test06,test07,test08,test09,test10,test11]:
            runtime = 0
            error = "No_Error"
            runtime_and_error = re.findall(r'runtime:(.*?)optimaltime',test)[0]
            if "[" in runtime_and_error:
                error = re.findall(r'\[(.*?)\]', runtime_and_error)[0]
                runtime = runtime_and_error.split('[')[0]
            else:
                runtime = runtime_and_error
            row.extend([runtime, error])

        rows.append(row)

    with open('analysis/efficiency_scores.csv', 'w+') as f:
        csvwriter = csv.writer(f) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)

write_to_csv()