import contextlib
import io
from pathlib import Path
import runpy
import string
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "Tiny-Python-Toys"


def load(name):
    return runpy.run_path(str(ROOT / (name + ".py.py")))


class ToysTests(unittest.TestCase):
    def test_imports_have_no_interaction_or_output(self):
        for path in ROOT.glob("*.py.py"):
            with self.subTest(path=path.name), patch("builtins.input", side_effect=AssertionError("input on import")):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    runpy.run_path(str(path))
                self.assertEqual(output.getvalue(), "")

    def test_arithmetic(self):
        evaluate = load("simple_calculator")["evaluate_expression"]
        for text, expected in [("2+3*4", 14), ("sqrt(9)", 3), ("math.sqrt(16)", 4), ("-2**2", -4), ("7//2", 3), ("7%2", 1)]:
            self.assertEqual(evaluate(text), expected)
        with self.assertRaises(ZeroDivisionError):
            evaluate("1/0")

    def test_rejects_code_and_unbounded_expressions(self):
        evaluate = load("simple_calculator")["evaluate_expression"]
        for text in ["__import__('os')", "(1).__class__", "[x for x in ()]", "True", "2**1000000", "1e999", "sqrt(-1)", "(-1)**0.5", "'x'*100", "1+" * 600 + "1"]:
            with self.subTest(text=text[:30]), self.assertRaises((ValueError, SyntaxError)):
                evaluate(text)

    def test_password_options(self):
        generate = load("password_generator")["generate_password"]
        for digits in [False, True]:
            for symbols in [False, True]:
                password = generate(20, digits, symbols)
                self.assertEqual(len(password), 20)
                self.assertTrue(any(c.isupper() for c in password))
                self.assertTrue(any(c.islower() for c in password))
                self.assertEqual(any(c.isdigit() for c in password), digits)
                self.assertEqual(any(c in string.punctuation for c in password), symbols)
        for length in [0, 3, -1, 4.5, True]:
            with self.assertRaises(ValueError):
                generate(length)

    def test_quicksort(self):
        sort = load("quick_sort")["quicksort"]
        for values in [[], [1], [3, -1, 3, 2, 0], list(range(100, 0, -1))]:
            original = values.copy()
            self.assertEqual(sort(values), sorted(values))
            self.assertEqual(values, original)

    def test_todo_completion_and_invalid_removal(self):
        module = load("todo_list")
        module["todos"].append("task")
        with patch("builtins.input", return_value="0"), contextlib.redirect_stdout(io.StringIO()):
            module["remove_todo"]()
        self.assertEqual(module["todos"], ["task"])
        with patch("builtins.input", return_value="1"), contextlib.redirect_stdout(io.StringIO()):
            module["mark_completed"]()
        self.assertEqual(module["todos"], [])
        self.assertEqual(module["completed_todos"], ["task"])

    def test_game_scoring(self):
        game = load("rock_paper_scissors")
        scores = {"赢": 0, "输": 0, "平局": 0}
        with patch("random.choice", return_value="剪刀"), patch("builtins.input", return_value="石头"), contextlib.redirect_stdout(io.StringIO()):
            game["play_game"](scores)
        self.assertEqual(scores, {"赢": 1, "输": 0, "平局": 0})


if __name__ == "__main__":
    unittest.main()
