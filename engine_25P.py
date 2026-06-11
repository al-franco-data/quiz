# Quiz Master
# This is a quiz project challenge amongst three friends.
# Goal: write a multiple choice quiz.
# My goal: write code that can later be repurposed as modules.

# this section imports objects from module files

from questions import questions
from quiz_multiple_choice import play_quiz
from scoring_25p import calculate_points


# this section defines an intro with purpose

def show_intro():
    print()
    print("Quiz Engine 25p 2026")
    print("  by Al Franco")
    print("   Sphinx1195")
    print()
    print("The purpose of engine_25.py is to cause the value of a correct answer to go down by 25 percent, each time an incorrect answer is selected.")
    print("It was placed into a separate file to act as a module, to make it easier to use and to understand, when writing new code.")
    print()

# this section displays the intro as defined, then quizes using ojbect questions imported from questions, and object calculate_points imported from scoring_25p

show_intro()
play_quiz(questions, calculate_points)
