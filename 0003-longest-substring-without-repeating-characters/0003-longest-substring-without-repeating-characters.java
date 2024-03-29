
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charIndexMap = new HashMap<>();
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentCharacter = s.charAt(right);
            if (charIndexMap.containsKey(currentCharacter)) {
                left = Math.max(left, charIndexMap.get(currentCharacter) + 1);
            }
            charIndexMap.put(currentCharacter, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}
