"""
STEP 2A: ПОВЕДЕНИЯ (Стратегии)
==============================

Мы ВЫДЕЛИЛИ изменяющиеся части (fly и quack) в отдельные классы.
Каждое семейство поведений — это набор взаимозаменяемых алгоритмов.

Это и есть "стратегии" — разные способы выполнить одно действие.
"""

from abc import ABC, abstractmethod


# ═══════════════════════════════════════════════════════════════
# СЕМЕЙСТВО #1: ПОВЕДЕНИЯ ПОЛЁТА
# ═══════════════════════════════════════════════════════════════

class FlyBehavior(ABC):
    """
    Интерфейс для всех поведений полёта.
    
    Это КОНТРАКТ: любой класс, реализующий FlyBehavior,
    обязан предоставить метод fly().
    """
    
    @abstractmethod
    def fly(self) -> None:
        """Выполнить полёт (или его отсутствие)"""
        pass


class FlyWithWings(FlyBehavior):
    """Летает с помощью крыльев — настоящий полёт!"""
    
    def fly(self) -> None:
        print("    ✈️  Лечу! Машу крыльями!")


class FlyNoWay(FlyBehavior):
    """Не умеет летать вообще."""
    
    def fly(self) -> None:
        print("    🚫 Я не умею летать...")


class FlyRocketPowered(FlyBehavior):
    """Летает с реактивным двигателем! 🚀"""
    
    def fly(self) -> None:
        print("    🚀 ВЖУХ! Лечу на реактивной тяге!")


class FlyWithJetpack(FlyBehavior):
    """Летает с джетпаком."""
    
    def fly(self) -> None:
        print("    🎒 Лечу с джетпаком на спине!")


# ═══════════════════════════════════════════════════════════════
# СЕМЕЙСТВО #2: ПОВЕДЕНИЯ КРЯКАНЬЯ
# ═══════════════════════════════════════════════════════════════

class QuackBehavior(ABC):
    """
    Интерфейс для всех поведений кряканья.
    
    Разные утки издают разные звуки (или молчат).
    """
    
    @abstractmethod
    def quack(self) -> None:
        """Издать звук (или промолчать)"""
        pass


class Quack(QuackBehavior):
    """Обычное кряканье настоящей утки."""
    
    def quack(self) -> None:
        print("    🔊 Кря-кря!")


class Squeak(QuackBehavior):
    """Писк резиновой уточки."""
    
    def quack(self) -> None:
        print("    🔊 Пи-и-ик!")


class MuteQuack(QuackBehavior):
    """Молчание — для деревянных уток."""
    
    def quack(self) -> None:
        print("    🔇 << тишина >>")


class RoboQuack(QuackBehavior):
    """Электронный звук робо-утки."""
    
    def quack(self) -> None:
        print("    🤖 БЗЗЗ-КРЯ-БЗЗЗ!")


# ═══════════════════════════════════════════════════════════════
# ВИЗУАЛИЗАЦИЯ СЕМЕЙСТВ
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("   СЕМЕЙСТВА ПОВЕДЕНИЙ (СТРАТЕГИИ)")
    print("=" * 60)
    
    print("\n📦 Семейство FlyBehavior:")
    print("-" * 40)
    fly_behaviors = [FlyWithWings(), FlyNoWay(), FlyRocketPowered(), FlyWithJetpack()]
    for fb in fly_behaviors:
        print(f"  {fb.__class__.__name__}:")
        fb.fly()
    
    print("\n📦 Семейство QuackBehavior:")
    print("-" * 40)
    quack_behaviors = [Quack(), Squeak(), MuteQuack(), RoboQuack()]
    for qb in quack_behaviors:
        print(f"  {qb.__class__.__name__}:")
        qb.quack()
    
    print("\n" + "=" * 60)
    print("""
    💡 КЛЮЧЕВАЯ ИДЕЯ:
    
    Поведения — это ОТДЕЛЬНЫЕ объекты!
    Их можно:
    • Переиспользовать между разными утками
    • Заменять во время выполнения программы
    • Добавлять новые без изменения класса Duck
    
    ➡️ Смотрите duck_strategy.py чтобы увидеть,
       как Duck ИСПОЛЬЗУЕТ эти поведения!
    """)
