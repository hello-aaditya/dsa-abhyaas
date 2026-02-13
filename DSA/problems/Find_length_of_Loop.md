---
problem: Find length of Loop
link: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
status: DONE
approach: Linked List, Fast-Slow Approach
level: MODERATE
prerequisite: https://leetcode.com/problems/linked-list-cycle/
video: https://www.youtube.com/watch?v=70tx7KcMROc&t=2718s
---

# Solution
```java
/*
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}
*/

class Solution {
    public int lengthOfLoop(Node head) {
        // code here
        Node slow = head;
        Node fast = head;
        
        int count = 0;
        
        while ((fast != null) && (fast.next != null)) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) {
                do {
                    slow = slow.next;
                    count++;
                } while (slow != fast);
                return count;
            }
        }
        return 0;
    }
}
```
