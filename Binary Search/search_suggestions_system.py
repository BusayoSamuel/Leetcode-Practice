"""
https://leetcode.com/problems/search-suggestions-system/description/
"""

class Solution: #Time complexity O(n.m), Space complexity O(n)
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        for i in range(len(searchWord)):
            suggs = []
            for j in range(len(products)):
                if searchWord[:i+1] == products[j][:i+1]:
                    suggs.append(products[j])
                    if len(suggs) == 3:
                        break
            res.append(suggs)

        return res

class BetterSolution: #Time complexity O(nlogn), Space complexity O(n)
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        l , r = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != c): 
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c): #With these two loops you ensure that all words within l and r are valid
                r -= 1

            res.append([])

            for j in range(min(3, r-l+1)):  #You only need a maximum of 3 to be added to the suggestions
                res[-1].append(products[l+j])


        return res

class AnotherSolution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l = 0
        r = len(products) - 1
        res = []

        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or searchWord[i] != products[l][i]):
                l += 1

            while l <= r and (len(products[r]) <= i or searchWord[i] != products[r][i]):
                r -= 1

            res.append(products[l:min(l+3, r + 1)]) #instead of using a for loop

        return res

        
