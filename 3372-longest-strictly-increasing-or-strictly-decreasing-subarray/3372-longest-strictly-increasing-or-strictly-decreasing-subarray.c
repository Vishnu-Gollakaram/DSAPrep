int longestMonotonicSubarray(int* nums, int numsSize) {
    // Intialise all Sequences to 0
    int maximum_sequence = 0;
    int decreasing_sequence = 0;
    int increasing_sequence = 0;

    // Count for both increasing and decreasing sequences
    // If increasing value found increment increasing_sequence
    // If decreasing value found increment decreasing_sequence
    // Set the other variable to 0 in other cases
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i - 1]) {
            increasing_sequence++;
            decreasing_sequence = 0;
        }
        else if (nums[i] == nums[i - 1]) {
            decreasing_sequence = 0;
            increasing_sequence = 0;
        }
        else {
            decreasing_sequence++;
            increasing_sequence = 0;
        }
        if (increasing_sequence > maximum_sequence) {
            maximum_sequence = increasing_sequence;
        }

        // In each Iteration, trace maximum value via check
        if (decreasing_sequence > maximum_sequence) {
            maximum_sequence = decreasing_sequence;
        }
    }

    // We need to return sequence length not sequnce hence always +1 added.
    return maximum_sequence + 1;
}
