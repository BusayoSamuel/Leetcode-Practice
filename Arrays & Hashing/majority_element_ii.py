"""
https://leetcode.com/problems/majority-element-ii/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        n = len(nums)

        for num, count in count.items():
            if count > n/3:
                res.append(num)


        return res


class EfficientSolution: #Time complexity O(n), Space complexity O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count
        
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
