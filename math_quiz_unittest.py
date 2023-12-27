import unittest
from math_quiz import MathQuestion, MathQuestionGenerator

class TestMathQuiz(unittest.TestCase):
    def test_check_correct_answer(self):
        question = MathQuestion("What is the sum of 2 and 3?", 5)
        self.assertTrue(question.check_answer(5))

    def test_check_incorrect_answer(self):
        question = MathQuestion("What is the sum of 2 and 3?", 5)
        self.assertFalse(question.check_answer(4))

    def test_generate_random_question(self):
        question = MathQuestionGenerator.generate_random_question()
        self.assertIsNotNone(question)
        self.assertTrue(isinstance(question.text, str))
        self.assertTrue(isinstance(question.correct_answer, int))
        self.assertTrue(2 <= question.correct_answer <= 18)

if __name__ == "__main__":
    unittest.main()
