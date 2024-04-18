import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class MyRegex {
    
    public boolean isRegex(String ip_address) {

	Pattern pattern = Pattern.compile("^([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3})$");
	Matcher matcher = pattern.matcher(ip_address);
	boolean matchFound = matcher.find();

	if (matchFound) {
	    int octet_len = 4;
	    int octet;
	    for (int i = 1; i <= octet_len; i++) {
		octet = Integer.parseInt(matcher.group(i));
		if (octet > 256) {
		    return false;
		}
	    }
	} else {
	    return false;
	}
	return true;
    }
}

class Main {
    public static void main(String[] args) {
	MyRegex r = new MyRegex();
	Scanner scan = new Scanner(System.in);
	String input = new String();
	
	do {
	    input = scan.nextLine();
	    System.out.println(r.isRegex(input));
	} while (input != "quit");
    }
}
