---
problem: Linked List End Insertion
link: https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1
status: DONE
approach: Linked List
level: MODERATE
prerequisite: 
video: 
---

# Solution
```java
/*
class Node{
    int data;
    Node next;

    Node(int x){
        data = x;
        next = null;
    }
}
*/
class Solution {
    public Node insertAtEnd(Node head, int x) {
        // code here
        Node newNode = new Node(x);
        
        // IF LINKED LIST IS EMPTY
        if (head == null) {
            head = newNode;
            return head;
        }
        
        // IF NOT EMPTY
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
        return head;
    }
}
```

