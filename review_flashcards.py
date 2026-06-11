# review_flashcards.py
# this file reviews the presented data by showing it, then pausing until the user selects ENTER
# upon ENTER, the card is either turned over to show the answer, or left to focus on the next card

def show_flashcard(question):
    print()
    print("=====================================")
    print("FLASHCARD REVIEW")
    print()

    print(question["prompt"])

    _ = input("Press ENTER to show the answer...")

    correct_letter = question["correct_answer"]
    correct_answer = question["answers"][correct_letter]

    print()
    print(correct_answer)
    print()

    _ = input("Press ENTER for next card...")


def play_review(questions):
    for question in questions:
        show_flashcard(question)

    print()
    print("Flashcard review complete.")


# This section lets this file run by itself.
# It only runs when this file is started directly.
# It does NOT run when menu.py imports this file.

if __name__ == "__main__":
    from questions import questions

    play_review(questions)
