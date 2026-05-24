# Quiz Master
# This is a quiz project challenge amongst three friends.
# Goal: write a multiple choice quiz.
# My goal: write code that can later be repurposed as modules.

from questions import questions
from quiz_multiple_choice import play_quiz
from scoring_25p import calculate_points


def show_intro():
    print()
    print("Quiz Engine 25p 2026")
    print("  by Al Franco")
    print("   Sphinx1195")
    print()
    print("The subject of the questions is personal coding related history.")
    print()


show_intro()
play_quiz(questions, calculate_points)