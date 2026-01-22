---
problem: Find in Mountain Array
link: https://leetcode.com/problems/find-in-mountain-array/
status: Done
approach: Binary Search
level: HARD
---

# Solution
```java
/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int peak = findPeakElement(mountainArr);

        int increasingStart = 0;
        int increasingEnd = peak;

        int decreasingStart = peak + 1;
        int decreasingEnd = mountainArr.length() - 1;

        int firstPoisition =  binarySearhInIncreasingPart(mountainArr, target, increasingStart, increasingEnd);

        if (firstPoisition != -1) {
            return firstPoisition;
        }

        return binarySearhInDecreasingPart(mountainArr, target, decreasingStart, decreasingEnd);
    }
    public static int findPeakElement(MountainArray arr) {
        int start = 0;
        int end = arr.length()-1;
        int peak = -1;

        while (start < end) {
            int mid = start + (end - start) / 2;

            if (arr.get(mid) > arr.get(mid+1)) {
                end = mid;
            } else if (arr.get(mid) < arr.get(mid+1)) {
                peak = start;
                start = mid + 1;
            }
        }
        peak = start;
        return peak;
    }
    public static int binarySearhInIncreasingPart(MountainArray arr, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr.get(mid) == target) {
                return mid;
            } else if (arr.get(mid) < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
    public static int binarySearhInDecreasingPart(MountainArray arr, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (arr.get(mid) == target) {
                return mid;
            } else if (arr.get(mid) > target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
}
```
