import json

# For creating randomized problem sets
import random

OPERATOR_END_STRING = "--------"



def make_new_problem_file(path, operand_type, num_problems,
                          num_vars, var_len_min, var_len_max):
    problem_list = \
        generate_problem_list_as_json(operand_type, num_problems,
                                      num_vars, var_len_min, var_len_max)

    print("PROBLEM_LIST:")
    print(problem_list)
    print("END PROBLEM_LIST:")


    # Make all the text we will write to file
    problem_list_as_string = ",".join(problem_list)
    return '{\n  \"problem_set\": [\n' + problem_list_as_string + '\n  ]\n}'

def generate_problem_list_as_json(operand_type, num_problems,
                                  num_vars, var_len_min, var_len_max):
    json_problem_list = []
    idx = 0
    while idx < num_problems:
        print("Creating randomized problem", idx)
        json_problem_list.append(make_json_problem_item(
            num_vars, operand_type, var_len_min, var_len_max))
        idx += 1

    print(">>>>>>>>>>>>>>>>>")
    print(json_problem_list)
    print(type(json_problem_list))
    print("<<<<<<<<<<<<<<<<<")

    return json_problem_list

#
#
#
#
#
def make_json_problem_item(num_vars, operand_type, var_len_min, var_len_max):
    vars = []
    operator = []
    var_val_min = 1 * 10 ** var_len_min
    var_val_max = 1 * (10 ** var_len_max + 1) - 1

    jdx = 0
    while jdx < (num_vars - 1):
        vars.append(random.randint(var_val_min, var_val_max))
        operator.append(operand_type)
        jdx += 1

    vars.append(random.randint(var_val_min, var_val_max))
    operator.append(OPERATOR_END_STRING)

    # Make Python json object
    pre_json_obj = {
        "vars": vars,
        "operator": operator,
        "result": 57,
        "numTries": 0,
        "numCorrect": 0,
        "numWrong": 0,
        "tryAgain": "True"
    }

    # Convert to json
    json_object = json.dumps(pre_json_obj)
    return json_object

#
#
def assemble_problem_as_line(prob_dict_item):
    question_string = ""
    idx = 0
    varlist = prob_dict_item['vars']
    num_elements = len(varlist)
    while idx < (num_elements - 1): # wish to avoid the "---" at end of operators
        question_string += str(varlist[idx])
        question_string += prob_dict_item['operator'][idx]
        idx += 1
    question_string += str(varlist[idx])

    return question_string

# assemble_problem()
# Returns tuple with a problem string and an answer
#
# Args: Single problem object
# Rets: Tuple, string (problem string) and answer (int)
def assemble_problem(prob_dict_item):
    question_string = "\n   "

    idx = 0
    for var in prob_dict_item['vars']:
        question_string += str(var)
        question_string += "\n "
        question_string += prob_dict_item['operator'][idx]
        question_string += " "
        idx += 1

    return question_string, prob_dict_item['result']


