class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int n = nums.length;
        int minSize = n;
        
        int sum = 0;
        while (right < n && sum < target) {
            sum += nums[right];
            right++;
        }
        
        if (sum < target) {
                return 0;
        } 
        else {
            while (sum - nums[left] >= target) {
                sum -= nums[left];
                left++;
            }
            minSize = Math.min(minSize, right - left);
        }

        while (right < n) {
            sum += nums[right];
            while (sum - nums[left] >= target) {
                sum -= nums[left];
                left++;
            }
            minSize = Math.min(minSize, right - left + 1);
            right++;
        }
        
        return minSize;
    }
}