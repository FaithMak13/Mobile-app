
import random

# Language Learning App
# Created by Faith

vocabulary = {
    "Spanish": [
        {"word": "Hello", "translation": "Hola"},
        {"word": "Thank you", "translation": "Gracias"},
        {"word": "Goodbye", "translation": "Adiós"},
        {"word": "Please", "translation": "Por favor"},
        {"word": "Good morning", "translation": "Buenos días"},
    ],
    "French": [
        {"word": "Hello", "translation": "Bonjour"},
        {"word": "Thank you", "translation": "Merci"},
        {"word": "Goodbye", "translation": "Au revoir"},
        {"word": "Please", "translation": "S'il vous plaît"},
        {"word": "Good morning", "translation": "Bonjour"},
    ],
    "Shona": [
        {"word": "Hello", "translation": "Mhoro"},
        {"word": "Thank you", "translation": "Ndatenda"},
        {"word": "Goodbye", "translation": "Sara zvakanaka"},
        {"word": "Please", "translation": "Ndapota"},
        {"word": "Good morning", "translation": "Mangwanani"},
    ],
}


def show_vocabulary(language):
    """Display words and their translations."""
    print(f"\n--- {language} Vocabulary ---")

    for item in vocabulary[language]:
        print(f"{item['word']} = {item['translation']}")


def take_quiz(language):
    """Ask translation questions and calculate the score."""
    questions = vocabulary[language][:]
    random.shuffle(questions)

    score = 0

    print(f"\n--- {language} Quiz ---")
    print("Choose the correct translation.")

    for item in questions:
        correct_answer = item["translation"]

        wrong_answers = [
            entry["translation"]
            for entry in vocabulary[language]
            if entry["translation"] != correct_answer
        ]

        options = [correct_answer]
        if wrong_answers:
            options.append(random.choice(wrong_answers))

        # Add more unique options where possible.
        for entry in vocabulary[language]:
            answer = entry["translation"]
            if answer not in options:
                options.append(answer)
            if len(options) == 3:
                break

        random.shuffle(options)

        print(f"\nWhat is '{item['word']}' in {language}?")
        for number, option in enumerate(options, start=1):
            print(f"{number}. {option}")

        choice = input("Enter your answer (1-3): ").strip()

        if choice in ("1", "2", "3"):
            if options[int(choice) - 1] == correct_answer:
                print("Correct! Well done.")
                score += 1
            else:
                print(f"Not quite. The correct answer is {correct_answer}.")
        else:
            print(f"Invalid choice. The correct answer is {correct_answer}.")

    print(f"\nYour score: {score}/{len(questions)}")
    percentage = score / len(questions) * 100
    print(f"Result: {percentage:.0f}%")


def main():
    """Display the main menu and run the app."""
    while True:
        print("\n===== LANGUAGE LEARNING APP =====")
        print("1. Learn vocabulary")
        print("2. Take a quiz")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "3":
            print("Thank you for learning. Goodbye!")
            break

        if choice not in ("1", "2"):
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        languages = list(vocabulary.keys())

        print("\nChoose a language:")
        for number, language in enumerate(languages, start=1):
            print(f"{number}. {language}")

        language_choice = input("Enter a language number: ").strip()

        if not language_choice.isdigit():
            print("Please enter a valid number.")
            continue

        index = int(language_choice) - 1

        if index < 0 or index >= len(languages):
            print("Invalid language selection.")
            continue

        language = languages[index]

        if choice == "1":
            show_vocabulary(language)
        else:
            take_quiz(language)


if __name__ == "__main__":
    main()
