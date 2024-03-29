class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        int len = s.length();
        int left = 0;
        int right = 0;
        int maxLength = 0;
        
        while (right < len) {
            char currentCharacter = s.charAt(right);
            if (charSet.contains(currentCharacter)) {
                while (left <= right) {
                    char tempCharacter = s.charAt(left);
                    left++;
                    if (currentCharacter == tempCharacter) {
                        break;
                    } else {
                        charSet.remove(tempCharacter);
                    }
                }
            } else {
                charSet.add(currentCharacter);
            }
            right++;
            maxLength = Math.max(maxLength, right - left);
        }
        return maxLength;
    }
}