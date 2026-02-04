---
problem: Node at a given index in linked list
link: https://www.geeksforgeeks.org/problems/node-at-a-given-index-in-linked-list/1
status: DONE
approach: Linked List
level: MODERATE
prerequisite:
video:
---

# Solution
```java
/*node class of the linked list
class Node
{
    int data;
    Node next;
    Node(int key)
    {
        data = key;
        next = null;
    }
}
*/

class Solution {
    public int GetNth(Node head, int index) {
        // Code here
        Node current = head;
        for (int i=1; i<index; i++) {
            if (current.next == null) {
                return -1;
            }
            current = current.next;
        }
        return current.data;
    }
}
```
