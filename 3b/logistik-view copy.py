import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional


class LogisticPopulationModel:
    """
    Модель логистического роста популяции (дискретная версия).

    Уравнение: N_{t+1} = r * N_t * (1 - N_t / K)
    
    Где:
    - N_t — численность популяции в момент времени t
    - r — коэффициент роста (скорость воспроизводства)
    - K — ёмкость среды (максимальная устойчивая численность)
    """

    def __init__(self, initial_population: float, growth_rate: float, carrying_capacity: float):
        """
        Инициализация модели логистического роста.

        Параметры:
            initial_population : начальная численность популяции (N0 > 0)
            growth_rate : коэффициент роста (r > 0)
            carrying_capacity : ёмкость среды (K > 0)
            
        Исключения:
            ValueError: если параметры не соответствуют ограничениям
        """
        # Валидация входных параметров
        if initial_population <= 0:
            raise ValueError("Начальная численность должна быть положительной")
        if growth_rate <= 0:
            raise ValueError("Коэффициент роста должен быть положительным")
        if carrying_capacity <= 0:
            raise ValueError("Ёмкость среды должна быть положительной")

        # Сохраняем параметры в атрибутах экземпляра
        self.N0 = initial_population
        self.r = growth_rate
        self.K = carrying_capacity

    def simulate(self, years: int) -> np.ndarray:
        """
        Моделирует динамику популяции на заданный период.

        Параметры:
            years : количество лет для моделирования (years > 0)

        Возвращает:
            np.ndarray : массив численности популяции по годам
            
        Алгоритм:
            Для каждого года t: 
            N_{t+1} = r * N_t * (1 - N_t / K)
            
            Использует рекуррентное вычисление на основе предыдущего значения.
        """
        # Валидация параметров
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным")

        # Инициализируем массив для хранения динамики популяции
        population = np.zeros(years)
        population[0] = self.N0

        # Рекурсивно вычисляем популяцию на каждом следующем шаге
        for t in range(1, years):
            population[t] = (
                self.r * population[t - 1] * (1 - population[t - 1] / self.K)
            )

        return population

    def plot(self, years: int, ax: Optional[plt.Axes] = None) -> plt.Figure:
        """
        Визуализирует динамику популяции.

        Параметры:
            years : количество лет для отображения
            ax : объект осей matplotlib (если None — создаётся новая фигура)

        Возвращает:
            plt.Figure : объект фигуры с графиком
            
        График включает:
            - Линию динамики популяции
            - Горизонтальную линию ёмкости среды (K)
            - Подписи осей и легенду
        """
        # Получаем данные моделирования
        population = self.simulate(years)

        # Создаём график или используем переданную ось
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        else:
            fig = ax.get_figure()

        # Основной график динамики популяции
        ax.plot(
            range(years), population, 'bo-', 
            label='Численность популяции'
        )
        
        # Добавляем линию ёмкости среды для сравнения
        ax.axhline(
            y=self.K, color='r', linestyle='--',
            label=f'Ёмкость среды (K={self.K})'
        )

        # Форматирование графика
        ax.set_xlabel('Год')
        ax.set_ylabel('Численность')
        ax.set_title('Логистическое отображение популяции')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xticks(range(years))

        return fig

    def get_summary(self, years: int) -> Tuple[np.ndarray, dict]:
        """
        Возвращает данные моделирования и статистическую сводку.

        Параметры:
            years : количество лет для анализа

        Возвращает:
            tuple : 
                - массив численности популяции
                - словарь со статистикой:
                    min     : минимальная численность
                    max     : максимальная численность
                    mean    : средняя численность
                    final   : финальная численность
                    stable  : флаг стабильности (близость к K)
        """
        # Получаем данные моделирования
        population = self.simulate(years)

        # Рассчитываем статистику
        stats = {
            'min': np.min(population),
            'max': np.max(population),
            'mean': np.mean(population),
            'final': population[-1],
            'stable': bool(np.isclose(population[-1], self.K, rtol=0.05))
        }

        return population, stats


def main():
    """Основная функция для демонстрации работы модели."""
    # Параметры модели
    params = {
        'initial_population': 10.0,
        'growth_rate': 3.56995,
        'carrying_capacity': 150.0,
        'years': 9000
    }

    # Создание и проверка модели
    model = LogisticPopulationModel(
        initial_population=params['initial_population'],
        growth_rate=params['growth_rate'],
        carrying_capacity=params['carrying_capacity']
    )

    # Моделирование и визуализация
    fig = model.plot(years=params['years'])
    plt.show()

    # Получение и вывод результатов
    population, stats = model.get_summary(years=params['years'])

    print("Динамика популяции:")
    print("-" * 25)
    for year, count in enumerate(population):
        print(f"Год {year:2d}: {count:8.2f}")

    print("\nСтатистика:")
    print("-" * 25)
    print(f"Минимум:       {stats['min']:8.2f}")
    print(f"Максимум:      {stats['max']:8.2f}")
    print(f"Среднее:       {stats['mean']:8.2f}")
    print(f"Финальное:    {stats['final']:8.2f}")
    print(f"Стабильность:   {'Да' if stats['stable'] else 'Нет'}")


if __name__ == "__main__":
    main()
