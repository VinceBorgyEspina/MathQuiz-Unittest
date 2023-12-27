import random

class MathQuestion:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class MathQuestionGenerator:
    @staticmethod
    def generate_random_question():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        question_text = f"What is the sum of {num1} and {num2}?"
        return MathQuestion(question_text, correct_answer)

def main():
    print("Welcome to the Math Quiz!")

    # Generate a random math question
    question = MathQuestionGenerator.generate_random_question()

    # Display the question
    print(f"Question: {question.text}")

    # Get the user's answer
    user_answer_input = input("Your Answer: ")

    # Validate and check the answer
    try:
        user_answer = int(user_answer_input)
        if question.check_answer(user_answer):
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question.correct_answer}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
