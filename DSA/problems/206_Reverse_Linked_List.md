---
problem: 206. Reverse Linked List
link: https://leetcode.com/problems/reverse-linked-list/description/
status: DONE
approach: Linked List
level: MODERATE
prerequisite:
video: https://youtu.be/t7YaoQOFXzk
---

# Solution
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // EDGE-CASE-1: IF LINKED LIST IS EMPTY THEN WE WILL JUST RETURN THE head
        // EDGE-CASE-2: IF LINKED LIST CONTAINS ONLY 1 NODE THEN WE DON'T HAVE TO REVERSE ANYTHING, THEN JUST RETURN
        if ((head == null) || (head.next == null)) {
            return head;
        }

        ListNode previous = head;
        ListNode current = previous.next;

        while (current != null) {
            ListNode after = current.next;

            current.next = previous;

            // UPDATION
            previous = current;
            current = after;
        }
        head.next = null;
        head = previous;
        return head;
    }
}
```

