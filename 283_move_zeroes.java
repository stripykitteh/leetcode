import java.util.Arrays;

class Solution {
    public int[] moveZeroes(int[] nums) {
	
	if (nums == null || nums.length == 0) {
	    return nums;
	}

	int actualP = 0;
	int scanP = 0;

	while (scanP < nums.length) {
	    
	    if (nums[scanP] != 0) {
		nums[actualP++] = nums[scanP++];
	    } else {
		scanP++;
	    }

	    System.out.println(Arrays.toString(nums));
	}

	while (actualP < nums.length) {
	    nums[actualP++] = 0;
	}
	
	return nums;
    }

}

class Main {
    public static void main(String[] args) {
	Solution sol = new Solution();
	int[] nums_0 = { 0,1,0,3,12 };
	System.out.println(Arrays.toString(sol.moveZeroes(nums_0)));
	int[] nums_1 = { 0 };
	System.out.println(Arrays.toString(sol.moveZeroes(nums_1)));
    }
}


