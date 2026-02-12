# Фабрика

У нового объекта имеется подходящее имя: мы назовем его Фабрикой.
Фабрика инкапсулирует подробности создания объектов. Метод
orderPizza() становится обычным клиентом фабрики SimplePizzaFactory.
Каждый раз, когда ему понадобится новая пицца, он просит фабрику
ее создать. Прошли те времена, когда метод orderPizza() должен был
знать, чем греческая пицца отличается от вегетарианской. Теперь метод
orderPizza() знает лишь то, что полученный им объект реализует интерфейс Pizza для вызова методов prepare(), bake(), cut() и box().
Осталось разобраться с некоторыми подробностями; например, чем заменяется код создания объекта в методе orderPizza()? Давайте реализуем
простую фабрику пиццы и узнаем...

``` java

Pizza orderPizza() {
    Pizza pizza = new Pizza();
    pizza.prepare();
    pizza.bake();
    pizza.cut();
    pizza.box();
    return pizza;
}


// Тип пиццы передается
// orderPizza при вызове.
Pizza orderPizza(String type) {
    Pizza pizza;
    if (type.equals(“cheese”)) {
         pizza = new CheesePizza();
    } else if (type.equals("greek")) {
        pizza = new GreekPizza();
    } else if (type.equals("pepperoni")) {
        pizza = new PepperoniPizza();
    }


    // В зависимости от типа мы
    // создаем экземпляр нужного
    // конкретного класса и присваиваем его переменной pizza.
    // Обратите внимание: каждый
    // тип пиццы должен реализовать интерфейс Pizza.
    pizza.prepare();
    pizza.bake();
    pizza.cut();
    pizza.box();
    return pizza;
}

// Получив объект Pizza, мы готовим
// его, выпекаем, разрезаем и кладем
// в коробку!
// Каждый подтип Pizza (CheesePizza,
// VeggiePizza и т. д.) умеет готовить
// себя.
```

Инкапсуляция создания объектов — это один из основных принципов проектирования. Он позволяет отделить логику создания объектов от логики использования объектов. Это позволяет упростить код и сделать его более модульным.

``` java
public class SimplePizzaFactory {
    public Pizza createPizza(String type) {
        Pizza pizza = null;
        if (type.equals(“cheese”)) {
            pizza = new CheesePizza();
        } else if (type.equals(“pepperoni”)) {
            pizza = new PepperoniPizza();
        } else if (type.equals(“clam”)) {
            pizza = new ClamPizza();
        } else if (type.equals(“veggie”)) {
            pizza = new VeggiePizza();
        }
        return pizza;
    }
}
Код параметризуется по типу
// пиццы, как и наш исходный метод orderPizza()
```