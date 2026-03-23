/* https://leetcode.com/problems/min-stack/description/ */



/*
  Time complexity O(1), Space complexity O(n)
*/
var MinStack = function() {
    this.stack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    const curMin = this.stack.length? Math.min(this.stack[this.stack.length - 1][1], val) : val;
    this.stack.push([val, curMin]);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
   this.stack.pop();
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1][0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.stack[this.stack.length - 1][1];
    
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
