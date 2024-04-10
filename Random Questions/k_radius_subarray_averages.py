"""
https://leetcode.com/problems/k-radius-subarray-averages/description/
"""

class MySolution:  #Time complexity O(n), Space complexity O(n)
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = []
        n = 2*k+1
        l = 0 - k
        m = 0
        r = 0 + k
        curTotal = 0
        totals = []

        for i in range(len(nums)):
            curTotal += nums[i]
            totals.append(curTotal)

        
        while m < len(nums):
            if l < 0 or r >= len(nums):
                avgs.append(-1)
            else:
                if l - 1 >= 0:
                    total = totals[r] - totals[l-1]
                else:
                    total = totals[r]

                avgs.append(total//n)
                
            l += 1 
            r += 1
            m += 1


        return avgs


class CleanerSolution: #Time complexity O(n), Space complexity O(n)
  def getAverages(self, nums: List[int], k: int) -> List[int]:
    res = [-1]*len(nums)

    left, curWindowSum, diameter = 0, 0, 2*k+1
    for right in range(len(nums)):
      curWindowSum += nums[right]
      if (right-left+1 >= diameter):
        res[left+k] = curWindowSum//diameter
        curWindowSum -= nums[left]
        left += 1
    return res
