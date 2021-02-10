import sys
import file_io_manager
import problem_builder
import test_module
import user_interface
import answer_checker
import quiz_manager

PATH_TEST_FILE = "problem_sets/test_file.json"
PATH_SIMPLE_ADDITION_FILE = "problem_sets/simple_addition.json"

###############################################################################
# Tasks (Feb 2021)
# TODO: Get args from CLI
# TODO: Add try/except all over, especially with file i/o and arg receipt
# TODO: Build GUI
# TODO: Develop self-testing framework
# TODO: Make auto-generation utility for various problem set files
# TODO: Make student database (student files, read/write, update)
# TODO: Put everything into classes
# TODO: CLI invocation of utilities, not just starting the app in general
# TODO: Add proper fcn() headers, comments, and descriptions
# TODO: Figure out if there is a "conditional compilation" option in python
#       where I can auto-enable or auto-disable
# TODO: SRS and SDD (at least a list of features, CLI options, and purpose)
# TODO: Install and run static code analysis
# TODO: Verify no lines exceed 80 characters (for printers)
# TODO: Consider creating another entry point to run utilities instead of the
#       args for the main() CLI
# TODO:
# TODO:
# TODO:
# TODO:
###############################################################################

def make_randomized_problem_set():
    # Generate randomized problem set
    debug_path = "test_file.json"
    path = debug_path
    operand_type = "+"
    num_problems = 5
    num_vars = 3
    var_len_min = 1
    var_len_max = 5
    json_problem_contents = \
        problem_builder.make_new_problem_file(path, operand_type,
                                              num_problems, num_vars,
                                              var_len_min, var_len_max)
    file_io_manager.write_file(path, json_problem_contents)

def do_one_test_iteration(problem_set_list):
    retry_true_false = False
    question_idx = 0
    for prob in problem_set_list:
        if prob['tryAgain'] == True:
            # Create text for displaying problem
            prob_inst = problem_builder.assemble_problem(prob)

            # Get user answer
            user_answer = \
                user_interface.display_dialogue(prob_inst[0], question_idx)

            # Check for user escape
            if (user_answer == "x") or (user_answer == "X"):
                print("Exiting test run.")
                return False, problem_set_list

            # Evaluate PASS/FAIL
            question_pass_fail = \
                answer_checker.check_answer(user_answer, prob['result'])

            # Record question stats
            prob['numTries'] += 1
            if (question_pass_fail == True):
                prob['tryAgain'] = False
                prob['numCorrect'] += 1
            else:   # Question was answered incorrectly
                retry_true_false = True   # Wrong answer, try again
                prob['tryAgain'] = True   # Want to be sure
                prob['numWrong'] += 1

            # Record student stats

            # Display result of this question iteration
            user_interface.display_result(question_pass_fail, user_answer, prob['result'])

        # Increment counter
        question_idx += 1

    # End of one problem in list
    return retry_true_false, problem_set_list

#
# CLI Args:
# - Student Name
# - Desired Test File
#
if __name__ == '__main__':
    # Display args from invocation
    print("Invocation: python mathquiz.py <student_name> <test_file>")
    #print(f"Args count: {len(sys.argv)}")
    #for i, arg in enumerate(sys.argv):
    #    print(f"Argument {i:>2}: {arg}")

    student_name = sys.argv[1]
    test_file = sys.argv[2]

    # Check for errors (maybe this step is not needed here)

    # Import user record
    student_name_file = "student_records/" + student_name + ".json"
    student_record = file_io_manager.get_json_file(student_name_file)

    # Import math problem set
    test_file_name = "problem_sets/" + test_file + ".json"
    problem_set_dict = file_io_manager.get_json_file(test_file_name)
    problem_set_list = problem_set_dict['problem_set']

    # Data set self-test
    test_module.run_data_set_self_test(problem_set_list)

    # Create new test_record object and
    # Record quiz time hack
    current_test_record = quiz_manager.create_new_test_record(test_file_name)

    # Handle one problem per iteration
    retry_true_false = True
    test_iterations = 0
    while (retry_true_false == True):
        retry_true_false, problem_set_list = \
            do_one_test_iteration(problem_set_list)

    # Record the test run
    percent_correct, total_num_correct, total_questions, total_num_tries = \
        quiz_manager.record_test_run_stats(current_test_record, problem_set_list)

    # Display results
    user_interface.display_test_summary(percent_correct, total_num_correct, \
                                        total_questions, total_num_tries)

print("Exiting...")
