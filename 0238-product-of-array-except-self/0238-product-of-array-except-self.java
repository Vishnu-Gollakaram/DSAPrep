/*
// My idea
class Solution {
    private int getProduct(int[] nums) {
        return Arrays.stream(nums)
            .filter(i -> i != 0)
            .reduce(1, (a, b) -> a * b);
    }
    
    public int[] productExceptSelf(int[] nums) {
        Map<Integer, Long> elementCount = Arrays.stream(nums)
            .boxed()
            .collect(Collectors
                     .groupingBy(Function.identity(),
                                 Collectors.counting()));

        if (elementCount.getOrDefault(0, 0L) > 1) {
            return Arrays.stream(nums)
                .map(i -> 0)
                .toArray();
        } else if (elementCount.getOrDefault(0, 0L) == 1) {
            int prod = getProduct(nums);
            return Arrays.stream(nums)
                .map(i -> i == 0 ? prod : 0)
                .toArray();
        } else {
            int prod = getProduct(nums);
            return Arrays.stream(nums)
                .map(i -> prod/i)
                .toArray();
        } 
    }
}
*/
// Optimization

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int zeroCount = 0;
        int totalProduct = 1;

        for (int num : nums) {
            if (num == 0) {
                zeroCount++;
            } else {
                totalProduct *= num;
            }
        }

        int[] result = new int[nums.length];

        if (zeroCount > 1) {
            Arrays.fill(result, 0);
        } else if (zeroCount == 1) {
            Arrays.fill(result, 0);
            int zeroIndex = Arrays.stream(nums).boxed().collect(Collectors.toList()).indexOf(0);
            result[zeroIndex] = totalProduct;
        } else {
            for (int i = 0; i < nums.length; i++) {
                result[i] = totalProduct / nums[i];
            }
        }

        return result;
    }
}
