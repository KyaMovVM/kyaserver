// package headfirst.designpatterns.decorator.starbuzz;

public class Mocha extends CondimentDecorator {
	public Mocha(Beverage beverage) {
		this.beverage = beverage;
	}
 
	public String getDescription() {
		return beverage.getDescription() + ", Mocha";
	}
 
	public double cost() {
		double cost = beverage.cost();
		switch (getSize()) {
			case TALL:   cost += .15; break;
			case GRANDE: cost += .20; break;
			case VENTI:  cost += .25; break;
		}
		return cost;
	}
}
