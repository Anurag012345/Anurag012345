package Assignment1;

public class NonWearable implements Device {
	
	private int deviceId;
	private String name;
	private String deviceType = "Non-Wearable";
	private static int count =0;
	
	public NonWearable(String name) {
		this.name = name;
		count ++;
		deviceId = count;
	}
	
	@Override
	public int getDeviceId() {

		return deviceId;
	}

	@Override
	public String getDeviceName() {

		return name;
	}

	@Override
	public String getDeviceType() {

		return deviceType;
	}

	@Override
	public String toString() {
		return "Device{"+ "deviceId=" + deviceId + '}';
	}

	@Override
	public int compareTo(Device device) {
		if (this.deviceId == device.deviceId && this.name.equals(device.name) && this.deviceType.equals(device.deviceType)){
            return 1;
        }
        else return 0;
    }

    
		
		
}
	


