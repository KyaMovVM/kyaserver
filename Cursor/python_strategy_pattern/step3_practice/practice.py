"""
STEP 3: ПРАКТИКА — Создай свою утку!
====================================

Теперь ваша очередь! 
Выполните задания ниже, чтобы закрепить понимание паттерна.

ЗАДАНИЯ:
--------
1. Создайте новое поведение полёта: FlyWithHelicopter
   (летает с пропеллером на голове)

2. Создайте новое поведение кряканья: SingQuack
   (утка поёт вместо кряканья)

3. Создайте новый тип утки: CyborgDuck
   - Изначально летает с джетпаком
   - Издаёт роботизированные звуки
   - Может переключаться между режимами!

4. БОНУС: Добавьте третье семейство поведений — SwimBehavior
   (разные стили плавания)

Раскомментируйте код ниже и дополните его!
"""

import sys
import io

# Исправление кодировки для Windows консоли
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        elif hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass  # Игнорируем ошибки кодировки

from abc import ABC, abstractmethod

# Импортируем готовые поведения
import sys
sys.path.insert(0, '../step2_solution')
from behaviors import (
    FlyBehavior, FlyWithWings, FlyNoWay, FlyRocketPowered, FlyWithJetpack,
    QuackBehavior, Quack, Squeak, MuteQuack, RoboQuack
)


# ═══════════════════════════════════════════════════════════════
# ЗАДАНИЕ 1: Новое поведение полёта
# ═══════════════════════════════════════════════════════════════

class FlyWithHelicopter(FlyBehavior):
    """
    TODO: Реализуйте полёт с пропеллером!
    Подсказка: просто выведите сообщение о полёте с пропеллером.
    """
    
    def fly(self) -> None:
        # ВАШ КОД ЗДЕСЬ
        print("    🚁 Лечу с пропеллером на голове! Вжжж-вжжж!")


# ═══════════════════════════════════════════════════════════════
# ЗАДАНИЕ 2: Новое поведение кряканья
# ═══════════════════════════════════════════════════════════════

class SingQuack(QuackBehavior):
    """
    TODO: Реализуйте пение вместо кряканья!
    """
    
    def quack(self) -> None:
        # ВАШ КОД ЗДЕСЬ
        print("    🎵 Ла-ла-ла! Я пою красиво! 🎶")


# ═══════════════════════════════════════════════════════════════
# БАЗОВЫЙ КЛАСС (копия из step2_solution)
# ═══════════════════════════════════════════════════════════════

class Duck(ABC):
    """Базовый класс утки с поддержкой стратегий."""
    
    def __init__(self):
        self.fly_behavior: FlyBehavior = None
        self.quack_behavior: QuackBehavior = None
    
    def perform_fly(self) -> None:
        if self.fly_behavior:
            self.fly_behavior.fly()
    
    def perform_quack(self) -> None:
        if self.quack_behavior:
            self.quack_behavior.quack()
    
    def swim(self) -> None:
        print("    🏊 Плыву по воде...")
    
    @abstractmethod
    def display(self) -> None:
        pass
    
    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        print(f"    ⚙️  Меняю режим полёта → {fb.__class__.__name__}")
        self.fly_behavior = fb
    
    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        print(f"    ⚙️  Меняю режим звука → {qb.__class__.__name__}")
        self.quack_behavior = qb


# ═══════════════════════════════════════════════════════════════
# ЗАДАНИЕ 3: Создайте CyborgDuck
# ═══════════════════════════════════════════════════════════════

class CyborgDuck(Duck):
    """
    Утка-киборг!
    
    TODO: 
    - В __init__ установите начальные поведения:
      - fly_behavior = FlyWithJetpack()
      - quack_behavior = RoboQuack()
    - Реализуйте display()
    """
    
    def __init__(self):
        super().__init__()
        # ВАШ КОД ЗДЕСЬ
        self.fly_behavior = FlyWithJetpack()
        self.quack_behavior = RoboQuack()
    
    def display(self) -> None:
        # ВАШ КОД ЗДЕСЬ
        print("🤖 Я УТКА-КИБОРГ — наполовину утка, наполовину машина!")


# ═══════════════════════════════════════════════════════════════
# ЗАДАНИЕ 4 (БОНУС): Третье семейство — SwimBehavior
# ═══════════════════════════════════════════════════════════════

class SwimBehavior(ABC):
    """
    БОНУС: Интерфейс для разных стилей плавания.
    """
    
    @abstractmethod
    def swim(self) -> None:
        pass


