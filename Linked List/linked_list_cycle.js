/*
https://leetcode.com/problems/linked-list-cycle/description/
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
     * @return {boolean}
     * Time complexity O(n), Space complexity O(1)
     */
    hasCycle(head) {
        var slow = head
        var fast = head

        while(fast && fast.next){
            slow = slow.next
            fast = fast.next.next

            if(slow === fast){
                return true
            }
        }

        return false
    }
}
