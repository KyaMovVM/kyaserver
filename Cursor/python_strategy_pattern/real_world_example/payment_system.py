"""
РЕАЛЬНЫЙ ПРИМЕР: Система оплаты
================================

Паттерн Стратегия в реальном приложении.
Разные способы оплаты — это разные стратегии!
"""

import sys
import io

# Исправление кодировки для Windows консоли
''
if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        elif hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass  # Игнорируем ошибки кодировки

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


# ═══════════════════════════════════════════════════════════════
# ИНТЕРФЕЙС СТРАТЕГИИ ОПЛАТЫ
# ═══════════════════════════════════════════════════════════════

class PaymentStrategy(ABC):
    """
    Интерфейс для всех способов оплаты.
    
    Каждый конкретный способ оплаты реализует этот интерфейс,
    но внутренняя логика совершенно разная.
    """
    
    @abstractmethod
    def pay(self, amount: float) -> bool:
        """
        Провести оплату.
        
        Args:
            amount: Сумма к оплате
            
        Returns:
            True если оплата успешна, False иначе
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Название способа оплаты."""
        pass


# ═══════════════════════════════════════════════════════════════
# КОНКРЕТНЫЕ СТРАТЕГИИ ОПЛАТЫ
# ═══════════════════════════════════════════════════════════════

class CreditCardPayment(PaymentStrategy):
    """Оплата кредитной картой."""
    
    def __init__(self, card_number: str, cvv: str, expiry: str):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry
    
    def pay(self, amount: float) -> bool:
        # Здесь была бы реальная интеграция с платёжной системой
        masked_card = f"****{self.card_number[-4:]}"
        print(f"    💳 Оплата {amount:.2f}₽ картой {masked_card}")
        print(f"    ✓ Связываемся с банком...")
        print(f"    ✓ Проверка CVV...")
        print(f"    ✓ Оплата подтверждена!")
        return True
    
    def get_name(self) -> str:
        return "Кредитная карта"


class PayPalPayment(PaymentStrategy):
    """Оплата через PayPal."""
    
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> bool:
        print(f"    🅿️  Оплата {amount:.2f}₽ через PayPal")
        print(f"    ✓ Авторизация аккаунта {self.email}...")
        print(f"    ✓ Перевод средств...")
        print(f"    ✓ Оплата подтверждена!")
        return True
    
    def get_name(self) -> str:
        return "PayPal"


class CryptoPayment(PaymentStrategy):
    """Оплата криптовалютой."""
    
    def __init__(self, wallet_address: str, currency: str = "BTC"):
        self.wallet_address = wallet_address
        self.currency = currency
    
    def pay(self, amount: float) -> bool:
        crypto_amount = amount / 5_000_000  # примерный курс
        print(f"    ₿ Оплата {amount:.2f}₽ ({crypto_amount:.8f} {self.currency})")
        print(f"    ✓ Генерация транзакции...")
        print(f"    ✓ Ожидание подтверждений блокчейна...")
        print(f"    ✓ Транзакция подтверждена!")
        return True
    
    def get_name(self) -> str:
        return f"Криптовалюта ({self.currency})"


class CashOnDeliveryPayment(PaymentStrategy):
    """Оплата при получении (наличными)."""
    
    def __init__(self, phone: str):
        self.phone = phone
    
    def pay(self, amount: float) -> bool:
        print(f"    💵 Оплата {amount:.2f}₽ при получении")
        print(f"    ✓ SMS-подтверждение на {self.phone}...")
        print(f"    ✓ Заказ оформлен, оплата при доставке!")
        return True
    
    def get_name(self) -> str:
        return "Наличные при получении"


class SBPPayment(PaymentStrategy):
    """Оплата через Систему Быстрых Платежей."""
    
    def __init__(self, phone: str, bank: str):
        self.phone = phone
        self.bank = bank
    
    def pay(self, amount: float) -> bool:
        print(f"    📱 Оплата {amount:.2f}₽ через СБП")
        print(f"    ✓ Запрос в {self.bank}...")
        print(f"    ✓ Push-уведомление на {self.phone}...")
        print(f"    ✓ Оплата подтверждена!")
        return True
    
    def get_name(self) -> str:
        return f"СБП ({self.bank})"


# ═══════════════════════════════════════════════════════════════
# КОНТЕКСТ: КОРЗИНА ПОКУПОК
# ═══════════════════════════════════════════════════════════════

@dataclass
class CartItem:
    """Товар в корзине."""
    name: str
    price: float
    quantity: int = 1


