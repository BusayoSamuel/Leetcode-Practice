/*
https://leetcode.com/problems/merge-two-sorted-lists/description/
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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     * Time complexity O(n+m), Space complexity O(1)
     */
    mergeTwoLists(list1, list2) {
        const dummy = new ListNode()
        let cur = dummy

        while(list1 !== null && list2 !== null){
            if(list1.val <= list2.val){
                let temp = list1
                list1 = list1.next
                cur.next = temp
                cur = cur.next 
            }else{
                let temp = list2
                list2 = list2.next
                cur.next = temp
                cur = cur.next 
            }
        }

        if (list1 !== null){
            cur.next = list1
        }

        if(list2 !== null){
            cur.next = list2
        }

        return dummy.next

    }
}
