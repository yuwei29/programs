package example;

public class Main {

    public static void main(String[] args) {
        NumberReader reader = new NumberReader();
        NumberReadListener listener = new NumberReadListenerImpl();
        reader.addNumberReadListener(listener);
        reader.start();
    }
}