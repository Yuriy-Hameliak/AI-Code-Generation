import unittest
from expression_calculator_new import calculate_expression

class TestCalculateExpression(unittest.TestCase):
    """
    Тестовий клас для функції `calculate_expression`.
    """

    def test_valid_expressions(self):
        """
        Тестування коректних виразів.
        """
        test_cases = [
            ("Скільки буде 8 відняти 3?", 5),
            ("Скільки буде 7 додати 3 помножити на 5?", 50),
            ("Скільки буде 10 поділити на -2 додати 11 мінус -3?", 9),
            ("Скільки буде 15 додати 2 помножити на 3 мінус 4 поділити на 2?", 23),
            ("Скільки буде 10 помножити на 2 додати 5 відняти 1?", 24),
            ("Скільки буде 20 поділити на 4 - 3 + 1?", 3),
            ("Скільки буде сім додати", "Неправильний вираз!"),  # Missing operand after "+"
            ("Скільки буде десять ділити на", "Неправильний вираз!"),  # Missing operand after "/"
            # Extra operator tests
            ("Скільки буде десять плюс два плюс", "Неправильний вираз!"),  # Extra "+" at the end
            ("Скільки буде п'ять помножити на три множити на", "Неправильний вираз!"),  # Extra "множити на"
            # Unsupported operator tests
            ("Скільки буде десять залишок від двох", "Неправильний вираз!")
            ]

        for expression, expected_result in test_cases:
            result = calculate_expression(expression)
            self.assertEqual(result, expected_result, f"Неправильний результат для виразу: {expression}")

    def test_invalid_expressions(self):
        """
        Тестування некоректних виразів.
        """
        invalid_expressions = [
            "Неправильний вираз!",
            "Скільки буде 7 додати 5",
            "Скільки буде 10 * 2 / 0?",
            "Скільки буде 15 + 2 * 3 - 4 /?",
            "Скільки буде текст + 5 - 1?",
            "Скільки буде 20 / 4 - 3 + текст?",
            "Скільки буде 12A + 4B - 7C?",
            "Скільки буде 100 * 20 - 500 / 10D?",
            "Скільки буде 30 / 3 + 20 - 10$?",
            "Скільки буде 5 ** 3 - 2 * 1%?",
            "Скільки буде 100 // 2 + 50 % 3^?"
        ]

        for expression in invalid_expressions:
            result = calculate_expression(expression)
            self.assertEqual(result, "Неправильний вираз!", f"Неправильна обробка виразу: {expression}")

    def test_edge_cases(self):
        """
        Тестування граничних випадків.
        """
        edge_cases = [
            ("Скільки буде 0 + 0?", 0),
            ("Скільки буде 0 - 0?", 0),
            ("Скільки буде 0 * 0?", 0),
            ("Скільки буде 0 / 1?", 0),
            ("Скільки буде 1 / 0?", "Неправильний вираз!"),
            ("Скільки буде -1 * -1?", 1),
            ("Скільки буде -10 / -2?", 5),
        ]

        for expression, expected_result in edge_cases:
            result = calculate_expression(expression)
            self.assertEqual(result, expected_result, f"Неправильна обробка граничного випадку: {expression}")

if __name__ == "__main__":
    unittest.main()