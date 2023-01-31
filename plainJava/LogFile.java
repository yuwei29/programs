import java.io.File;
import java.io.FileOutputStream;
import java.util.Date;

public class LogFile{
	public static void main(String[] args) throws Exception{
		File file = new File("log.txt");
		FileOutputStream stream = new FileOutputStream(file);
		String timeInString = new Date().toString();
		byte[] timeInBytes = timeInString.getBytes();
		stream.write(timeInBytes);
		stream.flush();
		stream.close();
	}
}

		