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
        ListNode previous = null;
        ListNode current = head;
        ListNode after = null;

        while (current != null ) {
            after = current.next;

            current.next = previous;
            previous = current;
            current = after;
        }
        return previous;
    }
}
```

