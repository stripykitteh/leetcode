import java.util.*;

public class IsPalindrome {

    public static void main(String[] args) throws Exception {
	Scanner scan = new Scanner(System.in);
	String s = scan.nextLine();

	int s_len = s.length();

	String pal = "Yes";
	
	for (int i = 0; i < s_len/2; i++){
	    char c = s.charAt(i);
	    char d = s.charAt(s_len - i - 1);
	    if (c != d) {
		pal = "No";
	    }
	}

	System.out.println(pal);
	
    }
}
