package Assignment1;

public class SmartGlass extends Wearable {
	private int deviceId = 0;
	private String name;
	private String deviceType = "Wearable";
	private static int count = 0; 
	
	public SmartGlass(String name) {
		super(name);
		count = count +1;
		deviceId = count;
	}

	
	public int compareToSmartGlass(SmartGlass SG) {
		if(this.compareTo(SG) == 1) {
			return 1;
		}
		else {
			return 0;
		}
	}

}
