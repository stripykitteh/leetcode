class Loops_1 {
    public void printMultiples(int N) {

	int loop_len = 10;

	for (int i = 1; i <= loop_len; i++) {
	    System.out.println(N + " x " + i + " = " + N*i);
	}	    	
	return;
    }
}

class Main {
    public static void main(String[] args) {
	Loops_1 l = new Loops_1();
	int N = 5;
	l.printMultiples(N);
	N = 17;
	l.printMultiples(N);
    }
}
