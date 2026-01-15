# ARRAY


| S NO. | PROBLEM                             | PLATFORM LINK                                                                                              | SOLVE STATUS |
| ----- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------ |
| 1.    | Maximum Subarray                    | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                    | ✔️           |
| 2.    | Maximum Product Subarray            | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)                   | ✔️           |
| 5.    | Best Time to Buy and Sell Stock<br> | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)     | ✔️           |
| 3.    | Two Sum II - Input Array Is Sorted  | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | ✔️           |
| 4.    | Happy Number<br>                    | [202. Happy Number](https://leetcode.com/problems/happy-number/)<br>                                       | ✔️           |


| S NO. | PROBLEM                             | PLATFORM LINK                                                                                              | CORE CONCEPT                                   | LEVEL    | SOLUTION                                   |
| ----- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------- | ------------------------------------------ |
| 1.    | Maximum Subarray                    | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                    | [Kadane's Algorithm](00.1_KADANE_ALGORITHM.md) | EASY     | [View](#1-Maximum-Subarray)                |
| 2.    | Maximum Product Subarray            | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)                   | [Kadane's Algorithm](00.1_KADANE_ALGORITHM.md) | MODERATE | [View](#2-Maximum-Product-Subarray)        |
| 3.    | Best Time to Buy and Sell Stock<br> | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)     | [Kadane's Algorithm](00.1_KADANE_ALGORITHM.md) | MODERATE | [View](#3-Best-Time-to-Buy-and-Sell-Stock) |
| 4.    | Two Sum II - Input Array Is Sorted  | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointer                                    | EASY     | [View](#4-Two-Sum-II)                      |
| 5.    | Happy Number                        | [202. Happy Number](https://leetcode.com/problems/happy-number/)                                           |                                                | EASY     | [View](#5-Happy-Number)                    |
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
# 3-Best-Time-to-Buy-and-Sell-Stock
```java
class Solution {
    public int maxProfit(int[] prices) {
        // KADANE'S ALGORITHM
        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i=0; i<prices.length; i++) {
            int currentProfit = prices[i] - minPrice;
            maxProfit = Math.max(currentProfit, maxProfit);
            minPrice = Math.min(minPrice, prices[i]);
        }

        return maxProfit;
    }
}
```
# 4-Two-Sum-II
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length-1;

        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum == target) {
                return new int[]{start+1, end+1};
            } else if (sum > target) {
                end--;
            } else {
                start++;
            }
        }
        return new int[]{-1, -1};
    }
}
```
# 5-Happy-Number
```java
class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<>();

        while (true) {
            int sum = 0;
            while (n!=0) {
                int lastDigit = n % 10;
                sum += (lastDigit * lastDigit);
                n /= 10;
            }

            if (sum == 1) {
                return true;
            }
            
            if (set.contains(sum)) {
                return false;
            } else if (!set.contains(sum)) {
                set.add(sum);
            }
            n = sum;
        }
    }
}
```
