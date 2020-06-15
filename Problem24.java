import java.util.ArrayList;
import java.util.Arrays;

public class Problem24 {
	public static void main(String[] args) {
		int[] factArr = new int[9];
		factArr[0] = 1;
		for (int i = 1; i < 9; i++) {
			factArr[i] = factArr[i-1] * (i+1);
			System.out.println(String.format("factArr[%d] = %d", i, factArr[i]));
		}
		System.out.println();

		ArrayList<Integer> digits = new ArrayList(Arrays.asList(new Integer[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}));
		int perm = 999999, idx = 8;
		String permStr = "";
		while (perm > 0) {
			int d = perm / factArr[idx];
			Integer[] dArray =  digits.toArray(new Integer[digits.size()]);
			System.out.println(perm + " > " + factArr[idx] + " * " + d + " -> [" + Arrays.toString(dArray) + "]");
			permStr += "" + digits.get(d);
			digits.remove(d);
			perm -= d * factArr[idx];
			idx--;
		}
		System.out.println();
		System.out.println(permStr);
		System.out.println();
	}
}
			
