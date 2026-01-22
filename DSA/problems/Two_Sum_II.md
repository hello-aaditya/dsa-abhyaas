---
problem: Two Sum II - Input Array Is Sorted
link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
status: Done
approach: Two Pointer
level: EASY
---
# Solution
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