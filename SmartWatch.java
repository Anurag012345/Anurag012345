package Assignment1;

public class SmartWatch extends Wearable {
	private int deviceId = 0;
	private String name;
	private String deviceType = "Wearable";
	private static int count = 0; 
	
	public SmartWatch(String name) {
		super(name);
		count ++;
		deviceId = count;
	}
	
	public int compareToSmartWatch(SmartGlass SW) {
		if(this.compareTo(SW) == 1) {
			return 1;
		}
		else {
			return 0;
		}
	}

}
