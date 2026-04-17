/*
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
*/

class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     * Time complexity O(n), Space complexoty O(n)
     */
    evalRPN(tokens) {
        const stack = []
        for(var token of tokens){
            if(token === "+"){
                let num1 = stack.pop()
                let num2 = stack.pop()
                stack.push(num2 + num1)
            }else if(token === "-"){
                let num1 = stack.pop()
                let num2 = stack.pop()
                stack.push(num2 - num1)
            }else if(token === "/"){
                let num1 = stack.pop()
                let num2 = stack.pop()
                stack.push(Math.trunc(num2 / num1))
            }else if(token === "*"){
                let num1 = stack.pop()
                let num2 = stack.pop()
                stack.push(num2 * num1)
            }else{
                stack.push(Number(token))
            }
        }
        return stack.pop()
    }
}
