import java.io.FileReader;
import java.io.BufferedReader;
import java.lang.Exception;
import java.util.Arrays; 

public class Problem22 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new FileReader("p022_names.txt"));
		String  line = null;
		String names = "";
		while ((line = br.readLine()) != null) {
			names += line.replaceAll("\"", "").toUpperCase();
		}
		String[] namesArr = names.split(",");
		Arrays.sort(namesArr);
		int sum = 0;
		for (int idx = 0; idx < namesArr.length; idx++) {
			int nameSum = 0;
			char[] charArr = namesArr[idx].toCharArray();
			for (char c : charArr) {
				nameSum += c - 'A' + 1;
			}
			int score = nameSum * (1 + idx);
			sum += score;
		}
		System.out.println("sum total of scores = " + sum);
	}
}
