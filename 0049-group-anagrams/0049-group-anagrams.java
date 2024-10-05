import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        return Arrays.stream(strs)
            .collect(Collectors.groupingBy(
                word -> {
                    char[] chars = word.toCharArray();
                    Arrays.sort(chars);
                    return new String(chars);
                }
            ))
            .values()
            .stream()
            .collect(Collectors.toList());
    }
}
