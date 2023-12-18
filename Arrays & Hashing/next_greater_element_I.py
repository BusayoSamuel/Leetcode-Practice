"""
https://leetcode.com/problems/next-greater-element-i/description/
"""

class Solution1: #Time complexity O(n^2), Space complexity O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(-1)
                    k = j + 1
                    while k < len(nums2):
                        if nums1[i] < nums2[k]:
                            ans[-1] = nums2[k]
                            break
                        k += 1
                    break

        return ans
    

class Solution: #Time complexity O(n + m), Space complexity O(m) where m is the size of nums1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for i in range(len(nums1))]
        stack = []
        hashmap = {}

        for i in range(len(nums1)):
            if nums1[i] in set(nums2):
                hashmap[nums1[i]] = i

        for j in range(len(nums2)):


            while stack and nums2[j] > stack[-1]:
                if stack[-1] in hashmap:
                    ans[hashmap[stack[-1]]] = nums2[j]
                stack.pop()
            

            if nums2[j] in hashmap:
                stack.append(nums2[j])

        return ans
    
class Solution3: #Neetcode Answer
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # O (n + m)
        nums1Idx = { n:i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]

            # while stack exists and current is greater than the top of the stack
            while stack and cur > stack[-1]:
                val = stack.pop() # take top val
                idx = nums1Idx[val]
                res[idx] = cur

            if cur in nums1Idx:
                stack.append(cur)
        
        return res
    
    
        # O (n * m)
        nums1Idx = { n:i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        
        return res