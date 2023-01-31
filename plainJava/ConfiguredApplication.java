import java.io.File;
import java.io.FileInputStream;
 
public class ConfiguredApplication {
 
  public static void main(String[] args) throws Exception {
 
    // Data reading
    File file = new File("source.txt");
    FileInputStream stream = new FileInputStream(file);
 
    StringBuffer buffer = new StringBuffer();
 
    int character = 0;
    while ((character = stream.read()) != -1) {
      buffer.append((char) character);
    }
 
    stream.close();
 
    // Data use
    Integer readInteger = Integer.parseInt(buffer.toString());
    for (int i = 0; i < readInteger ; i++) {
      System.out.println("Hello world!");
    }
  }
}