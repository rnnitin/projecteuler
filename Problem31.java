public class Problem31 {
	static int[] DENOMS = {200,100,50,20,10,5,2,1};
	public static void main(String[] args) {
		System.out.println(countPerms(Integer.parseInt(args[0]),0,0,""));
	}
	
	private static int countPerms(int val, int idx, int ways, String waysStr) {
		// System.out.println(String.format("countPerms(%d, %d, %d) => DENOMS[idx] = %d", val, idx, ways, DENOMS[idx]));
		if (val == 0) {
			System.out.println("val == 0 => waysStr=("+waysStr+")");
			return ways + 1;
		}
		if (val < DENOMS[idx]) {
			//System.out.println("val < DENOMS[idx]");
			return countPerms(val, 1+idx, ways, waysStr);
		}	
		//System.out.println("last return");
		int sumWays = ways;
		for (; idx < DENOMS.length; idx++) {
			sumWays += countPerms(val - DENOMS[idx], idx, ways, waysStr + DENOMS[idx]);
		}
		return sumWays;
		// return (1+idx < DENOMS.length ? countPerms(val - DENOMS[1+idx], 1+idx, ways, waysStr + DENOMS[1+idx]) : 0)
		//	+ countPerms(val - DENOMS[idx], idx, ways, waysStr + DENOMS[idx]);
	}
}
