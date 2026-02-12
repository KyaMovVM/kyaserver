"""
STEP 2B: ПАТТЕРН СТРАТЕГИЯ В ДЕЙСТВИИ
=====================================

Теперь класс Duck НЕ РЕАЛИЗУЕТ fly() и quack() сам.
Вместо этого он ДЕЛЕГИРУЕТ эти действия объектам-поведениям.

Это и есть паттерн Стратегия!
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
from behaviors import (
    # Поведения полёта
    FlyBehavior, FlyWithWings, FlyNoWay, FlyRocketPowered,
    # Поведения кряканья  
    QuackBehavior, Quack, Squeak, MuteQuack
)


# ═══════════════════════════════════════════════════════════════
# БАЗОВЫЙ КЛАСС DUCK
# ═══════════════════════════════════════════════════════════════

class Duck(ABC):
    """
    Базовый класс для всех уток.
    
    🌟 КЛЮЧЕВОЕ ОТЛИЧИЕ от наследования:
    Duck СОДЕРЖИТ поведения как переменные экземпляра (КОМПОЗИЦИЯ),
    а не наследует их.
    
    HAS-A лучше чем IS-A!
    (ИМЕЕТ поведение лучше чем ЯВЛЯЕТСЯ поведением)
    """
    
    def __init__(self):
        # Эти переменные объявлены как интерфейсы!
        # Конкретный тип назначается в подклассах
        self.fly_behavior: FlyBehavior = None
        self.quack_behavior: QuackBehavior = None
    
    def perform_fly(self) -> None:
        """
        Делегирует полёт объекту fly_behavior.
        
        Duck не знает КАК летать — он просто просит
        объект-поведение сделать это за него.
        """
        if self.fly_behavior:
            self.fly_behavior.fly()
    
    def perform_quack(self) -> None:
        """
        Делегирует кряканье объекту quack_behavior.
        """
        if self.quack_behavior:
            self.quack_behavior.quack()
    
    def swim(self) -> None:
        """Все утки плавают одинаково — это не меняется."""
        print("    🏊 Плыву по воде...")
    
    @abstractmethod
    def display(self) -> None:
        """Внешний вид — уникален для каждой утки."""
        pass
    
    # ═══════════════════════════════════════════════════════════
    # 🌟 МАГИЯ СТРАТЕГИИ: Можно менять поведение НА ЛЕТУ!
    # ═══════════════════════════════════════════════════════════
    
    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        """
        Установить новое поведение полёта.
        
        Это позволяет менять поведение ДИНАМИЧЕСКИ,
        во время выполнения программы!
        """
        print(f"    ⚙️  Меняю поведение полёта на {fb.__class__.__name__}")
        self.fly_behavior = fb
    
    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        """Установить новое поведение кряканья."""
        print(f"    ⚙️  Меняю поведение кряканья на {qb.__class__.__name__}")
        self.quack_behavior = qb


# ═══════════════════════════════════════════════════════════════
# КОНКРЕТНЫЕ УТКИ
# ═══════════════════════════════════════════════════════════════

class MallardDuck(Duck):
    """
    Кряква — настоящая дикая утка.
    Летает крыльями и крякает.
    """
    
    def __init__(self):
        super().__init__()
        # Кряква получает "настоящие" поведения
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()
    
    def display(self) -> None:
        print("🦆 Я КРЯКВА — зелёная голова, красивое оперение!")


class RedheadDuck(Duck):
    """Красноголовый нырок — тоже настоящая утка."""
    
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()
    
    def display(self) -> None:
        print("🦆 Я КРАСНОГОЛОВЫЙ НЫРОК — рыжая голова!")


class RubberDuck(Duck):
    """
    Резиновая уточка.
    НЕ летает (FlyNoWay) и пищит (Squeak).
    """
    
    def __init__(self):
        super().__init__()
        # Резиновая утка получает подходящие поведения
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()
    
    def display(self) -> None:
        print("🛁 Я РЕЗИНОВАЯ УТОЧКА — жёлтенькая и миленькая!")


class DecoyDuck(Duck):
    """
    Деревянная утка-приманка.
    НЕ летает и молчит.
    """
    
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()
    
    def display(self) -> None:
        print("🪵 Я ДЕРЕВЯННАЯ УТКА-ПРИМАНКА!")


class ModelDuck(Duck):
    """
    Модель утки — начинает без полёта,
    но можно установить реактивный двигатель!
    """
    
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()  # Изначально не летает
        self.quack_behavior = Quack()
    
    def display(self) -> None:
        print("🎮 Я МОДЕЛЬ УТКИ — для экспериментов!")


# ═══════════════════════════════════════════════════════════════
# ДЕМОНСТРАЦИЯ ПАТТЕРНА СТРАТЕГИЯ
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 65)
    print("   ПАТТЕРН СТРАТЕГИЯ В ДЕЙСТВИИ!")
    print("=" * 65)
    
    # --- Демонстрация разных уток ---
    print("\n📋 ДЕМОНСТРАЦИЯ РАЗНЫХ УТОК:")
    print("-" * 65)
    
    ducks = [
        MallardDuck(),
        RubberDuck(),
        DecoyDuck(),
    ]
    
    for duck in ducks:
        print()
        duck.display()
        duck.perform_quack()
        duck.perform_fly()
        duck.swim()
    
    # --- Магия динамического изменения ---
    print("\n" + "=" * 65)
    print("   🌟 ДИНАМИЧЕСКОЕ ИЗМЕНЕНИЕ ПОВЕДЕНИЯ!")
    print("=" * 65)
    
    print("\nСоздаём модель утки:")
    model = ModelDuck()
    model.display()
    
    print("\nПробуем лететь (изначально не умеет):")
    model.perform_fly()
    
    print("\n✨ Устанавливаем реактивный двигатель...")
    model.set_fly_behavior(FlyRocketPowered())
    
    print("\nТеперь пробуем лететь:")
    model.perform_fly()
    
    # --- Итоги ---
    print("\n" + "=" * 65)
    print("   ✅ ПРЕИМУЩЕСТВА ПАТТЕРНА СТРАТЕГИЯ:")
    print("=" * 65)
    print("""
    1. ГИБКОСТЬ:
       Можно менять поведение во время выполнения!
       (model.set_fly_behavior(FlyRocketPowered()))
    
    2. ПЕРЕИСПОЛЬЗОВАНИЕ:
       FlyNoWay используется и RubberDuck, и DecoyDuck
       Без дублирования кода!
    
    3. РАСШИРЯЕМОСТЬ:
       Добавить новое поведение (FlyWithHelicopter) —
       создать один новый класс, НЕ трогая Duck или подклассы!
    
    4. ТЕСТИРУЕМОСТЬ:
       Можно легко подставить mock-поведения для тестов.
    
    5. ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ:
       Код открыт для расширения, закрыт для модификации.
    """)
    
    print("=" * 65)
    print("   ➡️  Переходите к step3_practice/ для практики!")
    print("=" * 65)


if __name__ == "__main__":
    main()
