# match_jeopardy.py
# this file provides an answer in the form of a year, and the contestant or user must provide all correct questions that match that year

from questions import questions
import random


def get_correct_year(question):
    correct_letter = question["correct_answer"]
    return question["answers"][correct_letter]


def get_years(questions):
    years = []

    for question in questions:
        year = get_correct_year(question)

        if year not in years:
            years.append(year)

    return sorted(years)


def get_correct_questions_for_year(questions, year):
    correct_questions = []

    for question in questions:
        if get_correct_year(question) == year:
            correct_questions.append(question)

    return correct_questions


def get_wrong_questions_for_year(questions, year):
    wrong_questions = []

    for question in questions:
        if get_correct_year(question) != year:
            wrong_questions.append(question)

    return wrong_questions


def ask_year_question(year, questions):
    correct_questions = get_correct_questions_for_year(questions, year)
    wrong_questions = get_wrong_questions_for_year(questions, year)

    number_needed = 8 - len(correct_questions)
    distractors = random.sample(wrong_questions, number_needed)

    options = correct_questions + distractors
    random.shuffle(options)

    print()
    print("=====================================")
    print("MATCH JEOPARDY")
    print("Choose all events from this year:")
    print(year)
    print()

    for number, question in enumerate(options, start=1):
        print(str(number) + ".", question["prompt"])

    print()
    choice = input("Choose all correct numbers, separated by commas: ")

    selected_numbers = choice.replace(" ", "").split(",")

    selected_questions = []
    for number_text in selected_numbers:
        if number_text.isdigit():
            index = int(number_text) - 1
            if 0 <= index < len(options):
                selected_questions.append(options[index])

    print()

    if set(id(q) for q in selected_questions) == set(id(q) for q in correct_questions):
        print()
        print("*** Correct! ***")
    else:
        print()
        print("--- Not quite. ---")
        print()
        print("Correct answers:")
        for question in correct_questions:
            print("-", question["prompt"])


def play_match_jeopardy(questions):
    years = get_years(questions)

    for year in years:
        ask_year_question(year, questions)

    print()
    print("Match Jeopardy complete.")




# This section lets this file run by itself.
# It only runs when this file is started directly.
# It does NOT run when menu.py imports this file.

if __name__ == "__main__":
    from questions import questions

    play_match_jeopardy(questions)
