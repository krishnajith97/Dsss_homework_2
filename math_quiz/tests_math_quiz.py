import unittest
from math_quiz import generate_random_number, select_operator, create_math_problem

class TestMathQuiz(unittest.TestCase):
    def test_generate_random_number(self):
        """Test if generated numbers are within the specified range"""
        # Test for default range
        for _ in range(10):
            number = generate_random_number()
            self.assertTrue(1 <= number <= 10)
        
        # Test for custom range
        for _ in range(10):
            number = generate_random_number(1, 5)
            self.assertTrue(1 <= number <= 5)
    
    def test_select_operator(self):
        """Test if operator is valid"""
        for _ in range(10):
            operator = select_operator()
            self.assertIn(operator, ['+', '-', '*'])
    
    def test_create_math_problem(self):
        """Test if problems are created correctly with right answers"""
        # Test addition
        problem, answer = create_math_problem(5, 3, '+')
        self.assertEqual(answer, 8)
        self.assertEqual(problem, "5 + 3")
        
        # Test subtraction
        problem, answer = create_math_problem(7, 2, '-')
        self.assertEqual(answer, 5)
        self.assertEqual(problem, "7 - 2")
        
        # Test multiplication
        problem, answer = create_math_problem(4, 3, '*')
        self.assertEqual(answer, 12)
        self.assertEqual(problem, "4 * 3")

if __name__ == '__main__':
    unittest.main()