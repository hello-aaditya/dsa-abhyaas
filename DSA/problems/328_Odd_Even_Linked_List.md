---
problem: 328. Odd Even Linked List
link: https://leetcode.com/problems/odd-even-linked-list/description/
status: DONE
approach: Linked List
level: MODERATE
prerequisite: 
video: https://youtu.be/qf6qp7GzD5Q?t=683
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
    public ListNode oddEvenList(ListNode head) {
        if ((head == null) || (head.next == null) || (head.next.next == null)) {
            return head;
        }
        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = head.next;

        while ((even != null) && (even.next != null)) {
            odd.next = odd.next.next;
            even.next = even.next.next;

            odd = odd.next;
            even = even.next;
        }
        odd.next = evenHead;

        return head;
    }
}
```
