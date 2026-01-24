---
problem: 268. Missing Number
link: https://leetcode.com/problems/missing-number/description/
status: DONE
approach: Cyclic Sort
level: MODERATE
prerequisite: 
video: 
---

# Solution
```java
class Solution {
    public int missingNumber(int[] nums) {
        int size = nums.length;
        int start = 0;

        while (start < size) {
            int correctIndex = nums[start];

            if ((nums[start] < size) && (nums[start] != nums[correctIndex])) {
                int temp = nums[correctIndex];
                nums[correctIndex] = nums[start];
                nums[start] = temp;
            } else {
                start++;
            }
        }
        for (int i=0; i<size; i++) {
            if (i != nums[i]) {
                return i;
            }
        }
        return size;
    }
}
```
