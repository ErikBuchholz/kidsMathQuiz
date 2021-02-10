from datetime import datetime

# create_new_test_record()
#
# Args: (str) name of the test file used in this quiz run
# Ret: (dict) test record
def create_new_test_record(test_file_name):
    # Gather data
    now = datetime.now()
    date_time_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date = now.strftime("%m/%d/%Y")
    time = now.strftime("%H:%M:%S")

    # Make Python json object
    json_record_dict = {
        "test_file_taken": "test_file_name",
        "start_date_time": date_time_string,
        "end_date_time": date_time_string,
        "date_taken": date,
        "start_time_24hr": time,
        "end_time_24hr": time,
        "pass_fail": "Fail",
        "num_correct": 0,
        "num_incorrect": 0,
        "num_retries": 0
    }

    return json_record_dict


# record_test_run_stats()
# Updates the current test run object with data from end of run.
# Args: (dict) One json-style test record
#       (dict) list of all problems from the quiz set
# Rets: updated json-style test record
def record_test_run_stats(current_test_record, problem_set_list):
    print("Computing quiz results...")

    now = datetime.now()
    date_time_string = now.strftime("%d/%m/%Y %H:%M:%S")
    time_string = now.strftime("%H:%M:%S")

    total_num_tries = 0
    total_num_correct = 0
    total_num_incorrect = 0
    total_questions = 0
    for question in problem_set_list:
        total_questions += 1
        total_num_tries += int(question['numTries'])
        total_num_correct += int(question['numCorrect'])
        total_num_incorrect += int(question['numWrong'])

    current_test_record['end_date_time'] = date_time_string
    current_test_record['end_date_time'] = time_string

    # Compute pass/fail
    percent_correct = (total_num_correct/total_questions) * 100

    # Return tuple with:
    # percent correct the first time, total number correct,
    # total number of questions, total number of tries
    return \
        percent_correct, total_num_correct, \
        total_questions, total_num_tries

