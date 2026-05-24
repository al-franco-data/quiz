from questions import questions


def play_match_by_year(questions):
    grouped = {}

    for question in questions:
        correct_letter = question["correct_answer"]
        year = question["answers"][correct_letter]

        if year not in grouped:
            grouped[year] = []

        grouped[year].append(question["prompt"])

    for year in sorted(grouped):
        print()
        print("=====================================")
        print(year, "(there are", len(grouped[year]), "answers)")
        print()

        for item in grouped[year]:
            print("-", item)


play_match_by_year(questions)