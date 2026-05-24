import time


def show_item(question):
    print()
    print("=====================================")
    print("SHOW MODE")
    print()
    print(question["prompt"])

    time.sleep(5)

    correct_letter = question["correct_answer"]
    correct_answer = question["answers"][correct_letter]

    print()
    print(correct_answer)

    time.sleep(8)


def play_show(questions):
    for question in questions:
        show_item(question)

    print()
    print("Show complete.")


# This section lets this file run by itself.
# It only runs when this file is started directly.
# It does NOT run when menu.py imports this file.

if __name__ == "__main__":
    from questions import questions

    play_show(questions)