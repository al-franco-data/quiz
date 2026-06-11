# quiz_multiple_choice.py
# this file asks a question, and provides four possible answers, one of which is correct.


def show_question(question, available_choices):
    print()
    print(question["prompt"])

    for letter in available_choices:
        print(letter + ".", question["answers"][letter])


#  this section listens for the button press, accepts a valid choice, and returns that choice

def get_choice(available_choices):
    choice = input("Choose an answer: ").upper()

    while choice not in available_choices:
        choice = input("Please choose a valid answer: ").upper()

    return choice


def play_question(question, calculate_points):
    available_choices = list(question["answers"].keys())
    wrong_answers = 0

    print()
    print("=====================================")
    print("NEW QUESTION:")
    print("A correct answer is worth 100 points.")
    print()

    while len(available_choices) > 0:
        show_question(question, available_choices)
        choice = get_choice(available_choices)

        print()

        if choice == question["correct_answer"]:
            points = calculate_points(wrong_answers)
            print()
            print("***  Correct!  ***")
            print()
            print("Points earned:", points)
            return points

        wrong_answers = wrong_answers + 1
        available_choices.remove(choice)

        if len(available_choices) > 0:
            points_now = calculate_points(wrong_answers)
            print()
            print("        ---  Wrong answer!  ---")
            print()
            print("A correct answer is now worth", points_now, "points!")
            print()

    return 0


def play_quiz(questions, calculate_points):
    total_score = 0

    for question in questions:
        total_score = total_score + play_question(question, calculate_points)

    print()
    print("Quiz complete!")
    print()
    print("Total score:", total_score)


# This section lets this file run by itself.
# It only runs when this file is started directly.
# It does NOT run when menu.py imports this file.

if __name__ == "__main__":
    from questions import questions
    from scoring_25p import calculate_points

    play_quiz(questions, calculate_points)
