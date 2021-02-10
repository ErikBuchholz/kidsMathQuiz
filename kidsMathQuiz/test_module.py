import problem_builder

def run_data_set_self_test(problem_set_list):
    question_idx = 0
    for prob in problem_set_list:
        verify_result_is_correct(question_idx, prob)
        question_idx += 1

#
#
#
#

def verify_result_is_correct(prob_idx, problem_instance):
    prob_equation = problem_builder.assemble_problem_as_line(problem_instance)
    evaluated_result = eval(prob_equation)
    read_result = problem_instance["result"]

    if evaluated_result != problem_instance['result']:
        test_result = "FAIL"
    else:
        test_result = "PASS"

    print("%s - Problem %d: Computed: %s read: %s" %
                 (test_result, prob_idx,
                  evaluated_result, read_result))

