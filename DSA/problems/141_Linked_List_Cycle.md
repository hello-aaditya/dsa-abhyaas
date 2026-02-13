---
problem: 141. Linked List Cycle
link: https://leetcode.com/problems/linked-list-cycle/description/
status: DONE
approach: Linked List, Fast-Slow Approach
level: MODERATE
prerequisite: 
video: https://www.youtube.com/watch?v=70tx7KcMROc&t=2718s
---

# Solution
```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;


        while ((fast != null) && (fast.next != null)) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }   
        }
        return false;
    }
}
```
