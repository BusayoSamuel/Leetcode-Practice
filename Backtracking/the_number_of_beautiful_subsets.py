"""
https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
"""

class MySolution: #Time complexity O(n*2^n), Space complexity O(n)
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        cur = []
        def backtrack(i):
            nonlocal res

            if len(cur) > len(nums):
                return

            for j in range(i, len(nums)):
                cur.append(nums[j])
                if not cur:
                    if nums[j] - 0 != k:
                        res += 1
                        backtrack(j+1)
                else:
                    beauty = True
                    for num in cur:
                        if abs(nums[j] - num) == k:
                            beauty = False
                    if beauty:
                        res += 1
                        backtrack(j+1)
                cur.pop()


        backtrack(0)
        return res


class CleanerSolution: #Time complexity O(n*2^n), Space complexity O(n)
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0  # Result to store the number of beautiful subsets
        cur = []  # Temporary list to hold the current subset
        
        def backtrack(start):
            nonlocal res
            
            # Increment result by 1 for each valid subset found (excluding the empty subset)
            if cur:
                res += 1
            
            for i in range(start, len(nums)):
                # Check if adding nums[i] maintains beauty (no pair with difference k)
                if all(abs(nums[i] - num) != k for num in cur):
                    cur.append(nums[i])  # Choose the number
                    backtrack(i + 1)  # Explore further
                    cur.pop()  # Backtrack to explore other possibilities

        backtrack(0)
        return res


class MySolution: #Time complexity O(n*2^n), Space complexity O(n)
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = []
        res = 0

        def backtrack(i):
            nonlocal res 

            if i >= len(nums):
                for num in set(cur):
                    if num + k in cur or num - k in cur:
                        return

                if cur:
                    res += 1
                return

            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()
            backtrack(i+1)


        backtrack(0)
        return res
            

                
        

                    
                        



        
