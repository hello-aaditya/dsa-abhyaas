---
problem: Peak Index in a Mountain Array
link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
status: Done
approach: Binary Search
level: EASY
---

# Solution
```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start = 0;
        int end = arr.length-1;

        int peak = -1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if ( (mid+1 != arr.length) && (arr[mid] >= arr[mid+1]) ) {
                peak = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return peak;
    }
}
```

