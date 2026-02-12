public class Whip extends CondimentDecorator {
	public Whip(Beverage beverage) {
		this.beverage = beverage;
	}
 
	public String getDescription() {
		return beverage.getDescription() + ", Whip";
	}
 
	public double cost() {
		double cost = beverage.cost();
		switch (getSize()) {
			case TALL:   cost += .10; break;
			case GRANDE: cost += .15; break;
			case VENTI:  cost += .20; break;
		}
		return cost;
	}
}

