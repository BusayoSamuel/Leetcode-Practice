/*
https://leetcode.com/problems/reorder-list/description/
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
     * @return {void}
     * Time complexity O(n), Space complexity O(1)
     */
    reorderList(head) {
        function reverse(node){
            let prev = null
            let cur = node

            while(cur !== null){
                let temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            }
            
            return prev
        }

        let slow = head
        let fast = head

        while(fast && fast.next){
            slow = slow.next
            fast = fast.next.next
        }

        let l1 = head
        let l2 = slow.next
        slow.next = null

        l2 = reverse(l2)

        while(l1 && l2 ){
            let temp1 = l1.next
            let temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
        }
    }
}
