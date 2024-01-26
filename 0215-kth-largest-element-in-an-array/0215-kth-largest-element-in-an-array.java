import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Intuition -> Sort based
        // Arrays.sort(nums);
        // return nums[nums.length - k];

        // Heap solution
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int i = 0; i < k; i++) {
            minHeap.offer(nums[i]);
        }

        for (int i = k; i < nums.length; i++) {
            minHeap.offer(nums[i]);
            minHeap.poll();
        }

        return minHeap.peek();
    }
}
