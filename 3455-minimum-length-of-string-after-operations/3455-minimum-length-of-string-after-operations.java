class Solution {
    public int minimumLength(String s) {
        Map<Character, Integer> hm = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            hm.put(s.charAt(i), hm.getOrDefault(s.charAt(i), 0) + 1);
        }
        int ans = 0;
        for(Character k : hm.keySet()) {
            if (hm.get(k) % 2 == 0) {
                ans += 2;
            } else {
                ans += 1;
            }
        }
        return ans;
    }
}