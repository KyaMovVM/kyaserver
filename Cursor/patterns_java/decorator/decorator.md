# dec

``` java
public abstract class Beverage {
    String description = “Unknown Beverage”;

    public String getDescription() {
        return description;
    }

    public abstract double cost();
}
```

Beverage — абстрактный класс с двумя методами:
getDescription() и cost().

Метод getDescription
уже реализован, а метод cost() необходимо
реализовать в субклассах.

## Как видите, класс Beverage достаточно прост. Давайте реализуем абстрактный класс для дополнений

Объекты должны быть взаимозаменяемы с Beverage, поэтому
расширяем класс Beverage.

``` java
public abstract class CondimentDecorator extends Beverage {
    public abstract String getDescription();
}
```

Также все декораторы должны заново реализовать метод
getDescription(). Зачем? Скоро узнаете

``` java
// Все классы конкретных напитков расширяют Beverage.
public class Espresso extends Beverage {

    // Описание задается в конструкторе класса. Стоит напомнить, что
    // переменная description наследуется
    // от Beverage.
    public Espresso() {
        description = “Espresso”;
    }

    public double cost() {
        return 1.99;
    }

    // Остается вычислить стоимость напитка. В этом
    // классе беспокоиться о дополнениях не нужно, поэтому мы просто возвращаем стоимость «базового»
    // эспрессо: $1.99
}

public class HouseBlend extends Beverage {
    public HouseBlend() {
        description = “House Blend Coffee”;
    }

    public double cost() {
        return .89;
    }
}

// Другой класс напитка. От нас
// требуется лишь назначить подходящее описание и вернуть правильную стоимость.
// Два других класса напитков (DarkRoast
// и Decaf ) создаются аналогично.
```

Код декоратора Mocha:

``` java
// Класс декоратора расширяет CondimentDecorator.
// Не забудьте, что CondimentDecorator расширяет Beverage.
public class Mocha extends CondimentDecorator {
    // Чтобы в объекте Mocha хранилась
    // ссылка на Beverage, нам понадобятся:
    
    Beverage beverage;

    public Mocha(Beverage beverage) {  // Переменная для ссылки
        this.beverage = beverage;  //  Способ присваивания переменной ссылки на объект. Мы будем передавать ссылку при вызове конструктора
    }
    public String getDescription() {
        return beverage.getDescription() + “, Mocha”;  // В описании должны содержаться
                                                        // не только название напитка (допустим, «Dark Roast»), но и все дополнения — например, «Dark Roast,
                                                        // Mocha». Таким образом, мы сначала
                                                        // получаем описание, делегируя вызов
                                                        // декорируемому объекту, а затем
                                                        // присоединяем к нему строку «, Mocha».
    }

    public double cost() {
        return .20 + beverage.cost();
    }
}

public class Soy extends CondimentDecorator {
    // Чтобы в объекте Soy хранилась
    // ссылка на Beverage, нам понадобятся:
    
    Beverage beverage;

    public Soy(Beverage beverage) {  // Переменная для ссылки
        this.beverage = beverage;  //  Способ присваивания переменной ссылки на объект. Мы будем передавать ссылку при вызове конструктора
    }
    public String getDescription() {
        return beverage.getDescription() + “, Soy”;  // В описании должны содержаться
                                                        // не только название напитка (допустим, «Dark Roast»), но и все дополнения — например, «Dark Roast,
                                                        // Soy». Таким образом, мы сначала
                                                        // получаем описание, делегируя вызов
                                                        // декорируемому объекту, а затем
                                                        // присоединяем к нему строку ", Soy."
    }

    public double cost() {      // double — это тип данных с плавающей точкой двойной точности
        return .15 + beverage.cost();
    }
}

public class Whip extends CondimentDecorator {
    // Чтобы в объекте Whip хранилась
    // ссылка на Beverage, нам понадобятся:
    
    Beverage beverage;

    public Whip(Beverage beverage) {  // Переменная для ссылки
        this.beverage = beverage;  //  Способ присваивания переменной ссылки на объект. Мы будем передавать ссылку при вызове конструктора
    }
    public String getDescription() {
        return beverage.getDescription() + “, Whip”;  // В описании должны содержаться
                                                        // не только название напитка (допустим, «Dark Roast»), но и все дополнения — например, «Dark Roast,
                                                        // Soy». Таким образом, мы сначала
                                                        // получаем описание, делегируя вызов
                                                        // декорируемому объекту, а затем
                                                        // присоединяем к нему строку ", Whip."
    }

    public double cost() {      // double — это тип данных с плавающей точкой двойной точности
        return .20 + beverage.cost();
    }
}

```

Тестовый код для оформления заказов:

``` java
public class StarbuzzCoffee {

    public static void main(String args[]) { // Заказываем эспрессо без дополнений, выводим описание и стоимость
        Beverage beverage = new Espresso();
            System.out.println(beverage.getDescription()
            + “ $” + beverage.cost());

        Beverage beverage2 = new DarkRoast();  // Создаем объект DarkRoast
            beverage2 = new Mocha(beverage2); // «Заворачиваем» в объект Mocha...
            beverage2 = new Mocha(beverage2);
            beverage2 = new Whip(beverage2); // Потом во второй... И еще в объект Whip
            System.out.println(beverage2.getDescription()
                + “ $” + beverage2.cost());

        Beverage beverage3 = new HouseBlend();  // Напоследок заказываем «домашнюю смесь» с соей, шоколадом и взбитыми сливками.
            beverage3 = new Soy(beverage3);
            beverage3 = new Mocha(beverage3);
            beverage3 = new Whip(beverage3);
            System.out.println(beverage3.getDescription()
            + “ $” + beverage3.cost());
        }
    }

//  Более элегантный способ создания декорированных объектов будет представлен при описании
// паттерна Фабрика (а также паттерна Строитель в приложении)
```
