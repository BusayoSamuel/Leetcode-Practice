"""
https://leetcode.com/problems/product-of-array-except-self/
"""


class MySolution: #Time complexity 0(n), Space complexity O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []

        curProd = 1

        for i in range(len(nums)):
            curProd *= nums[i]
            prefix.append(curProd)

        curProd = 1

        for i in range(len(nums)-1 , -1 , -1):
            curProd *= nums[i]
            suffix.append(curProd)

        suffix = suffix[::-1]

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(suffix[i+1] * prefix[i-1])

        return res

class MySolution: #Same complexity as above
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        curr = 1
        for i in range(len(nums)):
            curr = curr * nums[i]
            prefix[i] = curr

        curr = 1
        for j in range(len(nums)-1, -1, -1):
            curr = curr * nums[j]
            postfix[j] = curr

        res = []
        curr = 1

        for k in range(len(nums)):
            pre = prefix[k-1] if k > 0 else 1
            post = postfix[k+1] if k < len(nums) - 1 else 1

            res.append(pre * post)

        return res


        


