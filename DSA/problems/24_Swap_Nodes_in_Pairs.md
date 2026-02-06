---
problem: 24. Swap Nodes in Pairs
link: https://leetcode.com/problems/swap-nodes-in-pairs/description/
status: DONE
approach: Linked List
level: MODERATE
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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (prev.next!=null && prev.next.next!=null) {
            // NODE INITIALIZATION
            ListNode first = prev.next;
            ListNode second = first.next;
            ListNode after = second.next;

            // NODE SWAPPING
            first.next = after;
            second.next = first;
            prev.next = second;

            // NODE UPDATION
            prev = first;
        }
        return dummy.next;
    }
}
```
