package Assignment1;

import java.util.ArrayList;
import java.util.List;

public class CNetwork implements ANetwork {

    private List<Connection> connectionList;

    public CNetwork(){

        connectionList = new ArrayList<>();
    }

    public void setConnectionList(Connection connection){

        connectionList.add(connection);
    }

    @Override
    public void getName() {

        System.out.println("Ron");
    }

    @Override
    public String toString() {
        return "CNetwork{" +
                "connectionList=" + connectionList +
                '}';
    }
}
