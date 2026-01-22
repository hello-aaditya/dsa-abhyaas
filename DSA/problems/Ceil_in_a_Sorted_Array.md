---
problem: Ceil in a Sorted Array
link: https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1
status: Done
approach:
level:
---

# Solution
```java
class Solution {
    public int findCeil(int[] arr, int x) {
        // code here
        int start = 0;
        int end = arr.length-1;
        
        int ceil = -1;
        
        while (start <= end) {
            int mid = start + (end - start)/2;
            
            if (arr[mid] == x) {
                ceil = mid;
                end = mid - 1;
            } else if (arr[mid] > x) {
                ceil = mid;
                end = mid - 1;
            } else {
                start = mid+1;
            }
        }
        return ceil;
    }
}
```