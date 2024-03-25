class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            if (maxReach < i) {
                return false;
            } else if(maxReach >= n) {
                return true;
            }
            
            maxReach = Math.max(i + nums[i], maxReach);
        }
        return true;
    }
}