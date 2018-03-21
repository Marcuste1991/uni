import java.util.Observable;

public class EuDModel extends Observable{
    int a, b, ggt, gz;

    public void setA(int a) {
        this.a = a;
    }

    public void setB(int b) {
        this.b = b;
    }

    public int getGgt() {
        return ggt;
    }

    public EuDModel(int a, int b) {
        super();
        this.a = a;
        this.b = b;
    }

    public EuDModel() {
        super();
        a = 0;
        b = 0;
    }

    public void ggt() {
        if(a == 0 || b == 0) {
            throw new IllegalArgumentException("Division 0");
        }
        else {
            if(a < b) {
                gz = a;
                a  = b;
                b  = gz;
            }
            do {
                ggt = a % b;
                a = b;
                b = ggt;
            } while ( b != 0);
        }
            setChanged();
            notifyObservers();
    }
}
