# ARRAY

| S NO. | PROBLEM                                                           | PLATFORM LINK                                                                                                                                               | SOLVE STATUS |
| ----- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 1.    | Find Peak Element                                                 | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                                                                  |              |
| 2.    | Binary Search                                                     | [704. Binary Search](https://leetcode.com/problems/binary-search/)                                                                                          |              |
| 3.    | Sort an Array                                                     | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)                                                                                          |              |
| 4.    | Two Sum II - Input Array Is Sorted                                | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)                                                  | ✔️           |
| 5.    | Happy Number<br>                                                  | [202. Happy Number](https://leetcode.com/problems/happy-number/)<br>                                                                                        | ✔️           |
| 6.    | Ceil in a Sorted Array                                            | [Ceil in a Sorted Array](https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1)                                                                   | ✔️           |
| 7.    | Floor in a Sorted Array                                           | [Floor in a Sorted Array](https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1)                                                      | ✔️           |
| 8.    | Find Smallest Letter Greater Than Target                          | [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)                                    | ✔️           |
| 9.    | Find First and Last Position of Element in Sorted Array           | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)       | ✔️           |
| 10    | Find position of an element in a sorted array of infinite numbers | [Find position of an element in a sorted array of infinite numbers](https://www.geeksforgeeks.org/dsa/find-position-element-sorted-array-infinite-numbers/) | ✔️           |
| 11.   | Peak Index in a Mountain Array                                    | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)                                                             |              |


| S NO. | PROBLEM                                                           | PLATFORM LINK                                                                                                                                               | CORE CONCEPT  | LEVEL    | SOLUTION                                                           |
| ----- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------- | ------------------------------------------------------------------ |
| 1.    | Find Peak Element                                                 | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                                                                  |               |          |                                                                    |
| 2.    | Binary Search                                                     | [704. Binary Search](https://leetcode.com/problems/binary-search/)                                                                                          |               |          |                                                                    |
| 3.    | Sort an Array                                                     | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)                                                                                          |               |          |                                                                    |
| 4.    | Two Sum II - Input Array Is Sorted                                | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)                                                  | Two Pointer   | EASY     | [View](#4-Two-Sum-II)                                              |
| 5.    | Happy Number                                                      | [202. Happy Number](https://leetcode.com/problems/happy-number/)                                                                                            |               | EASY     | [View](#5-Happy-Number)                                            |
| 6.    | Ceil in a Sorted Array                                            | [Ceil in a Sorted Array](https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1)                                                                   | BINARY SEARCH | EASY     | [View](#6-Ceil-in-a-Sorted-Array)                                  |
| 7.    | Floor in a Sorted Array                                           | [Floor in a Sorted Array](https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1)                                                      | BINARY SEARCH | EASY     | [View](#7-Floor-in-a-Sorted-Array)                                 |
| 8.    | Find Smallest Letter Greater Than Target                          | [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)                                    | BINARY SEARCH | EASY     | [View](#8-Find-Smallest-Letter-Greater-Than-Target)                |
| 9.    | Find First and Last Position of Element in Sorted Array           | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)       | BINARY SEARCH | MODERATE | [View](#9-Find-First-and-Last-Position-of-Element-in-Sorted-Array) |
| 10.   | Find position of an element in a sorted array of infinite numbers | [Find position of an element in a sorted array of infinite numbers](https://www.geeksforgeeks.org/dsa/find-position-element-sorted-array-infinite-numbers/) | BINARY SEARCH | MODERATE | [View](#9-Find-First-and-Last-Position-of-Element-in-Sorted-Array) |
| 11.   | Peak Index in a Mountain Array                                    | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)                                                             |               |          |                                                                    |
# 4-Two-Sum-II
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length-1;

        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum == target) {
                return new int[]{start+1, end+1};
            } else if (sum > target) {
                end--;
            } else {
                start++;
            }
        }
        return new int[]{-1, -1};
    }
}
```
# 5-Happy-Number
```java
class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<>();

        while (true) {
            int sum = 0;
            while (n!=0) {
                int lastDigit = n % 10;
                sum += (lastDigit * lastDigit);
                n /= 10;
            }

            if (sum == 1) {
                return true;
            }
            
            if (set.contains(sum)) {
                return false;
            } else if (!set.contains(sum)) {
                set.add(sum);
            }
            n = sum;
        }
    }
}
```
# 6-Ceil-in-a-Sorted-Array
```java
// User function Template for Java
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
# 7-Floor-in-a-Sorted-Array
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
# 8-Find-Smallest-Letter-Greater-Than-Target
```java
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int start = 0;
        int end = letters.length-1;

        char smallest = letters[0];

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (letters[mid] <= target) {
                start = mid + 1;
            }
            else {
                smallest = letters[mid];
                end = mid - 1;
            }
        }
        return smallest;
    }
}
```
# 9-Find-First-and-Last-Position-of-Element-in-Sorted-Array
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
# 10-Find-position-of-an-element-in-a-sorted-array-of-infinite-numbers
> **Note:** You are not allowed to use `.length()` function. 
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
# 11-Peak-Index in a Mountain Array