public abstract class CondimentDecorator extends Beverage {
    protected Beverage beverage;

    public abstract String getDescription();

      // Делегируем getSize() обёрнутому напитку
      @Override
      public Size getSize() {
         return beverage.getSize();
    }
}
