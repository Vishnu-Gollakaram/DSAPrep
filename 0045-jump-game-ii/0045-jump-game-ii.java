class Solution {
    public int jump(int[] nums) {
        int jumps = 0;
        int max_reached = 0;
        int max_greedy_index = 0;
        for(int i = 0; i < nums.length - 1; i++) {
            max_reached = Math.max(max_reached, i + nums[i]);
            if (i == max_greedy_index) {
                jumps += 1;
                max_greedy_index = max_reached;
            }
        }
        return jumps;
    }
}