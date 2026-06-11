from questions import questions
from show_auto import play_show


def show_intro():
    print()
    print("Show Engine 2026")
    print("  by Al Franco")
    print("   Sphinx1195")
    print()
    print("Automatic presentation mode.")
    print()
    print("The purpose of engine_show.py is to pull from the data file--questions.py--to present or show the data, without requiring keyboard interaction.")
    print("It was placed into a separate file to act as a module, to make it easier to use and to understand, when writing new code.")


show_intro()
play_show(questions)
