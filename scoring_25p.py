#  scoring_25p.py
# this short code subtracts 25 points for every wrong answer
# it is in a module to try using it in future code as a short module

def calculate_points(wrong_answers):
    return 100 - (wrong_answers * 25)
