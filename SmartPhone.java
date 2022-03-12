package Assignment1;

public class SmartPhone extends NonWearable {
	private int deviceId = 0;
	private String deviceName;
	private String deviceType = "Non-Wearable";
	private static int count = 0; 
	
	public SmartPhone(String name) {
		super(name);
		count ++;
		deviceId = count;
	}
	
	public int compareToSmartPhone(SmartPhone SP) {
		if(this.compareTo(SP) == 1) {
			return 1;
		}
		else {
			return 0;
		}
	}
}
