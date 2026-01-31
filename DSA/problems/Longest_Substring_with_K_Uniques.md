---
problem: Longest Substring with K Uniques
link: https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
status: DONE
approach: Sliding Window, Variable-Length Sliding Window
level: MODERATE
prerequisite: 
video: https://www.youtube.com/watch?v=Lav6St0W_pQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=10
---

# Solution
```java
class Solution {
    public int longestKSubstr(String s, int k) {
        // code here
        int size = s.length();
        int start = 0;
        int maxSubstring = -1;
        
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int end=0; end<size; end++) {
            char currentChar = s.charAt(end);
            
            map.put(currentChar, map.getOrDefault(currentChar, 0) + 1);
            
            while (map.size() > k) {
                char firstChar = s.charAt(start);
                map.put(firstChar, map.getOrDefault(firstChar, 0) - 1);
                
                if (map.get(firstChar) == 0) {
                    map.remove(firstChar);
                }
                start++;
            }
            
            if (map.size() == k) {
                int windowSize = end - start + 1;
                maxSubstring = Math.max(maxSubstring, windowSize);
            }
        }
        return maxSubstring;
        
    }
}
```

