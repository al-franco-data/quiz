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


show_intro()
play_review(questions)
