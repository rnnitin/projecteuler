public class Problem33 {
	static final double PRECISION = 0.000001d;
	public static void main(String[] args) {
		for (int i = 11; i < 100; i++)
			for (int j = 11; j < 100; j++) {
				if (i == j || i % 10 == 0) continue;

				int i1 = i / 10, i2 = i % 10, j1 = j / 10, j2 = j % 10;
				if (j2 != 0 && i1 == j1 && Double.compare(((double)i2) / j2, ((double)i)/j) < PRECISION)
					System.out.println(String.format("%d / %d == %d / %d", i, j, i1, j1));
				else if (j1 != 0 && i2 == j2 && Double.compare(((double)i1) / j1, ((double)i)/j) < PRECISION)
					System.out.println(String.format("%d / %d == %d / %d", i, j, i1, j1));
				else if (j1 != 0 && i1 == j2 && Double.compare(((double)i2) / j1, ((double)i)/j) < PRECISION)
					System.out.println(String.format("%d / %d == %d / %d", i, j, i2, j1));
				else if (j2 != 0 && i2 == j1 && Double.compare(((double)i1) / j2, ((double)i)/j) < PRECISION)
					System.out.println(String.format("%d / %d == %d / %d", i, j, i1, j2));
			}
	}
}
