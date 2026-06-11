# train_drill_wrong.py
# this file trains by quizing questions and answers, then it repeats those that were answered icnorrectly

def ask_training_question(question):
    print()
    print("-------------------------------")
    print()
    print(question["prompt"])

    for letter, answer in question["answers"].items():
        print(letter + ".", answer)

    choice = input("Choose an answer: ").upper()

    print()

    while choice not in question["answers"].keys():
        choice = input("Please choose a valid answer: ").upper()

    if choice == question["correct_answer"]:
        print("*** Correct! ***")
        return True
    else:
        print()
        print("--- Wrong answer. ---")
        return False


def play_train(questions):
    missed_questions = []

    print()
    print("TRAIN MODE")
    print("Answer all questions. Missed questions will be drilled afterward.")

    for question in questions:
        correct = ask_training_question(question)

        if not correct:
            missed_questions.append(question)

    print()
    print("You missed", len(missed_questions), "questions.")

    if len(missed_questions) == 0:
        print("No drill needed.")
        return

    _ = input("Press ENTER to focus on those questions.")

    for round_number in range(1, 3):
        print()
        print("DRILL ROUND", round_number)

        for question in missed_questions:
            ask_training_question(question)

    print()
    print("Training complete.")


# This section lets this file run by itself.
# It only runs when this file is started directly.
# It does NOT run when menu.py imports this file.

if __name__ == "__main__":
    from questions import questions

    play_train(questions)
