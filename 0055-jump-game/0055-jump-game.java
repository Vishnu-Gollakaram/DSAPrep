class Solution {
    public boolean canJump(int[] nums) {
        int max_till_here = 0;
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            if (max_till_here < i) {
                return false;
            }
            max_till_here = Math.max(max_till_here, i + nums[i]);
        }
        if (max_till_here >= length - 1) {
            return true;
        }
        return false;
    }
}