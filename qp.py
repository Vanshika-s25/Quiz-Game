def quizApp():
    quizData = [
        {
            "question": "A view of database that appears to an application program is known as?",
            "options": ["1. Schema", "2. Subschema", "3. Virtual table", "4. Index table"],
            "answer": 2
        },
        {
            "question": "Which operation is used to extract specified columns from a table?",
            "options": ["1. Project", "2. Join", "3. Extract", "4. Table"],
            "answer": 1
        },
        {
            "question": "Which of the following can be considered as the maximum size that is supported by FAT?",
            "options": ["1. 8GB" ,"2. 4GB", "3. 4TB" ,"4. None of the above"],
            "answer": 2
        }
    ]

    print("Welcome to the Quiz App!\n")
    score = 0

    for i, q in enumerate(quizData):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}: {q['options'][q['answer'] - 1]}\n")

    print(f"Quiz Over! Your final score is {score}/{len(quizData)}")

if __name__ == "__main__":
    quizApp()