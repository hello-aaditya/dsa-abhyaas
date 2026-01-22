---
problem: Find Minimum in Rotated Sorted Array
link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
status: Done
approach: Binary Search
level: MODERATE
prerequisite:
video: https://www.youtube.com/watch?v=Jin6vO0MdzY
---

# Solution
```java
class Solution {
    public int findMin(int[] nums) {
        int size = nums.length;

        int start = 0;
        int end = size - 1;

        while (start < end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] > nums[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return nums[end];
    }
}
```


