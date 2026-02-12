# low = 0
# high = len(list) - 1

# Каждый раз алгоритм проверяет средний элемент

# mid = (low + hight) / 2 # Если значение (low+high) нечетно,
# guess = list[mid]       # то Python автоматически округляет значение mid в меньшую сторону.

# Если названное число было слишком мало,
# то переменная low обновляется соответственно:

# if guess < item:
#     low = mid + 1


import math
from abc import ABC, abstractmethod


# --- Абстрактный класс и композиция (паттерн Decorator) ---

class SearchStrategy(ABC):
    """Абстрактный базовый класс для стратегий поиска."""

    @abstractmethod
    def search(self, arr, item, step_callback=None):
        """Выполняет поиск элемента в массиве. Возвращает индекс или None."""
        pass

    def __call__(self, arr, item):
        """Позволяет вызывать как binary_search.steps(arr, item)."""
        return self.search(arr, item)


class SearchDecorator(SearchStrategy):
    """Базовый декоратор — композиция: оборачивает другую стратегию."""

    def __init__(self, wrapped: SearchStrategy):
        self._wrapped = wrapped  # композиция


class BinarySearchCore(SearchStrategy):
    """Базовый алгоритм бинарного поиска (ConcreteStrategy)."""

    def search(self, arr, item, step_callback=None):
        """Функция получает отсортированный массив и значение.
        Если значение присутствует — возвращает позицию, иначе None."""
        low = 0
        high = len(arr) - 1

        while low <= high:
            if step_callback:
                step_callback()
            mid = (low + high) // 2
            guess = arr[mid]

            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None


class CountStepsDecorator(SearchDecorator):
    """Декоратор подсчёта шагов (композиция)."""

    def search(self, arr, item, step_callback=None):
        counter = {'steps': 0}

        def cb():
            counter['steps'] += 1
            if step_callback:
                step_callback()

        result = self._wrapped.search(arr, item, step_callback=cb)
        print(f"  → Шагов выполнено: {counter['steps']}")
        return result


class LogNDecorator(SearchDecorator):
    """Декоратор вывода информации о log2(n) (композиция)."""

    def search(self, arr, item, step_callback=None):
        n = len(arr)
        max_steps_theory = (math.floor(math.log2(n)) + 1) if n > 0 else 0
        print(f"  → log2(n) = log2({n}) ≈ {max_steps_theory:.1f} (макс. шагов теоретически)")

        counter = {'steps': 0}

        def cb():
            counter['steps'] += 1
            if step_callback:
                step_callback()

        result = self._wrapped.search(arr, item, step_callback=cb)
        print(f"  → Шагов фактически: {counter['steps']}")
        print(f"  → В пределах O(log n): {'✓' if counter['steps'] <= max_steps_theory else '!'}")
        return result


# --- Функциональный API с атрибутами (binary_search.steps.log) ---

_core = BinarySearchCore()


def binary_search(arr, item):
    """Базовый вызов без декораторов."""
    return _core.search(arr, item)


# Композиция: декораторы оборачивают друг друга
binary_search.steps = CountStepsDecorator(_core)
binary_search.steps.log = LogNDecorator(binary_search.steps)
binary_search.log = LogNDecorator(_core)


# --- Примеры использования ---
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print("Без декоратора:")
    print(binary_search(my_list, 3))   # => 1
    print(binary_search(my_list, -1))  # => None

    print("\nbinary_search.steps:")
    print(binary_search.steps(my_list, 3))

    print("\nbinary_search.steps.log:")
    print(binary_search.steps.log(my_list, 3))

    # В списке 128 элементов, максимальное количество шагов поиска — ?
    # Псевдокод для бинарного поиска на русском языке:
# ОЪявляем функцию поиска с параметрами Список и Искомое значение.
# Объявляем начальную границу в которых выполняется поиск.
# Объявляем конечную границу в которых выполняется поиск.
# Равна размеру списка.
# Объявляем цикл с условием пока начальная граница не станет больше или равна конечной.
# Вычисляем средний элемент.
# Складываем начальную и конечную границу и делим на 2. Потому что мы делим список пополам.
# Это  нужно для того чтобы найти средний элемент.
# Его можно найти по другому? Формула нахождения среднего элемента: (low Z high) XY:
# Берем элемент из списка по индексу среднего элемента.
# Если элемент равен искомому значению, то возвращаем его позицию.
# Если элемент больше искомого значения, то перемещаем конечную границу на один элемент влево.
# Если элемент меньше искомого значения, то перемещаем начальную границу на один элемент вправо.
# Если границы сомкнулись, то возвращаем None.

    my_list1 = [x for x in range(128)]
    print(my_list1)

    print("\nПоиск 127 в списке из 128 элементов (binary_search.steps.log):")
    print(binary_search.steps.log(my_list1, 127))