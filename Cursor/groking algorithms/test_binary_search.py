"""Тесты для binary_search: абстрактный метод, Log2N, 128 элементов."""
import io
import math
import re
import unittest
from unittest import mock

from binary_search import (
    BinarySearchCore,
    CountStepsDecorator,
    LogNDecorator,
    SearchStrategy,
    binary_search,
    _core,
)


class TestSearchStrategyAbstract(unittest.TestCase):
    """Проверка абстрактного класса SearchStrategy."""

    def test_search_strategy_cannot_be_instantiated(self):
        """SearchStrategy — абстрактный, нельзя создать экземпляр напрямую."""
        with self.assertRaises(TypeError):
            SearchStrategy()

    def test_binary_search_core_is_search_strategy(self):
        """BinarySearchCore реализует SearchStrategy."""
        self.assertIsInstance(_core, SearchStrategy)
        self.assertTrue(hasattr(_core, "search") and callable(_core.search))


class TestLog2NFormula(unittest.TestCase):
    """Проверка формулы log2(n) для 128 элементов."""

    def test_max_steps_formula_for_128(self):
        """Макс. шагов для n=128: floor(log2(128)) + 1 = 8."""
        n = 128
        expected = math.floor(math.log2(n)) + 1
        self.assertEqual(expected, 8, "floor(log2(128)) + 1 должно быть 8")

    def test_log2n_decorator_uses_correct_formula(self):
        """LogNDecorator для n=128 даёт max_steps_theory = 8."""
        n = 128
        max_steps_theory = (math.floor(math.log2(n)) + 1) if n > 0 else 0
        self.assertEqual(max_steps_theory, 8)


class Test128Elements(unittest.TestCase):
    """Проверка поиска в списке из 128 элементов."""

    def setUp(self):
        self.arr_128 = list(range(128))

    def test_binary_search_finds_element(self):
        """Базовый поиск находит элемент."""
        self.assertEqual(binary_search(self.arr_128, 127), 127)
        self.assertEqual(binary_search(self.arr_128, 0), 0)
        self.assertEqual(binary_search(self.arr_128, 64), 64)
        self.assertIsNone(binary_search(self.arr_128, -1))
        self.assertIsNone(binary_search(self.arr_128, 128))

    def test_worst_case_steps_within_log2n(self):
        """Худший случай (поиск 127) — не более 8 шагов."""
        steps = []
        core = BinarySearchCore()

        def count_step():
            steps.append(1)

        result = core.search(self.arr_128, 127, step_callback=count_step)
        self.assertEqual(result, 127)
        actual_steps = len(steps)
        max_allowed = math.floor(math.log2(128)) + 1
        self.assertLessEqual(
            actual_steps,
            max_allowed,
            f"Шагов {actual_steps} > max {max_allowed} для n=128",
        )

    def test_count_steps_decorator_128_elements(self):
        """CountStepsDecorator: поиск 127 в 128 элементах даёт ≤ 8 шагов."""
        stdout_capture = io.StringIO()
        decorator = CountStepsDecorator(_core)
        with mock.patch("sys.stdout", stdout_capture):
            result = decorator.search(self.arr_128, 127)

        self.assertEqual(result, 127)
        out = stdout_capture.getvalue()
        self.assertIn("Шагов выполнено:", out)
        # Парсим число шагов из вывода "  → Шагов выполнено: N"
        match = re.search(r"Шагов выполнено:\s*(\d+)", out)
        self.assertIsNotNone(match, "Не найден подсчёт шагов в выводе")
        actual_steps = int(match.group(1))
        self.assertLessEqual(
            actual_steps,
            8,
            f"Шагов {actual_steps} > 8 для n=128",
        )

    def test_log_decorator_128_elements_steps_ok(self):
        """LogNDecorator: для 128 элементов шаги в пределах O(log n)."""
        stdout_capture = io.StringIO()
        decorator = LogNDecorator(_core)

        with mock.patch("sys.stdout", stdout_capture):
            result = decorator.search(self.arr_128, 127)

        self.assertEqual(result, 127)
        out = stdout_capture.getvalue()
        self.assertIn("log2(128)", out)
        self.assertIn("≈ 8.0", out)
        self.assertIn("В пределах O(log n): ✓", out)


if __name__ == "__main__":
    unittest.main()
