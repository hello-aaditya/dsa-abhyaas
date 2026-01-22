---
problem: Find Smallest Letter Greater Than Target
link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
status: Done
approach: Binary Search
level: EASY
---

# Solution
```java
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int start = 0;
        int end = letters.length-1;

        char smallest = letters[0];

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (letters[mid] <= target) {
                start = mid + 1;
            }
            else {
                smallest = letters[mid];
                end = mid - 1;
            }
        }
        return smallest;
    }
}
```