#
#

PASS = True
FAIL: bool = False

# Floating point significant digits
ACCURACY_STANDARD = 0.0000001

#
#
#
#
def check_answer(user_answer, correct_answer):
    # Handle non-numeric answer
    if (user_answer.isnumeric() == False):
        return FAIL

    # Conclude answer is correct or not
    if (abs(float(user_answer) - float(correct_answer))) < ACCURACY_STANDARD:
        return PASS
    else:
        return FAIL

