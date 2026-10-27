/*
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
*/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode} 
     * Time complexity O(n), Space complexity O(n)
     */
    removeNthFromEnd(head, n) {
        let dummy = new ListNode(0, head)
        let fast = dummy
        let slow = dummy

        while(fast){
            fast = fast.next
            if(n + 1 > 0){
                n -= 1
                continue
            }
            slow = slow.next
        }

        slow.next = slow.next.next
        return dummy.next
    }
}
