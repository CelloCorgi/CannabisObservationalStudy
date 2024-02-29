import os
import sys
import json
import subprocess
import shutil
import time
import pytest
from time import sleep
from tqdm import tqdm
from multiprocessing import Process, Manager, Value

def get_lax_score(timestamp, participant_id, loglaxfile):
    """
    Read from lax.json and append the score to participant_id's score.
    """
    passed_cases = 24
    num_cases = 24
    problem_name = "setB-easy1-lax"

    # count passed_cases
    with open(loglaxfile,'r') as f:
        data = f.readlines()
        for line in data:
            line_json = json.loads(line)
            if "outcome" in line_json and line_json['outcome'] == "failed":
                passed_cases -= 1
        if len(data) < 10:
            passed_cases = 0

    # write score to target file
    file_name = "./scores/correctness_all_files/" + participant_id
    
    with open(file_name,'a')as f:
        f.write(problem_name + " " + str(timestamp) + "  " + str(passed_cases) + "/" + str(num_cases) + '\n')

    os.remove(loglaxfile)

def get_score(logfile, timestamp, participant_id, problem):
    """
    Read from a pytest logfile and append the score to participant_id's score.
    """
    passed_cases = 0
    problem_name = ""
    num_cases = 0
    if problem == 1:
        num_cases = 27
        passed_cases = 27
        problem_name = "setA-easy1"
    elif problem == 2:
        num_cases = 34
        passed_cases = 34
        problem_name = "setA-easy2"
    elif problem == 3:
        num_cases = 24
        passed_cases = 24
        problem_name = "setA-medium3"
    elif problem == 4:
        num_cases = 24
        passed_cases = 24
        problem_name = "setB-easy1"
    elif problem == 5:
        num_cases = 24
        passed_cases = 24
        problem_name = "setB-easy2"
    elif problem == 6:
        num_cases = 32
        passed_cases = 32
        problem_name = "setB-medium3"

    # count passed_cases
    with open(logfile,'r') as f:
        data = f.readlines()
        for line in data:
            line_json=json.loads(line)
            if "outcome" in line_json and line_json['outcome'] == "failed":
                passed_cases -= 1
        if len(data) < 10:
            passed_cases = 0

    # write score to target file
    file_name = "./scores/correctness_all_files/"+participant_id
    with open(file_name, 'a')as f:
        f.write(problem_name + " " + str(timestamp) + "  " + str(passed_cases) + "/" + str(num_cases) + '\n')

def run_tests(file_name, participant_id, problem):
    # parse timestamp
    timestamp = ""
    if problem == 1 or problem == 2 or problem == 4 or problem ==5:
        timestamp = file_name[13:-3]
    elif problem == 3 or problem == 6:
        timestamp = file_name[15:-3]
    logfile = "correctness/log_" + participant_id + "_" + timestamp + ".json"
    loglaxfile = "correctness/log_lax_" + participant_id + "_" + timestamp + ".json"

    # run pytest
    if problem == 1:
        retcode = pytest.main(["correctness/test_easy1_correctness.py", "-q", "--report-log=" + logfile, "--show-capture=no"])
    elif problem == 2:
        retcode = pytest.main(["correctness/test_easy2_correctness.py", "-q", "--report-log=" + logfile, "--show-capture=no"])
    elif problem == 3:
        retcode = pytest.main(["correctness/test_medium3_correctness.py", "-q", "--report-log=" + logfile, "--show-capture=no"])
    elif problem == 4:
        retcode1 = pytest.main(["correctness/test_easy4lax_correctness.py", "-q", "--report-log=" + loglaxfile, "--show-capture=no"])
        get_lax_score(timestamp, participant_id, loglaxfile)
        retcode = pytest.main(["correctness/test_easy4_correctness.py", "-q", "--report-log=" + logfile, "--show-capture=no"])
    elif problem == 5:
        retcode = pytest.main(["correctness/test_easy5_correctness.py", "-q", "--report-log=" + logfile, "--show-capture=no"])
    elif problem == 6:
        retcode = pytest.main(["correctness/test_medium6_correctness.py", "-q", "--report-log=" + logfile, "--show-capture=no"])

    get_score(logfile, timestamp, participant_id, problem)
    os.remove(logfile)
    sleep(0.1)

def get_ignore_problems():
    """
    correctness_ignore:
    abs33 A1
    abs33 A2
    abs33 B3
    huihu A
    oijkk

    output:
    ignore = {"abs33":["A1","A2","B3"],"huihu":["A1","A2","A3"],"oijkk":["A1","A2","A3","B1","B2","B3"]}
    """
    ignore = {}
    with open("correctness/correctness_ignore","r") as f:
        for line in f:
            splitt = line.split()
            if len(splitt) == 2:
                participant_id, problem = splitt
                if problem == "A":
                    if participant_id in ignore.keys():
                        ignore[participant_id].extend(["A1","A2","A3"])
                    else:
                        ignore[participant_id] = ["A1","A2","A3"]
                if problem == "B":
                    if participant_id in ignore.keys():
                        ignore[participant_id].extend(["B1","B2","B3"])
                    else:
                        ignore[participant_id] = ["B1","B2","B3"]
                else:
                    if participant_id in ignore.keys():
                        ignore[participant_id].append(problem)
                    else:
                        ignore[participant_id] = [problem]
            elif len(splitt) == 1:
                ignore[splitt[0]] = ["A1","A2","A3","B1","B2","B3"]
    return ignore

