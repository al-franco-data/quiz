# Quiz Master
# This is a quiz project challenge amongst three friends.
# Goal: write a multiple choice quiz.
# My goal: write code that can later be repurposed as modules.

from questions import questions
from quiz_multiple_choice import play_quiz
from scoring_flat import calculate_points


def show_intro():
    print()
    print("Quiz Engine flat 2026")
    print("  by Al Franco")
    print("   Sphinx1195")
    print()
    print("The purpose of engine_flat.py is to cause the value of a correct answer to remain the same, even when an incorrect answer is selected.")
    print("It was placed into a separate file to act as a module, to make it easier to use and to understand, when writing new code.")
    print()


show_intro()
play_quiz(questions, calculate_points)
