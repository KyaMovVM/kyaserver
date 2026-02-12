public abstract class Beverage {
    public enum Size { TALL, GRANDE, VENTI };
	Size size = Size.TALL;

    String description = "Unknown Beverage";

    public String getDescription() {
        return description;
    }


    public Size getSize() {
        return size;
    }

    public void setSize(Size size) {
        this.size = size;
    }

    public abstract double cost();
}

// Теперь кофе можно
// заказать в маленькой, средней или большой чашке. Starbuzz считает размер порции неотъемлемой частью класса кофе,
// поэтому в класс Beverage были добавлены два новых
// метода: setSize() и getSize(). Стоимость дополнений также зависит от размера порции,
// так что, скажем, добавка сои должна стоить 10, 15 или 20 центов для маленькой, средней или большой порции соответственно.
// Обновленный класс напитков показан ниже.
// Как бы вы изменили классы декораторов в соответствии с новыми требованиями?