class ShoppingCart:
    """
    Корзина покупок — КОНТЕКСТ паттерна Стратегия.
    
    Корзина содержит ссылку на стратегию оплаты,
    но не знает деталей реализации каждого способа.
    """
    
    def __init__(self):
        self.items: list[CartItem] = []
        self.payment_strategy: Optional[PaymentStrategy] = None
    
    def add_item(self, item: CartItem) -> None:
        """Добавить товар в корзину."""
        self.items.append(item)
        print(f"  + Добавлено: {item.name} x{item.quantity} = {item.price * item.quantity:.2f}₽")
    
    def get_total(self) -> float:
        """Подсчитать общую сумму."""
        return sum(item.price * item.quantity for item in self.items)
    
    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        """
        Установить способ оплаты.
        
        🌟 Это ключевой метод паттерна Стратегия!
        Позволяет менять способ оплаты на лету.
        """
        self.payment_strategy = strategy
        print(f"\n  ⚙️  Выбран способ оплаты: {strategy.get_name()}")
    
    def checkout(self) -> bool:
        """
        Оформить заказ и провести оплату.
        
        Корзина ДЕЛЕГИРУЕТ оплату объекту-стратегии.
        Она не знает, КАК именно будет проведена оплата.
        """
        if not self.items:
            print("  ❌ Корзина пуста!")
            return False
        
        if not self.payment_strategy:
            print("  ❌ Не выбран способ оплаты!")
            return False
        
        total = self.get_total()
        print(f"\n  📋 Оформление заказа на сумму {total:.2f}₽")
        print("-" * 50)
        
        # Делегируем оплату стратегии
        success = self.payment_strategy.pay(total)
        
        if success:
            print("-" * 50)
            print("  🎉 Заказ успешно оплачен!")
            self.items.clear()
        
        return success


# ═══════════════════════════════════════════════════════════════
# ДЕМОНСТРАЦИЯ
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("   ПАТТЕРН СТРАТЕГИЯ: Система оплаты")
    print("=" * 60)
    
    # Создаём корзину
    cart = ShoppingCart()
    
    # Добавляем товары
    print("\n🛒 КОРЗИНА ПОКУПОК:")
    print("-" * 60)
    cart.add_item(CartItem("Head First. Паттерны проектирования", 2500.0))
    cart.add_item(CartItem("Чистый код (Р. Мартин)", 1800.0))
    cart.add_item(CartItem("Закладки для книг", 150.0, quantity=3))
    
    print(f"\n  💰 ИТОГО: {cart.get_total():.2f}₽")
    
    # === Сценарий 1: Оплата картой ===
    print("\n" + "=" * 60)
    print("   СЦЕНАРИЙ 1: Оплата банковской картой")
    print("=" * 60)
    
    card_payment = CreditCardPayment(
        card_number="4111111111111234",
        cvv="123",
        expiry="12/25"
    )
    cart.set_payment_strategy(card_payment)
    
    # Добавляем товары заново (корзина очистилась)
    cart.add_item(CartItem("Head First. Паттерны проектирования", 2500.0))
    cart.checkout()
    
    # === Сценарий 2: Оплата через СБП ===
    print("\n" + "=" * 60)
    print("   СЦЕНАРИЙ 2: Передумали — хотим через СБП!")
    print("=" * 60)
    
    # Добавляем товар
    cart.add_item(CartItem("Рефакторинг (М. Фаулер)", 2200.0))
    
    # Меняем стратегию на лету!
    sbp_payment = SBPPayment(phone="+7-999-123-45-67", bank="Тинькофф")
    cart.set_payment_strategy(sbp_payment)
    cart.checkout()
    
    # === Сценарий 3: Оплата криптой ===
    print("\n" + "=" * 60)
    print("   СЦЕНАРИЙ 3: Оплата криптовалютой")
    print("=" * 60)
    
    cart.add_item(CartItem("Курс по блокчейну", 15000.0))
    
    crypto_payment = CryptoPayment(
        wallet_address="bc1qxy2kgdygjrsqtzq2n0yrf...",
        currency="BTC"
    )
    cart.set_payment_strategy(crypto_payment)
    cart.checkout()
    
    # Итоги
    print("\n" + "=" * 60)
    print("   💡 ЧТО МЫ УВИДЕЛИ:")
    print("=" * 60)
    print("""
    1. ShoppingCart не знает деталей оплаты
       → Только вызывает payment_strategy.pay(amount)
    
    2. Способы оплаты взаимозаменяемы
       → Все реализуют один интерфейс PaymentStrategy
    
    3. Можно менять способ оплаты на лету
       → cart.set_payment_strategy(новый_способ)
    
    4. Легко добавить новый способ оплаты
       → Создать класс, реализующий PaymentStrategy
       → НЕ менять ShoppingCart!
    
    Это и есть паттерн СТРАТЕГИЯ! 🎯
    """)


if __name__ == "__main__":
    main()
