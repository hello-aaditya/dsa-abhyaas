---
problem: Search in Rotated Sorted Array
link: https://leetcode.com/problems/search-in-rotated-sorted-array/
status: Done
approach: Binary Search
level: HARD
prerequisite: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
video: https://www.youtube.com/watch?v=U1VsdRgVevY
---

# Solution
```java
class Solution {
    public int search(int[] nums, int target) {
        int size = nums.length;

        int pivot = minimumInRotatedSorted(nums);
        
        int start = 0;
        int end = pivot-1;

        int findKey = binarySearch(nums, target, start, end);

        if (findKey != -1) {
            return findKey;
        } else {
            start = pivot;
            end = size-1;
            return binarySearch(nums, target, start, end);
        }

    }
    public static int minimumInRotatedSorted(int[] arr) {

        int size = arr.length;
        int start = 0;
        int end = size - 1;

        while (start < end) {
            int mid = start + (end - start) / 2;

            if (arr[mid] > arr[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return end;
    }
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }
}
```


