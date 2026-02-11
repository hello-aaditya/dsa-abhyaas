---
problem: 83. Remove Duplicates from Sorted List
link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
status: DONE
approach: Linked List
level: EASY
prerequisite: 
video: 
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
    public ListNode deleteDuplicates(ListNode head) {
        // LL IS EMPTY
        if ((head == null) || (head.next == null)) {
            return head;
        }
        
        ListNode first = head;
        ListNode second = first.next;

        while (second != null) {
            if (first.val != second.val) {
                first.next = second;
                first = second;
            }
            second = second.next;
        }
        first.next = null;
        return head;
    }
}
```
