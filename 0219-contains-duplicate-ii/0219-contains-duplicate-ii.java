class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, List<Integer>> indices = new HashMap<>();

        for (int ind = 0; ind < nums.length; ind++) {
            int num = nums[ind];
            List<Integer> indexList = indices.getOrDefault(num, new ArrayList<>());

            if (!indexList.isEmpty() && ind - indexList.get(indexList.size() - 1) <= k) {
                return true;
            }

            indexList.add(ind);
            indices.put(num, indexList);
        }

        return false;
    }
}