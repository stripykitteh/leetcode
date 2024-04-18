import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
The username consists of 8 to 30 characters inclusive.
The username can only contain alphanumeric characters and underscores (_).
Alphanumeric characters describe the character set consisting of lowercase
characters [a – z], uppercase characters [A – Z], and digits [0 – 9].
The first character of the username must be an alphabetic character, i.e.,
either a lowercase character [a – z] or uppercase character [A – Z].
*/

public class ValidUsername {

    public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	int n = scan.nextInt();

	String[] userNames = new String[n];
	
	for (int i = 0; i < n; i++) {
	    userNames[i] = scan.nextLine();
	}

	for (int i = 0; i < n; i++) {
	    System.out.println(i + ":" + userNames[i]);
	    Pattern pattern = Pattern.compile("^[a-z].([a-z]|[0-9]|_){7,29}$", Pattern.CASE_INSENSITIVE);
	    Matcher matcher = pattern.matcher(userNames[i]);
	    boolean matchFound = matcher.find();
	    if(matchFound) {
		System.out.println("Valid");
	    } else {
		System.out.println("Invalid");
	    }
	}
    }
}

