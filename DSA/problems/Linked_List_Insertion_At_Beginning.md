---
problem: Linked List Insertion At Beginning
link: https://www.geeksforgeeks.org/problems/linked-list-insertion-at-beginning/1
status: DONE
approach: Linked List
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
}
*/

class Solution {
    public Node insertAtFront(Node head, int x) {
        // code here
        Node newNode = new Node(x);
        // IF LINKED LIST IS EMPTY
        if (head == null) {
            head = newNode;
            return head;
        }
        // IF NOT EMPTY
        Node current = head;
        newNode.next = head;
        head = newNode;
        return head;
    }
}
```
