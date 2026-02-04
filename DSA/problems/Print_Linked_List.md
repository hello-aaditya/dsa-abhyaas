---
problem: Print Linked List
link: https://www.geeksforgeeks.org/problems/print-linked-list-elements/1
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
}*/

class Solution {
    public ArrayList<Integer> printList(Node head) {
        // code here
        ArrayList<Integer> list = new ArrayList<>();
        
        Node current = head;
        while (current != null) {
            list.add(current.data);
            current = current.next;
        }
        return list;
    }
}
```
