class Solution {
    public int maxSubArray(int[] nums) {
        int[] maxSum = {0, -10001};
        IntStream.range(0, nums.length).forEach(i -> {
            maxSum[0] = maxSum[0] + nums[i];
            maxSum[1] = Math.max(maxSum[0], maxSum[1]);
            maxSum[0] = Math.max(maxSum[0], 0);
        });
        return maxSum[1];
    }
}