---
problem: Max Sum Subarray of size K
link: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
status: DONE
approach: Sliding Window
level: EASY
prerequisite: 
video: https://youtu.be/KtpqeN0Goro?list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj
---

# Solution
```java
class Solution {
    public int maxSubarraySum(int[] arr, int k) {
        // Code here
        int size = arr.length;
        int start = 0;
        int end = 0;
        int maximumSum = Integer.MIN_VALUE;
        int currentSum = 0;
        
        while (end < size) {
            currentSum += arr[end];
            
            int windowSize = end - start + 1;
            if (windowSize < k) {
                end++;
            } else if (windowSize == k) {
                maximumSum = Math.max(maximumSum, currentSum);
                
                currentSum -= arr[start];
                start++;
                end++;
            }
        }
        return maximumSum;
    }
}
```
