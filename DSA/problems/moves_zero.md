---
problem: moves zero
link: https://leetcode.com/problems/move-zeroes/post-solution/?submissionId=1910915302
status: DONE
approach: Linked List, kadan's algorithm
level: MODERATE
prerequisite: 
video: 
---

# Solution
```java
class Solution {
    public void moveZeroes(int[] nums) {
        int size = nums.length;
        int start = 0;
        int end = 0;

        while (end < size) {
            if (nums[end] != 0) {
                int temp = nums[end];
                nums[end] = nums[start];
                nums[start] = temp;
                start++;
            }
            end++;
        }

        for (int i=start; i<size; i++) {
            nums[start] = 0;
        }
    }
}
```

