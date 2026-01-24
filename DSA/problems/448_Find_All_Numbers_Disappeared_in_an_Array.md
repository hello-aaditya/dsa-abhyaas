---
problem: 448. Find All Numbers Disappeared in an Array
link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
status: DONE
approach: Cyclic Sort
level: MODERATE
prerequisite: https://leetcode.com/problems/missing-number/
video: https://www.youtube.com/watch?v=JfinxytTYFQ&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=20
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

