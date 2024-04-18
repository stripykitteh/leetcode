import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class MyCalculator {
    
    public long power(int n, int p) throws Exception {

	System.err.println(n + " " + p);
	
	if (n < 0 || p < 0) {
	    throw new Exception("n and p should be non-negative.");
	}
	if (n == 0 && p == 0) {
	    throw new Exception("n and p should not be zero.");
	}
	return (long) Math.pow(n,p);
    }
}

class Main {
    public static void main(String[] args) {
	MyCalculator c = new MyCalculator();
	Scanner scan = new Scanner(System.in);
	String input = new String();
	
	do {
	    input = scan.nextLine();
	    Pattern pattern = Pattern.compile("(-?[0-9]+)\\s+(-?[0-9]+)");
	    Matcher matcher = pattern.matcher(input);
	    boolean matchFound = matcher.find();
	    if(matchFound) {
		try {
		    System.out.println(c.power(Integer.parseInt(matcher.group(1)),
					       Integer.parseInt(matcher.group(2))));
		} catch (Exception e) {
		    System.err.println(e.getMessage());
		}
		    
	    }
	} while (input != "q");
    }
}
