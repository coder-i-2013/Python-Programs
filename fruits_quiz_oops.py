import random

class FruitQuiz:
    def __init__(self):
        self.questions = {
            "What is the color of an apple?": "red",
            "What is the color of an orange?": "orange",
            "What is the color of a watermelon?": "green",
            "What is the color of a banana?": "yellow",
            "Which fruit is known as the 'king of fruits'?": "mango",
            "Which fruit has seeds on its outer skin?": "strawberry",
            "Which fruit is the largest in the world?": "pumpkin",
            "Which fruit is high in potassium?": "banana",
            "Which fruit is used to make guacamole?": "avocado",
            "Which fruit is known for having a spiky skin and strong smell?": "durian"
        }
        self.score = 0  
        wrong= 0

    def quiz(self):
        print("Welcome to the Enhanced Fruit Quiz!")
        print("You will earn 1 point for each correct answer. Let's see how many you get!")
        print("-" * 50)

        while True:
            question, answer = random.choice(list(self.questions.items()))
            print(question)

            user_answer = input("Your answer: ").strip().lower()

            if user_answer == answer:
                print("Correct answer! 🎉")
                self.score += 1
            else:
                wrong= wrong+1
                print(f"Wrong answer. The correct answer is '{answer}'.")

            # Ask if the user wants to continue
            try:
                option = int(input("Enter 0 to play again or 1 to quit: "))
                if option == 1:
                    print(f"Thank you for playing! Your final score is: {self.score} 🎯,")
                    break
            except ValueError:
                print("Invalid input. Please enter 0 to continue or 1 to quit.")
        
        print("-" * 50)
        print("Goodbye! Hope to see you again soon!")

FruitQuiz().quiz()