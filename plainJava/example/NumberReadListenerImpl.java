package example;

public class NumberReadListenerImpl implements NumberReadListener {
   
    double totalSoFar = 0D;

    @Override
    public void numberRead(NumberReadEvent numberReadEvent) {
        totalSoFar += numberReadEvent.getNumber();
    }

    @Override
    public void numberStreamTerminated(NumberReadEvent numberReadEvent) {
        System.out.println("Sum of the number stream: " + totalSoFar);
    }
}