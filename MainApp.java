package Assignment1;

public class MainApp {

    public static void main(String[] args) {
        System.out.println("Hello");
        Device d1 = new SmartGlass("Google");

        Device d2 = new SmartTV("MI");

        System.out.println("The first device is :" + d1 +
                "\n" + "The second device is :" + d2);
        Connection c0 = new Connection(d1,d2);
//        System.out.println(d1.getDeviceName());
        System.out.println("The connection is :" + c0);

        ANetwork a = new CNetwork();
        a.setConnectionList(new Connection(new SmartGlass("mi"), new SmartPhone("Samsung")));
        a.setConnectionList(new Connection(new SmartPhone("Oppo"), new SmartTV("Realme")));
        a.setConnectionList(new Connection(new SmartTV("LG"), new SmartGlass("MI")));
        a.setConnectionList(new Connection(new SmartWatch("Realme"), new SmartPhone("Apple")));
        System.out.println(a);

//        Device d1 = new Device();
//        Device d2 = new Device();

        Connection c1 = new Connection(d1, d2);
        System.out.println(c1.compareTo(c1));
        System.out.println(d1.compareTo(d2));


    }

}
