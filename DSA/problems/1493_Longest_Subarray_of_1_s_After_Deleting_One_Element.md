---
problem: 1493. Longest Subarray of 1's After Deleting One Element
link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
status: DONE
approach: Sliding Window
level: EASY
prerequisite:
video:
---

# Solution
```java
class Solution {
    public int longestSubarray(int[] nums) {
        int size = nums.length; // SIZE OF nums
        int start = 0;
        int end = 0;

        int zeroCount = 0;      // KEEPS THE COUNT OF ZERO IN CURRENT WINDOW
        int maxOne = 0;         // STORE THE MAXIMUM ONE IN THE GIVEN ARRAY-> nums

        while (end < size) {
            // ---------------- EXPAND ---------------- 
            // INCLUDE nums[end] INTO THE WINDOW
            if (nums[end] == 0) {
                zeroCount++;
            }

            // ---------------- SHRINK ---------------- 
            // IF MORE THAN ONE ZERO EXISTS -> CONDITION VIOLATED -> WINDOW BECOMES INVALID
            while (zeroCount > 1) {

                // REMOVE nums[start] FROM WINDOW
                if (nums[start] == 0) {
                    zeroCount--;
                }
                start++; // MOVE STARTING POINTER
            }

            // ---------------- UPDATE ANSWER ---------------- 
            // NOTE: WE MUST DELETE ONE ELEMENT, SO windowSize = end - start ->
            int windowSize = end - start;
            maxOne = Math.max(maxOne, windowSize); // UPDATE maxOne AFTER DELETING ONE INDEX
            // MOVE ENDING POINTER
            end++;
        }
        return maxOne;
    }
}
```

