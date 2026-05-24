from questions import questions


def get_correct_answer(question):
    correct_letter = question["correct_answer"]
    return question["answers"][correct_letter]


def get_year_questions(questions):
    year_questions = []

    for question in questions:
        correct_answer = get_correct_answer(question)

        if correct_answer.isdigit():
            year_questions.append(question)

    return year_questions


def play_match_jeopardy(questions):
    year_questions = get_year_questions(questions)

    print()
    print("MATCH JEOPARDY")
    print("The answer to each event is a year.")
    print("Choose all events from the following year.")

    # basic version: we can refine option mixing next
    years = sorted(set(get_correct_answer(q) for q in year_questions))

    for year in years:
        print()
        print("=====================================")
        print("Choose all events from this year:")
        print(year)
        print()

        matching = []
        for question in year_questions:
            if get_correct_answer(question) == year:
                matching.append(question)

        options = matching[:]

        for number, question in enumerate(options, start=1):
            print(str(number) + ".", question["prompt"])

        print()
        print("Correct answers:", len(matching))
        input("Press ENTER for next year...")


play_match_jeopardy(questions)

