---
problem: 442. Find All Duplicates in an Array
link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
status: DONE
approach: Cyclic Sort
level: MODERATE
prerequisite: https://leetcode.com/problems/missing-number/
video: 
---

# Solution
```java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int size = nums.length;
        int start = 0;

        while (start < size) {
            int correctIndex = nums[start] - 1;
            if (nums[start] != nums[correctIndex]) {
                int temp = nums[correctIndex];
                nums[correctIndex] = nums[start];
                nums[start] = temp;
            } else {
                start++;
            }
        }

        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0; i<size; i++) {
            if (i+1 != nums[i]) {
                list.add(nums[i]);
            }
        }
        return list;
    }
}
```
```
