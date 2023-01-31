public class Distance{
	private java.awt.Point point0,point1;
	public Distance(int x0,int y0,int x1,int y1){
		point0 = new java.awt.Point(x0,y0);
		point1 = new java.awt.Point(x1,y1);
	}
	public void printDistance(){
		System.out.println("Distance between "+point0+" and "+point1
		   +" is "+point0.distance(point1));
	}
	public static void main(String[] args){
		Distance dist = new Distance(intValue(args[0]),intValue(args[1]),
		             intValue(args[2]),intValue(args[3]));
		dist.printDistance();
	}
	private static int intValue(String data){
		return Integer.parseInt(data);
	}
}