def delete_session_scores(participant_id, problem_set):
    """
    Delete lines that belong to this session in scores/correctness_all_files/<participant_id>
    """
    new_lines = []
    if not os.path.isfile("scores/correctness_all_files/" + participant_id):
        return
    
    with open("scores/correctness_all_files/" + participant_id, 'r')as f: # eliminate those lines
        for line in f:
            if line.startswith("set" + problem_set):
                continue
            else:
                new_lines.append(line)
    with open("scores/correctness_all_files/" + participant_id, 'w+')as f: # replace the original file
        for line in new_lines:
            f.write(line)

def delete_scores(participant_id, problem_set, problem_number):
    """
    Delete lines that belong to this problem in scores/correctness_all_files/<participant_id>
    """
    if os.path.isfile("scores/correctness_all_files/" + participant_id):
            new_lines = []
            name = "-easy" + problem_number
            if problem_number == 3:
                name = "-medium3"
            with open("scores/correctness_all_files/" + participant_id, 'r')as f: # eliminate those lines
                for line in f:
                    if line.startswith("set" + problem_set + name):
                        continue
                    else:
                        new_lines.append(line)
            with open("scores/correctness_all_files/" + participant_id, 'w')as f: # replace the original file
                for line in new_lines:
                    f.write(line)

def main(args):
    test_data_directory = "./test_data/"
    list = os.listdir(test_data_directory)
    ignore = get_ignore_problems()

    if len(args) != 1: # run on one problem
        ignore = {} # don't consider ignore here, because we will always run tests on this problem
        folder_name = args[1] + "-" + args[2]
        assert folder_name in list, "folder " + folder_name + " doesn't exist under test_data/"
        list = [folder_name]

    for session in list:
        dash_index = session.find('-')
        participant_id = session[:dash_index]
        problem_set = session[-1]
        path = os.path.join(test_data_directory, session)
        file_names = os.listdir(path)
        if len(args) == 4: 
            # run on one problem, so only keep the files for that problem
            new_file_names = []
            for file in file_names:
                if file.startswith("problem" + args[3]):
                    new_file_names.append(file)
            file_names = new_file_names
            # delete original(if exist)lines of that problem in scores/correctness_all_files/<participant_id>
            delete_scores(args[1], args[2],args[3])
        if len(args) == 3:
            # run on one session, so only keep the files for that session
            delete_session_scores(args[1], args[2])
        
        pbar = tqdm(sorted(file_names), desc='description')
        for file_name in pbar:
            pbar.set_description("Processing "+ session)
            # exclude keystrokes.txt and terminal output files
            if file_name[0]=='k' or file_name[0]=='2':
                continue
            file_path = os.path.join(path,file_name)
            problem_num = file_name[7]

            # if this problem exists in correctness/correctness_ignore, then skip this problem; 
            # don't skip this problem if user wants to run on that single problem(len(args)!=1)
            if len(args) == 1 and participant_id in ignore.keys() and problem_set + problem_num in ignore[participant_id]:
                continue

            if problem_set == 'A':
                if problem_num == '1':
                    shutil.copy(file_path,"correctness/easy1.py")
                    process = Process(target=run_tests, args=(file_name, participant_id, 1))
                    process.start()
                    process.join()
                elif problem_num == '2':
                    shutil.copy(file_path,"correctness/easy2.py")
                    process = Process(target=run_tests, args=(file_name, participant_id, 2))
                    process.start()
                    process.join()
                elif problem_num == '3':
                    shutil.copy(file_path,"correctness/medium3.py")
                    process = Process(target=run_tests, args=(file_name, participant_id, 3))
                    process.start()
                    process.join()
            elif problem_set == 'B':
                if problem_num == '1':
                    shutil.copy(file_path,"correctness/easy4.py")
                    process = Process(target=run_tests, args=(file_name, participant_id, 4))
                    process.start()
                    process.join()
                elif problem_num == '2':
                    shutil.copy(file_path,"correctness/easy5.py")
                    process = Process(target=run_tests, args=(file_name, participant_id, 5))
                    process.start()
                    process.join()
                elif problem_num == '3':
                    shutil.copy(file_path,"correctness/medium6.py")
                    process = Process(target=run_tests, args=(file_name, participant_id, 6))
                    process.start()
                    process.join()



            
        
if __name__ == '__main__':
    # test_correctness.py --> run on all folders under test_data
    # test_correctness.py <participant_id> <problem set>
    #                     --> run on test_data/<participant_id>-<problem set>/*.py
    # test_correctness.py <participant_id> <problem set> <problem number>  
    #                     --> run on test_data/<participant_id>-<problem set>/<problem number>_*.py
    # Examples:
    # test_correctness.py abs33 A 2 --> run on test_data/abs33-A/problem2easy.py
    # test_correctness.py abs33 A --> run on test_data/abs33-A/*.py
    assert len(sys.argv) == 1 or len(sys.argv) == 3 or len(sys.argv) == 4
    if len(sys.argv) ==4 :
        assert(sys.argv[2] in ['A', 'B'] and sys.argv[3] in ['1','2','3'])
        assert(len(sys.argv)<=4)
    if len(sys.argv) == 3:
        assert(sys.argv[2] in ['A', 'B'])
    main(sys.argv)