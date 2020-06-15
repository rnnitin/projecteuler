import java.util.Date;

public class Problem19 {
	public static void main(String[] args) {
		int countSundays = 0;
		for (int y = 1; y <= 100; y++)
			for (int m = 0; m < 12; m++) {
				Date d = new Date(y, m, 1, 0, 0);
				if (0 == d.getDay()) {
					System.out.println (" >> " + d);
					countSundays++;
				} else {
					System.out.println (d);
				}
			}
		System.out.println("\n\n\t countSundays = " + countSundays);
		}
	} 
