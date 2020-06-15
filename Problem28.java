public class Problem28 {
	static final int BASE_MAT_DIM = 5;
	static final int BASE_MAT_SUM = 101;
	static final int BASE_MAT_MAX_DIFF = 4;
	static final int BASE_MAT_MAX = 25;
	static final int QDIM = 1001;
	public static void main(String[] args) {
		int matDim = QDIM, sum = BASE_MAT_SUM, diff = BASE_MAT_MAX_DIFF + 2, currMax = BASE_MAT_MAX;
		for (int currDim = BASE_MAT_DIM + 2; currDim <= matDim; currDim += 2) {
			sum += currMax * 4 + diff * 10;
			diff += 2;
			currMax = currDim * currDim; 
		}
		System.out.println(sum);
	}
}
