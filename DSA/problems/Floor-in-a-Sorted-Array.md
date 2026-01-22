---
problem: Floor in a Sorted Array
link: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
status: Done
approach: BINARY SEARCH
level: EASY
---

# Solution
```java
class Solution {
    public int findFloor(int[] arr, int x) {
        // code here
        int start = 0;
        int end = arr.length-1;
        
        int floor = -1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            
            if (arr[mid] == x) {
                floor = mid;
                start = mid + 1;
            } else if (arr[mid] > x) {
                end = mid - 1;
            } else {
                floor = mid;
                start = mid + 1;
            }
        }
        return floor;
    }
}
```