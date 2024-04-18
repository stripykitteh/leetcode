import java.util.*;

public class Solution {

    public static int min_size = 0;
    
    public static void main(String[] args){
	Scanner scan = new Scanner(System.in);
	int b = scan.nextInt();
	int h = scan.nextInt();	

	if (b <= min_size && h <= min_size) {
	    throw new Exception("Breadth and height must be positive");
	} else {
	    System.out.println(b*h);
	}
    }
}



