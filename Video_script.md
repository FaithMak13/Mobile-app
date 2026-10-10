# W06 Submit Module #3 — Video Presentation Script
**Project:** Language Learning App  
**Student:** Faith  
**Programming Language:** Python

## 1. Introduction — 30 seconds

Hello everyone. My name is Faith, and today I will be presenting my Module 3 project, which is called the Language Learning App.

The purpose of my application is to help beginners learn everyday vocabulary in different languages. The current version supports Spanish, French, and Shona.

Users can view vocabulary and translations, take a multiple-choice quiz, receive feedback on their answers, and see their final scores.

In this presentation, I will demonstrate how my program works, explain the main parts of my code, and share what I learned while developing the application.

## 2. Demonstration of the Software — 1 minute

*[Share your screen and run your program in VS Code.]*

I will begin by running my program.

As you can see, the application displays a main menu with three options. The first option allows users to learn vocabulary, the second allows them to take a quiz, and the third allows them to exit the program.

I will select the first option to learn vocabulary.

The program asks me to choose a language. For this demonstration, I will select Spanish.

The application now displays English words alongside their Spanish translations. This helps users learn common words and phrases.

Next, I will return to the main menu and select the quiz option. I will choose a language and answer the questions by entering the number corresponding to my selected answer.

The program tells me whether my answer is correct and displays the correct translation when I make a mistake. At the end, it calculates and displays my score and percentage.

Finally, the user can select the exit option to close the program.

This demonstration shows how the main features work together to create a simple language-learning experience.

## 3. Code Walkthrough — 2 minutes

*[Open language_app.py in VS Code and scroll through the code as you explain it.]*

Now I will explain how I developed the program.

At the beginning of my code, I import Python's built-in `random` module. I use this module to shuffle the quiz questions and randomize the answer choices.

Next, I created a dictionary called `vocabulary`. It stores the languages available in the application, along with their English words and translations. I used this structure because it allows me to organize vocabulary by language and add more words in the future.

The first function is called `show_vocabulary()`.

This function receives the selected language as a parameter and displays each word together with its translation. I used a loop to go through the vocabulary items and print them one by one.

The next function is `take_quiz()`.

This function creates a copy of the vocabulary list, shuffles the questions, and asks the user to translate English words into the selected language. It creates answer choices and checks whether the user's selection matches the correct translation.

I also used conditional statements to determine whether the answer is correct or incorrect. Each correct answer increases the score by one. When the quiz finishes, the program calculates the percentage and displays the final result.

The `main()` function controls the application. It displays the menu, accepts the user's choice, checks that the selection is valid, and calls the appropriate function.

I used a `while` loop so that users can continue learning or taking quizzes without restarting the program after every activity. The loop ends when the user chooses to exit.

Finally, the statement `if __name__ == "__main__":` ensures that the main function runs when I execute this Python file directly.

I added comments and function descriptions to make the code easier to understand and maintain.

## 4. Learning Reflection — 45 seconds


One of the important things I learned from this project was how to organize a program into separate functions. This made my code easier to read, test, and improve.

I also practised using dictionaries, lists, loops, conditional statements, user input, and functions. Another important lesson was the need to test different user choices, including incorrect inputs, so that the program can respond appropriately.

One challenge was making sure that the quiz checked answers correctly and calculated the final score. Working through these steps helped me improve my problem-solving and debugging skills.

In the future, I would like to develop a graphical mobile interface, add more languages and vocabulary, and save users' scores so that they can track their progress.

## 5. Conclusion — 20 seconds

In conclusion, my Language Learning App is a starting point for making language learning simple and interactive.

This project has helped me apply the Python programming concepts I have been learning and given me more confidence in developing software.

Thank you for watching my presentation.
