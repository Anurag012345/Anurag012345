package Assignment1;

public interface Device {
	public String name = null;
	public int deviceId = 0;
	public String deviceType = null;
	public int getDeviceId();
	public String getDeviceName();
	public String getDeviceType();
	public int compareTo(Device Device);

}