class SwimNormally(SwimBehavior):
    """Обычное плавание."""
    def swim(self) -> None:
        print("    🏊 Плыву спокойно по воде...")


class SwimFast(SwimBehavior):
    """Быстрое плавание."""
    def swim(self) -> None:
        print("    🏊‍♂️ Плыву на максимальной скорости! Буль-буль-буль!")


class SwimUnderwater(SwimBehavior):
    """Плавание под водой."""
    def swim(self) -> None:
        print("    🤿 Ныряю глубоко под воду...")


class CannotSwim(SwimBehavior):
    """Не умеет плавать (робо-утка?)."""
    def swim(self) -> None:
        print("    ⚠️  Я не могу плавать! Вызывайте спасателей!")


# ═══════════════════════════════════════════════════════════════
# ТЕСТИРОВАНИЕ ВАШИХ РЕШЕНИЙ
# ═══════════════════════════════════════════════════════════════

def test_new_behaviors():
    """Тест новых поведений."""
    print("=" * 65)
    print("   ТЕСТ НОВЫХ ПОВЕДЕНИЙ")
    print("=" * 65)
    
    print("\n🚁 FlyWithHelicopter:")
    helicopter = FlyWithHelicopter()
    helicopter.fly()
    
    print("\n🎵 SingQuack:")
    sing = SingQuack()
    sing.quack()


def test_cyborg_duck():
    """Тест утки-киборга."""
    print("\n" + "=" * 65)
    print("   ТЕСТ CYBORG DUCK")
    print("=" * 65)
    
    cyborg = CyborgDuck()
    print()
    cyborg.display()
    cyborg.perform_quack()
    cyborg.perform_fly()
    
    print("\n✨ Переключаем режимы киборга...")
    cyborg.set_fly_behavior(FlyWithHelicopter())
    cyborg.set_quack_behavior(SingQuack())
    
    print("\nНовый режим:")
    cyborg.perform_quack()
    cyborg.perform_fly()


def test_dynamic_behavior_change():
    """Демонстрация динамического изменения."""
    print("\n" + "=" * 65)
    print("   ДИНАМИЧЕСКОЕ ИЗМЕНЕНИЕ")
    print("=" * 65)
    
    print("\nСоздаём киборга...")
    cyborg = CyborgDuck()
    cyborg.display()
    
    print("\n--- Режим 1: Боевой ---")
    cyborg.set_fly_behavior(FlyRocketPowered())
    cyborg.set_quack_behavior(RoboQuack())
    cyborg.perform_fly()
    cyborg.perform_quack()
    
    print("\n--- Режим 2: Маскировка ---")
    cyborg.set_fly_behavior(FlyWithWings())
    cyborg.set_quack_behavior(Quack())
    cyborg.perform_fly()
    cyborg.perform_quack()
    
    print("\n--- Режим 3: Развлечение ---")
    cyborg.set_fly_behavior(FlyWithHelicopter())
    cyborg.set_quack_behavior(SingQuack())
    cyborg.perform_fly()
    cyborg.perform_quack()


def main():
    print("\n" + "🎓" * 32)
    print("   ПРАКТИКА: ПАТТЕРН СТРАТЕГИЯ")
    print("🎓" * 32)
    
    test_new_behaviors()
    test_cyborg_duck()
    test_dynamic_behavior_change()
    
    print("\n" + "=" * 65)
    print("   🎉 ПОЗДРАВЛЯЮ! Вы освоили паттерн Стратегия!")
    print("=" * 65)
    print("""
    📝 ЧТО ВЫ УЗНАЛИ:
    
    1. Как выделять изменяющееся поведение в отдельные классы
    2. Как использовать интерфейсы для определения семейств алгоритмов
    3. Как применять композицию вместо наследования
    4. Как менять поведение объекта во время выполнения
    
    📚 ФОРМУЛА ПАТТЕРНА СТРАТЕГИЯ:
    
    Клиент HAS-A Стратегия (интерфейс)
           ↓
    Конкретные стратегии реализуют интерфейс
           ↓
    Клиент делегирует работу текущей стратегии
           ↓
    Стратегию можно менять динамически!
    
    🔑 КОГДА ПРИМЕНЯТЬ:
    
    • Много похожих классов отличаются только поведением
    • Нужны разные варианты алгоритма
    • Алгоритм содержит данные, которые клиент знать не должен
    • Класс имеет множество поведений в виде условных операторов
    """)


if __name__ == "__main__":
    main()
