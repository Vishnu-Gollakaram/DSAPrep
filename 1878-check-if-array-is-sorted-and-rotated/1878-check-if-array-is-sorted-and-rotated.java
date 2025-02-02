class Solution {
    public boolean check(int[] nums) {
        /*
            We need to <=1 break as we are searching for rotated sorted array
            Breaks stores count of number of unsorted parts (LEFT ELEMENT > RIGHT)
            For a roated array, at max there is only one unsorted part, hence false
            if array is not roated, it's true
            If array is rotated, there are 2 parts, left and right
            left part should always be greater than right (min_pre >= max_post)
            Hence, 3 conditions:
            1) If more than 1 break, return false
            2) If no breaks, return true
            3) If 1 break, check left side minimum (0th element) is greater than or equal to right side maxima (n - 1 th element)
        */
        int breaks = 0;
        int length_of_nums = nums.length;
        int min_pre = nums[0];
        int max_post = nums[length_of_nums - 1];

        for(int index = 1; index < length_of_nums; index++) {
            if (nums[index] < nums[index - 1]) {
                breaks += 1;
                if (breaks > 1) {
                    return false;
                }
            }
        }
        if (breaks == 0) {
            return true;
        }
        return max_post <= min_pre;
    }
}