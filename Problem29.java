import java.util.HashSet;
import java.math.BigInteger;

public class Problem29 {
	public static void main(String[] args) {
		HashSet<BigInteger> powers = new HashSet<>();
		for (int a = 2; a <= 100; a++) {
			BigInteger A = new BigInteger("" + a);
			for (int b = 2; b <= 100; b++) {
				powers.add(A.pow(b));
			}
		}
		System.out.println(powers.size());
	}
}
