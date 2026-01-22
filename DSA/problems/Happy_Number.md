---
problem: Happy Number
link: "[Happy Number](https://leetcode.com/problems/happy-number/)"
status: Done
approach:
level: EASY
---

# Solution
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