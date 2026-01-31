---
problem: 3. Longest Substring Without Repeating Characters
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
status: DONE
approach: Sliding Window, Variable-Length Sliding Window
level: MODERATE
prerequisite:
video:
---

# Solution
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int size = s.length(); // SIZE OF THE STRING s
        int start = 0;
        int maxLength = 0; // TO STORE MAXIMUM-LENGTH OF LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

        // HASMAP TO STORE THE EVERY CHARACTERS AND ITS CURRENT POSITION
        HashMap<Character, Integer> map = new HashMap<>();

        for (int end =0; end<size; end++) {
            char currentChar = s.charAt(end); // CURRENT CHARACTER

            // IF currentChar FOUND INSIDE MAP THEN UPDATE start TO ITS CURRENT OCCURRENCE POSITION
            if(map.containsKey(currentChar)) {
                start = Math.max(start, map.get(currentChar) + 1);
            }

            // INSERT currentChar ALONG WITH ITS POSITION TO THE MAP
            map.put(currentChar, end);

            int windowSize = end - start + 1; 
            maxLength = Math.max(maxLength, windowSize);
        }
        return maxLength;
    }
}
```

