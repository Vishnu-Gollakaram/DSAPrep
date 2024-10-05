class Solution {
    public boolean isHappy(int n) {
        Set<Integer> hset = new HashSet<Integer>();
        while (n != 1) {
            // System.out.println(n);
            if (hset.contains(n)) {
                return false;
            } else {
                hset.add(n);
                int temp = 0;
                while (n != 0) {
                    temp += Math.pow(n % 10, 2);
                    n /= 10;
                }
                n = temp;
            }
        }
        return true;
    }
}