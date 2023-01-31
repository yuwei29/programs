public class SpeedTest{
	public static void main(String[] args){
		int sum=0;
		long start = System.nanoTime();
		for(int i=0;i<1e9;i++){
			sum+=i;
		}
		long end = System.nanoTime();
		String s = "exec cost is "+(end-start)/(1e9)+" seconds";
		System.out.println(s);
	}
}
