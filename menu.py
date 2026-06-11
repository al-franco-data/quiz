
# this section imports objects from specific files

from questions import questions
from show_auto import play_show
from review_flashcards import play_review
from match_jeopardy import play_match_jeopardy
from train_drill_wrong import play_train
from quiz_multiple_choice import play_quiz
from scoring_25p import calculate_points

# Menu options call these five behavior files:
# 1. show_auto.py
# 2. review_flashcards.py
# 3. match_jeopardy.py
# 4. train_drill_wrong.py
# 5. quiz_multiple_choice.py


# this section displays the menu

def show_menu():
    print()
    print("=====================================")
    print("QUIZ ENGINE MENU")
    print("1. Presentation Mode")
    print("2. Review Flashcards")
    print("3. Match Answers to Question")
    print("4. Train & Drill Those Missed")
    print("5. Quiz - Multiple Choice")
    print()
    print("Q. Quit")
    print()


# this section uses logic to respond appropriately to choices 1-5 or q, and ONLY to those options

while True:
    show_menu()
    choice = input("Choose an option: ").upper()

    if choice == "1":
        play_show(questions)

    elif choice == "2":
        play_review(questions)

    elif choice == "3":
        play_match_jeopardy(questions)

    elif choice == "4":
        play_train(questions)

    elif choice == "5":
        play_quiz(questions, calculate_points)

    elif choice == "Q":
        print("Goodbye.")
        break

    else:
        print("Please choose 1, 2, 3, 4, 5, or Q.")
