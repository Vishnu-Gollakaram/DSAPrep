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