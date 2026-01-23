---
problem: Find Kth Rotation
link: https://www.geeksforgeeks.org/problems/rotation4723/1
status: DONE
approach: Binary Search
level: EASY
prerequisite: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
video: 
---

# Solution
```java
class Solution {
    public int findKRotation(int arr[]) {
        // Code here
        int size = arr.length;
        
        // IF ARRAY IS ALREADY SORTED
        if (arr[0] < arr[size-1]) {
            return 0;
        }
        
        // IF ARRAY IS NOT SORTED
        int pivot = findPivot(arr);
        return pivot;
    }
    public static int findPivot(int[] arr) {
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
}
```
