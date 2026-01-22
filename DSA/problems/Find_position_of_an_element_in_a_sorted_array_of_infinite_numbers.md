---
problem: Find position of an element in a sorted array of infinite numbers
link: https://www.geeksforgeeks.org/dsa/find-position-element-sorted-array-infinite-numbers/
status: Done
approach: BINARY SEARCH
level: MODERATE
---

# Solution
>**Note:** You are not allowed to use `.length()` function. 
You have to find the position of first occurrence of *TARGET* 

```java
package searchingProblems;


public class binarySearchWithoutUsingLengthFunction {

	public static void main(String[] args) {
		int[] arr = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 3, 4, 8, 9, 12, 15, 17, 20, 25, 27, 30, 35, 38, 42, 50, 58, 59, 61};
		int target = 1;
		
		System.out.println(targetPosition(arr, target));
		
	}
	public static int targetPosition(int[] arr, int target) {
		int start = 0;
		int end = 0;
		
		while (target > arr[end]) {
			int newStart = start + 1;
			int newEnd = end + (end - start + 1) * 2;
			
			start = newStart;
			end = newEnd;
		}
		
		return binarySearch(arr, target, start, end);
	}
	
	public static int binarySearch(int[] arr, int target, int start, int end) {
		int firstOccurrence = -1;
		while (start <= end) {
			int mid = start + (end - start) / 2;
			
			if (arr[mid] == target) {
				firstOccurrence = mid;
				end = mid - 1;
			} else if (arr[mid] > target) {
				end = mid - 1;
			} else {
				start = mid + 1;
			}
		}
		return firstOccurrence;
	}

}
```