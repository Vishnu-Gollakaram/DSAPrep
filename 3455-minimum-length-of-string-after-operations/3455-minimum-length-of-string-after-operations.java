class Solution {
    public int minimumLength(String s) {
        Map<Character, Integer> hm = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            Character ch = s.charAt(i);
            int val = hm.getOrDefault(ch, 0);
            hm.put(ch, val + 1);
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