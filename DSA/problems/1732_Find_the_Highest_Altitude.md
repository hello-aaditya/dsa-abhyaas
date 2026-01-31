---
problem: 1732. Find the Highest Altitude
link: https://leetcode.com/problems/find-the-highest-altitude/description/
status: DONE
approach: Prefix Sum
level: EASY
prerequisite: 
video: 
---

# Solution
```java
class Solution {
    public int largestAltitude(int[] gain) {
        int size = gain.length;
        int currentAltitude = 0;
        int maxAltitude = 0;

        for (int i=0; i<size; i++) {
            currentAltitude += gain[i];
            maxAltitude = Math.max(maxAltitude, currentAltitude);
        }
        return maxAltitude;
    }
}
```
