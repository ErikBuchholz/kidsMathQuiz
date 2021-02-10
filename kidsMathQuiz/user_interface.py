#
#
#
#

#
#
#
def display_dialogue(prob_text, question_num):
    print("\n")
    display_problem(prob_text, question_num)
    user_answer = get_answer()
    return user_answer

#
#
#
#
#
def display_problem(prob_text, question_num):
    print("Question #%d: %s" % (question_num, prob_text))

#
#
#
#
#
def get_answer():
    answer = input("> Your answer: ")
    return answer

#
#
#
#
def display_result(question_pass_fail, user_answer, correct_answer):

    if (question_pass_fail == True) :
        feedback = "Job well done!"
    else:
        feedback = "You will have to practice this problem again."

    # Handle blank answers
    if user_answer == '':
        result_string = "You failed to provide any answer at all."
    else:
        result_string = "Result: " + str(question_pass_fail) + ", you entered " + \
                        str(user_answer) + " and the correct answer is " + \
                        str(correct_answer) + "."

    print(result_string)
    print(feedback)

    return 0

# display_test_summary()
#
# Args: (float) percent_correct
#       (int) total_num_correct
#       (int) total_questions
#       (int) total_num_tries
# Rets:
def display_test_summary(percent_correct, total_num_correct, total_questions, total_num_tries):
    print("\n#########################################")
    print("    Test Summary")
    print("    %.2f%% correct the first time" % percent_correct)
    print("    %d correct of %d questions" % (total_num_correct, total_questions))
    print("    %d total tries (including repeats)" % total_num_tries)
    print("#########################################")

