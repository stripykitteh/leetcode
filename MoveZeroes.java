class Solution {
    public void moveZeroes(int[] nums) {
	if (nums == null || nums.length == 0) {
	    return;
	}

	int actualP = 0;
	int scanP = 0;

	while (scanP < nums.length) {
	    
	    if (nums[scanP] != 0) {
		nums[actualP++] = nums[scanP++];
	    } else {
		scanP++;
	    }

	}

	while (actualP < nums.length) {
	    nums[actualP++] = 0;
	}
    }
}


