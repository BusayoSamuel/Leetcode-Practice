/*
https://leetcode.com/problems/copy-list-with-random-pointer/description/
*/

// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     * Time complexity O(n), Same complexity O(n)
     */
    copyRandomList(head) {
        const hashmap = new Map()
        hashmap.set(null, null)
        let cur = head

        while(cur){
            hashmap.set(cur, new Node(cur.val))
            cur = cur.next
        }

        cur = head

        while(cur){
            hashmap.get(cur).next = hashmap.get(cur.next)
            hashmap.get(cur).random = hashmap.get(cur.random)
            cur = cur.next
        }

        return hashmap.get(head)
    }
}
