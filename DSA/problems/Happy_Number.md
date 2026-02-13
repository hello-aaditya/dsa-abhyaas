---
problem: Happy Number
link: https://leetcode.com/problems/happy-number/
status: Done
approach:
level: EASY
---

# Solution-1
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
# Solution-2
```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;

        do {
            slow = findSquare(slow);
            fast = findSquare(findSquare(fast));

        } while (slow != fast);
        
        if (slow == 1) {
            return true;
        }
        return false;
    }
    public int findSquare(int number) {
        int square = 0;
        while (number != 0) {
            int lastDigit = number % 10;
            square += (lastDigit * lastDigit);
            number /= 10;
        }
        return square;
    }
}
```