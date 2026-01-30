---
problem: 1004. Max Consecutive Ones III
link: https://leetcode.com/problems/max-consecutive-ones-iii/description/
status: DONE
approach: Sliding Window
level: EASY
prerequisite: 
video: 
---

# Solution
```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int size = nums.length; // SIZE OF nums
        int start = 0; // start INDEX
        int maxOnes = 0; // KEEP THE COUNT OF MAX ONES INCLUDING K ZEROS
        int countZero = 0; // KEEP A COUNTER TO COUNT ZEROS IN CURRENT WINDOW


        for (int end=0; end<size; end++) {
            // COUNT THE NUMBER OF ZEROS IN CURRENT WINDOW
            if (nums[end] == 0) {
                countZero++;
            }

            // IF NUMBER OF ZEROS < K (IN THE CURRENT WINDOW) THEN 
            // UPDATE maxOnes WITH MAXIMUM OF CURRENT WINDOW-SIZE AND maxOnes (INCLUDING EQUALS TO AND LESS THEN k)
            if (countZero <= k) {
                int windowSize = end - start + 1;
                maxOnes = Math.max(maxOnes, windowSize);
            }

            // IF NO. OF ZEROS > K THEN PLACE start-INDEX TO THAT INDEX POSITION WHERE
            // NO. OF ZEROS GETS REDUCE TILL K : MEANS WE WILL REDUCE THE SIZE OF WINDOW
            while (countZero > k) {
                // WHILE REDUCING THE SIZE OF WINDOW, IF nums[start] ENCOUNTERS ZERO THEN REDUCE countZero--
                // AND start++ (SLIDE THE WINDOW / REDUCE THE WINDOW)
                if (nums[start] == 0) {
                    countZero--;
                }
                start++;
            }
        }
        return maxOnes;
    }
}
```
