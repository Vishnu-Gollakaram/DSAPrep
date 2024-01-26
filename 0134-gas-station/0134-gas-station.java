class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] result = {0, 0, 0, 0};
        IntStream.range(0, gas.length).forEach(i -> {
            result[0] += gas[i];
            result[1] += cost[i];
            if(result[2] + gas[i] - cost[i] < 0) {
                result[2] = 0;
                result[3] = i + 1;
            } else {
            result[2] = result[2] + gas[i] - cost[i];
            }
        });

        return result[0] >= result[1] ? result[3] : -1;
    }
}