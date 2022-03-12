package Assignment1;

public class SmartTV extends NonWearable {
	private int deviceId = 0;
	private String deviceName;
	private String deviceType = "Non-Wearable";
	private static int count = 0; 
	
	public SmartTV(String name) {
		super(name);
		count ++;
		deviceId = count;
	}
	
	public int compareToSmartTV(SmartTV ST) {
		if(this.compareTo(ST) == 1) {
			return 1;
		}
		else {
			return 0;
		}
	}
	

}
