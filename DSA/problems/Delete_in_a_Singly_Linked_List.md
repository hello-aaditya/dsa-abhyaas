---
problem: Delete in a Singly Linked List
link: https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1
status: DONE
approach: Linked List
level: MODERATE
prerequisite: 
video: 
---

# Solution
```java
/*
class Node
{
    int data;
    Node next;

    Node(int d)
    {
        this.data = d;
        this.next = null;
    }
}
*/
class Solution {
    Node deleteNode(Node head, int x) {
        // code here
        // A/C TO CONTRAINTS, LINKED LIST ALWAYS CONTAIN MORE THAN 0 NODES
        // IF LINKED LIST HAS ONE ELEMENT
        if (x == 1) {
            head = head.next;
            return head;
        }
        
        // IF LINKED LIST HAS MORE THAN ONE ELEMENT
        Node current = head;
        for (int i=1; i<x-1; i++) {
            current = current.next;
        }
        
        if (current.next != null) {
            current.next = current.next.next;
        }
        return head;
    }
}
```

