import java.util.LinkedHashMap;
import java.util.Map;

public class MapTest{
	public static void main(String[] args){
		Map<Integer,String> m = new LinkedHashMap<Integer,String>();
		m.put(new Integer(1),"Good");
		m.put(new Integer(2),"afternoon");
		m.put(new Integer(3),"!");
		
		System.out.println(m);
		System.out.println(m.size());
		System.out.println(m.getClass());
	}
}

		