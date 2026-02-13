---
problem: 202. Happy Number
link: https://leetcode.com/problems/happy-number/description/
status: DONE
approach: Linked List, HashSet, Linked List, Fast-Slow Approach
level: MODERATE
prerequisite: https://github.com/hello-aaditya/dsa-abhyaas/blob/main/DSA/problems/Find_length_of_Loop.md
video: https://youtu.be/70tx7KcMROc?t=4623
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