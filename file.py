QUIZ_FILE = "quiz_data.txt"

DEFAULT_QUIZ_DATA = [
    {
        "question": "A view of database that appears to an application program is known as??",
        "options":["1. Schema", "2. Subschema", "3. Virtual table", "4. Index table"],
        "correct_option": 2
    },
    {
        "question": "Which operation is used to extract specified columns from a table?",
        "options": ["1. Project", "2. Join", "3. Extract", "4. Table"],
        "correct_option": 1
    },
    {
        "question": " Which of the following can be considered as the maximum size that is supported by FAT?",
        "options": ["1. 8GB" ,"2. 4GB", "3. 4TB" ,"4. None of the above"],
        "correct_option": 2
    }
]

def load_quiz_data(file_path):
    quiz_data = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6): 
                if i + 5 < len(lines):  
                    question = lines[i].strip()
                    options = [lines[i + j].strip() for j in range(1, 5)]
                    correct_option = int(lines[i + 5].strip())
                    quiz_data.append({
                        "question": question,
                        "options": options,
                        "correct_option": correct_option
                    })
    except FileNotFoundError:
        print(f"{file_path} not found. Starting with default questions.")
    return quiz_data

def save_quiz_data(file_path, data):
    with open(file_path, "w") as file:
        for question in data:
            file.write(question["question"] + "\n")
            for option in question["options"]:
                file.write(option + "\n")
            file.write(str(question["correct_option"]) + "\n")

def play_quiz(quiz_data):
    score = 0
    for idx, question in enumerate(quiz_data):
        print(f"\nQuestion {idx + 1}: {question['question']}")
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        try:
            answer = int(input("\nEnter your answer (1-4): "))
            if answer == question["correct_option"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_option']}.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    print(f"\nYour final score: {score}/{len(quiz_data)}")

def main():
    print("Welcome to the Quiz App!\n")
    quiz_data = load_quiz_data(QUIZ_FILE)

    if not quiz_data:  
        quiz_data = DEFAULT_QUIZ_DATA
        save_quiz_data(QUIZ_FILE, quiz_data)

    print("Play the quiz")
    play_quiz(quiz_data)

if __name__ == "__main__":
    main()
