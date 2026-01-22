---
problem: Container With Most Water
link: https://leetcode.com/problems/container-with-most-water/description/?source=submission-ac
status: DONE
approach: Two Pointer
level: MODERATE
prerequisite: 
video: https://www.youtube.com/watch?v=KVU4JNNJkVg
---

# Solution
```java
class Solution {
    public int maxArea(int[] height) {
        int size = height.length;

        int start = 0;
        int end = size - 1;
        int maxArea = 0;
        while (start < end) {
            int length = Math.min(height[start], height[end]);
            int width = end - start;
            int area = length * width;

            maxArea = Math.max(maxArea, area);

            if (height[start] < height[end]) {
                start++;
            } else if (height[start] >= height[end]) {
                end--;
            } else {
                start++;
                end--;
            }
        }
        return maxArea;
    }
}
```

