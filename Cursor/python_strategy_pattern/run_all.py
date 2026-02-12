"""
ЗАПУСК ВСЕХ ПРИМЕРОВ
====================

Этот файл запускает все демонстрации по порядку.
Можно также запускать каждый файл отдельно.

Запуск: python run_all.py
"""

import os
import sys
from pathlib import Path


def run_example(name: str, path: str):
    """Запустить пример из файла."""
    print("\n")
    print("▀" * 70)
    print(f"  🚀 {name}")
    print("▀" * 70)
    
    # Меняем директорию для корректных импортов
    original_dir = os.getcwd()
    example_dir = Path(path).parent
    
    try:
        os.chdir(example_dir)
        
        # Читаем и выполняем файл
        with open(Path(path).name, 'r', encoding='utf-8') as f:
            code = f.read()
        
        exec(compile(code, path, 'exec'), {'__name__': '__main__'})
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
    finally:
        os.chdir(original_dir)


def main():
    base_path = Path(__file__).parent
    
    print("═" * 70)
    print("   📚 ИЗУЧАЕМ ПАТТЕРН СТРАТЕГИЯ")
    print("   По книге 'Head First. Паттерны проектирования'")
    print("═" * 70)
    
    print("""
    Учебный план:
    
    1️⃣  ПРОБЛЕМА: Почему наследование не работает
    2️⃣  РЕШЕНИЕ: Паттерн Стратегия с утками
    3️⃣  ПРАКТИКА: Создай свою утку
    4️⃣  РЕАЛЬНЫЙ ПРИМЕР: Система оплаты
    
    Нажмите Enter для начала...
    """)
    input()
    
    # Шаг 1: Проблема
    run_example(
        "ШАГ 1: ПРОБЛЕМА — Наследование",
        base_path / "step1_problem" / "duck_inheritance.py"
    )
    
    print("\n\n" + "─" * 70)
    print("  Нажмите Enter для продолжения...")
    input()
    
    # Шаг 2: Решение
    run_example(
        "ШАГ 2: РЕШЕНИЕ — Паттерн Стратегия",
        base_path / "step2_solution" / "duck_strategy.py"
    )
    
    print("\n\n" + "─" * 70)
    print("  Нажмите Enter для продолжения...")
    input()
    
    # Шаг 3: Практика
    run_example(
        "ШАГ 3: ПРАКТИКА — Твоя утка",
        base_path / "step3_practice" / "practice.py"
    )
    
    print("\n\n" + "─" * 70)
    print("  Нажмите Enter для продолжения...")
    input()
    
    # Шаг 4: Реальный пример
    run_example(
        "ШАГ 4: РЕАЛЬНЫЙ ПРИМЕР — Система оплаты",
        base_path / "real_world_example" / "payment_system.py"
    )
    
    # Финал
    print("\n\n" + "═" * 70)
    print("   🎓 ОБУЧЕНИЕ ЗАВЕРШЕНО!")
    print("═" * 70)
    print("""
    📋 ЧТО ВЫ ИЗУЧИЛИ:
    
    ✓ Почему наследование не всегда решение
    ✓ Принцип "Инкапсулируйте то, что изменяется"
    ✓ Принцип "Программируйте на уровне интерфейса"
    ✓ Принцип "Композиция лучше наследования"
    ✓ Паттерн Стратегия на примере уток
    ✓ Применение паттерна в реальном проекте
    
    📚 ДОПОЛНИТЕЛЬНЫЕ МАТЕРИАЛЫ:
    
    • README.md      — обзор и история проблемы
    • diagrams.md    — UML-диаграммы
    • cheatsheet.md  — шпаргалка по паттерну
    
    🎯 СЛЕДУЮЩИЙ ПАТТЕРН: Наблюдатель (Observer)
    """)


if __name__ == "__main__":
    main()
