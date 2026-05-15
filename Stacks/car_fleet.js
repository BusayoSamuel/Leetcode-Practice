/*
https://leetcode.com/problems/car-fleet/description/
*/

class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     * Time complexity O(nlogn), Space complexity O(n)
     */
    carFleet(target, position, speed) {
        const pos_and_speed = position.map((val, i) => [val, speed[i]]);
        pos_and_speed.sort((a, b) => b[0] - a[0]);
        const stack = []

        for(const [pos, speed] of pos_and_speed){
            const time = (target - pos)/speed;

            if(stack.length > 0 && time <= stack[stack.length-1]){
                continue;
            }

            stack.push(time);
        }

        return stack.length;
    }
}
