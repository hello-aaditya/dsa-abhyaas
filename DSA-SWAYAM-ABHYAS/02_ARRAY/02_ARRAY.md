# ARRAY

| S NO. | PROBLEM                  | PLATFORM LINK                                                                            | SOLVE STATUS |
| ----- | ------------------------ | ---------------------------------------------------------------------------------------- | ------------ |
| 1.    | Maximum Subarray         | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                  | ✔️           |
| 2.    | Maximum Product Subarray | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | ✔️           |


| S NO. | PROBLEM                  | PLATFORM LINK                                                                            | CORE CONCEPT                                   | LEVEL    | SOLUTION                            |
| ----- | ------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------- | -------- | ----------------------------------- |
| 1.    | Maximum Subarray         | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                  | [Kadane's Algorithm](02.1_KADANE_ALGORITHM.md) | EASY     | [View](#1-Maximum-Subarray)         |
| 2.    | Maximum Product Subarray | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) |                                                | MODERATE | [View](#2-Maximum-Product-Subarray) |
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
# 2-Maximum-Product-Subarray
```java
class Solution {
    public int maxProduct(int[] nums) {
        int size = nums.length;
        int leftProduct = 1;
        int rightProduct = 1;

        int maxProduct = nums[0];
        int start = 0;
        int end = size-1;

        for (int i=0; i<size; i++) {
            if (leftProduct == 0) {
                leftProduct = 1;
            }

            if (rightProduct == 0) {
                rightProduct = 1;
            }

            leftProduct = leftProduct * nums[start];
            rightProduct = rightProduct * nums[end];

            maxProduct = Math.max(maxProduct, Math.max(leftProduct, rightProduct));

            start++;
            end--;
        }
        return maxProduct;
    }
}
```