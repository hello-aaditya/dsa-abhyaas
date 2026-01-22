---
problem: 283. Move Zeroes
link: https://leetcode.com/problems/move-zeroes/description/
status: DONE
approach: Two Pointer
level: EASY
prerequisite:
video: https://www.youtube.com/watch?v=k5lIW5XxC7g
---

# Solution
```java
class Solution {
    public void moveZeroes(int[] nums) {
        int size = nums.length;

        int insertionPosition = 0;
        // FILL NON-ZERO ELEMENTS TO FRONTEND SIDE OF THE ARRAY (nums)
        for (int i=0; i<size; i++) {
            if (nums[i] != 0) {
                nums[insertionPosition] = nums[i];
                insertionPosition++;
            }
        }
        // NOW FILL THE ZEROS TO THE END SIDE
        while (insertionPosition < size) {
            nums[insertionPosition] = 0;
            insertionPosition++;
        }
    }
}
```

