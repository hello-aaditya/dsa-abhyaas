---
problem: Middle of a Linked List
link: https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
status: DONE
approach: Linked List, Tortoise and Hare Algorithm
level: MODERATE
prerequisite: 
video: 
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
} */

class Solution {
    int getMiddle(Node head) {
        // code here
        Node slow = head;
        Node fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.data;
    }
}
```

