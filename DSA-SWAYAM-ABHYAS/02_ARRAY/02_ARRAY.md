# ARRAY

| S NO. | PROBLEM                            | PLATFORM LINK                                                                                              | SOLVE STATUS |
| ----- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------ |
| 1.    | Find Peak Element                  | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                 |              |
| 2.    | Binary Search                      | [704. Binary Search](https://leetcode.com/problems/binary-search/)                                         |              |
| 3.    | Sort an Array                      | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)                                         |              |
| 4.    | Two Sum II - Input Array Is Sorted | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | ✔️           |
| 5.    | Happy Number<br>                   | [202. Happy Number](https://leetcode.com/problems/happy-number/)<br>                                       | ✔️           |


| S NO. | PROBLEM                            | PLATFORM LINK                                                                                              | CORE CONCEPT | LEVEL | SOLUTION                |
| ----- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------ | ----- | ----------------------- |
| 1.    | Find Peak Element                  | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                 |              |       |                         |
| 2.    | Binary Search                      | [704. Binary Search](https://leetcode.com/problems/binary-search/)                                         |              |       |                         |
| 3.    | Sort an Array                      | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)                                         |              |       |                         |
| 4.    | Two Sum II - Input Array Is Sorted | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointer  | EASY  | [View](#4-Two-Sum-II)   |
| 5.    | Happy Number                       | [202. Happy Number](https://leetcode.com/problems/happy-number/)                                           |              | EASY  | [View](#5-Happy-Number) |
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
