---
problem: 724. Find Pivot Index
link: https://leetcode.com/problems/find-pivot-index/description/
status: DONE
approach: Prefix Sum
level: MODERATE
prerequisite: 
video: https://www.youtube.com/watch?v=Q0Qat25D6JE
---

# Solution
```java
class Solution {
    public int pivotIndex(int[] nums) {
        int size = nums.length;
        int totalSum = 0;

        for (int x : nums) {
            totalSum += x;
        }

        int cumulativeSum = 0;
        for (int i=0; i<size; i++) {
            int leftSum = cumulativeSum;
            int rightSum = totalSum - leftSum - nums[i];

            if (leftSum == rightSum) {
                return i;
            }
            cumulativeSum += nums[i];
        }
        return -1;
    }
}
```
