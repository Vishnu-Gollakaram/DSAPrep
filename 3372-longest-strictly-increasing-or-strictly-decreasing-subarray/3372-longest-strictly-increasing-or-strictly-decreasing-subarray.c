int longestMonotonicSubarray(int* nums, int numsSize) {
    int ans = 0;
    int dec = 0;
    int inc = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 0;
        }
        else if (nums[i] == nums[i - 1]) {
            dec = 0;
            inc = 0;
        }
        else {
            dec++;
            inc = 0;
        }
        if (inc > ans) {
            ans = inc;
        }

        if (dec > ans) {
            ans = dec;
        }
    }

    return ans + 1;
}
