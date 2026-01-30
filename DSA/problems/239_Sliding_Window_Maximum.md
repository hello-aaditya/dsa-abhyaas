---
problem: 239. Sliding Window Maximum
link: https://leetcode.com/problems/sliding-window-maximum/description/
status: DONE
approach: Sliding Window
level: MODERATE
prerequisite: 
video: https://www.youtube.com/watch?v=xFJXtB5vSmM&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=6
---

# Solution
```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int size = nums.length;
        int start = 0;

        // ARRAYDEQUE CONTAINS THE MAX VALUES FROM nums
        ArrayDeque<Integer> deq = new ArrayDeque<>();
        deq.add(Integer.MIN_VALUE); // INITIALLY deq CONTAINS A SMALLEST VALUE IN JAVA

        int[] max = new int[size - k + 1]; // STORES THE MAXIMUM AMONGST k ELEMENT FROM nums
        int index = 0; // IS USED TO STORE VALUES INSIDE max

        for (int end=0; end<size; end++) {
            int windowSize = end - start + 1; // FIND windowSize
            int dqSize = deq.size(); // FIND deq SIZE

            // IF deq IS NOT EMPTY AND nums[end] > THE LAST VALUE OF deq THEN DELETE IT FROM THE deq
            while ( (!deq.isEmpty()) && (nums[end] > deq.peekLast()) ) { 
                deq.pollLast();
            }

            // ADD ELEMENT (nums[end]) INSIDE deq
            deq.add(nums[end]);

            // IF nums[end] < THE LAST ELEMENT OF deq THEN ADD IT INSIDE deq BECAUSE MAY BE IT WILL BE A MAXIMUM FOR UPCOMING WINDOW
            if (nums[end] < deq.peekLast()) {
                deq.add(nums[end]);
            }

            // IF WE HIT THE windowSize THEN
            if (windowSize == k) {
                max[index++] = deq.peekFirst(); // ADD THE 1st ELEMENT OF deq TO THE index-th POSITION OF max
                // IT'S TIME TO SLIDE THE WINDOW BUT BEFORE SLIDING CHECK WHETHER (nums[start] == FIRST ELEMENT OF deq), IF SO THEN
                // REMOVE THE ELEMENT FROM deq
                if (nums[start] == deq.peekFirst()) {
                    deq.pollFirst();
                }
                // AT THE END SLIDE THE WINDOW
                start++;
            }
            
        }
        return max;
    }
}
```

