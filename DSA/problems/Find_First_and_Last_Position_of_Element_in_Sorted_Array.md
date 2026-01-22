---
problem: Find First and Last Position of Element in Sorted Array
link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
status: Done
approach: Binary Search
level: MODERATE
---
# Solution
```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] find = {-1, -1};

        // RUN BINARY SEARCH TWO TIMES:
            // FIRST TO FIND THE nums[mid] == target -> IN SEARCH OF VERY FIRST OCCURRENEC OF TARGET
            int firstPosition = firstBinarySearch(nums, target);
            if (firstPosition == -1) {
                return find;
            }

            find[0] = firstPosition;
            // SECOND FIND THE nums[mid] == target -> IN SEARCH OF VERY LAST OCCURRENEC OF TARGET
            int secondPosition = secondBinarySearch(nums, target);
            find[1] = secondPosition;
            return find;
    }
    static int firstBinarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length-1;

        int firstPosition = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr[mid] == target) {
                firstPosition = mid;
                end = mid - 1;
            } else if (arr[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return firstPosition;
    }
    static int secondBinarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length-1;

        int lastPosition = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr[mid] == target) {
                lastPosition = mid;
                start = mid + 1;
            } else if (arr[mid] < target)  {
                start = mid + 1;
            } else if (arr[mid] > target) {
                end = mid - 1;
            }
        }
        return lastPosition;
    }
}
```