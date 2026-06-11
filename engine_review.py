from questions import questions
from review_flashcards import play_review


def show_intro():
    print()
    print("Review Engine 2026")
    print("  by Al Franco")
    print("   Sphinx1195")
    print()
    print("Flashcard review mode.")
    print()
    print("The purpose of engine_review.py is to use the same data file to create a method of review, rather than quiz.")
    print("The immediate goal was to put the system to use, by pulling from the same data list to present/show data, review data, quiz data, etc..")
    print("It was placed into a separate file to act as a module, to make it easier to use and to understand, and when writing new code.")


show_intro()
play_review(questions)
