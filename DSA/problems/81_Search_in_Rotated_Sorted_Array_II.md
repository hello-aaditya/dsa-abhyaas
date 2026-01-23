---
problem: 81. Search in Rotated Sorted Array II
link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
status: DONE
approach: Binary Search
level: MODERATE
prerequisite: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
video: https://www.youtube.com/watch?v=eneo_XPUEj0
---

# Solution
```java
class Solution {
    public boolean search(int[] nums, int target) {
        int size = nums.length;

        int pivot = findPivot(nums);
        
        int start = 0;
        int end = pivot-1;

        // SEARCH ON LEFT SIDE OF SORTED ARRAY (nums) BEFORE PIVOT
        if (binarySearch(nums, target, start, end)) {
            return true;
        }
        // SEARCH ON RIGHT SIDE (INCLUDING PIVOT) OF THE SORTED ARRAY (nums) AFTER PIVOT
        start = pivot;
        end = size - 1;
        return binarySearch(nums, target, start, end);
    }
    // FIND PIVOT
    public static int findPivot (int[] nums) {
        int size = nums.length;
        int start = 0;
        int end = size - 1;

        while (start < end) {

            // MOVE START TO 1 PLACE AHEAD TILL nums[start] == nums[start+1]
            while ((start < end) && (nums[start] == nums[start+1])) {
                start++;
            }
            // MOVE END TO 1 PLACE BEFORE TILL nums[end] == nums[end-1]
            while ((start < end) && (nums[end] == nums[end-1])) {
                end--;
            }

            // CODE FOR FIND MINIMUM IN ROTATED SORTED ARRAY
            int mid = start + (end - start) / 2;

            if (nums[mid] > nums[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return end;
    }
    // BINARY SEARCH
    public static boolean binarySearch(int[] nums, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start) / 2;
            
            if (nums[mid] == target) {
                return true;
            } if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }
}
```

