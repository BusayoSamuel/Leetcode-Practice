/*https://leetcode.com/problems/search-a-2d-matrix/description/*/

class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     * Time complexity O(log(m*n)), Space complexity 0(1)
     */
    searchMatrix(matrix, target) {
        var top = 0
        var bottom = matrix.length - 1

        while (top <= bottom){
            var center = Math.floor((top + bottom)/2)

            if (target < matrix[center][0]){
                bottom = center - 1
            } else if(target > matrix[center][matrix[center].length - 1]){
                top = center + 1
            } else{
                var l = 0
                var r = matrix[center].length - 1

                while (l <= r){
                    var m = Math.floor((l + r)/2)

                    if (target > matrix[center][m]){
                        l = m + 1
                    } else if(target < matrix[center][m]){
                        r = m - 1
                    } else{
                        return true
                    }  
                }
                return false
            }
        }
        return false
    }
}
