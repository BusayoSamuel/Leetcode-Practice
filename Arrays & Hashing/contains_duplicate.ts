"""
https://leetcode.com/problems/contains-duplicate/submissions/1918087743/
"""

function containsDuplicate(nums: number[]): boolean {
    const hashset = new Set<number>();

    for (const num of nums){
        if(hashset.has(num)){
            return true;
        }
        hashset.add(num);
    }
    return false;
};
