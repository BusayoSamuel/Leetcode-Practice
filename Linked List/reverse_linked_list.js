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
     * @return {ListNode}
     * Time complexity O(n), Space complexity O(1)
     */
    reverseList(head) {
        var prev = null
        var curr = head

        while(curr !== null){
            var temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        }

        return prev
    }
}
