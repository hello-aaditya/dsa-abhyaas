---
problem: 42. Linked List Cycle II
link: https://leetcode.com/problems/linked-list-cycle-ii/description/
status: DONE
approach: Linked List, Fast-Slow Approach
level: MODERATE
prerequisite: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
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

/*
Solution:
- find the length of cycle present inside LL. -> https://www.geeksforgeeks.org/problems/find-length-of-loop/1
    - if length is 0 means return null (means cycle is not found);

- create two Node (ptr1, ptr2 and initialized them with head). 
    - move any pointer (ptr2) of size length.
    - now move ptr1 and ptr2 (till ptr1 != ptr2) (move means ptr = ptr.next)
        - at a point when they will definitely equals then return any of the Node (ptr1 or ptr2)

*/
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // FIND THE LENGTH OF THE CYCLE
        ListNode slow = head;
        ListNode fast = head;

        int length = 0;

        while ((fast != null) && (fast.next != null)) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                do {
                    slow = slow.next;
                    length++;
                } while (slow != fast);
                break;
            }
        }
        if (length == 0) {
            return null;
        }
        ListNode ptr1 = head;
        ListNode ptr2 = head;

        while (length != 0) {
            ptr2 = ptr2.next;
            length--;
        }

        while (ptr1 != ptr2) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
            
        }
        return ptr2;
    }
}
```

