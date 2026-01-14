
| S NO. | PROBLEM          | PLATFORM LINK                                                           | SOLVE STATUS |
| ----- | ---------------- | ----------------------------------------------------------------------- | ------------ |
| 1.    | Maximum Subarray | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |              |


| S NO. | PROBLEM          | PLATFORM LINK                                                           | CORE CONCEPT       | LEVEL | SOLUTION                         |
| ----- | ---------------- | ----------------------------------------------------------------------- | ------------------ | ----- | -------------------------------- |
| 1.    | Maximum Subarray | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane's Algorithm | EASY  | !(Solution)[#1-Maximum-Subarray] |
# 1-Maximum-Subarray
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = 0;

        for (int i=0; i<nums.length; i++) {
            // STEP-1
            currentSum += nums[i];

            // STEP-2
            maxSum = Math.max(currentSum, maxSum);

            // STEP-3
            if (currentSum < 0) {
                currentSum = 0;
            }
        }
        return maxSum;
    }
}
```