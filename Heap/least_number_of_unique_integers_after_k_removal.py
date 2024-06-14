"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = Counter(arr)
        numfreq = []

        for num, freq in hashmap.items():
            numfreq.append([freq, num])

        heapq.heapify(numfreq)

        while numfreq and k:
            freq, num = heapq.heappop(numfreq)

            if k > freq:
                k -= freq
            elif k == freq:
                return len(numfreq)
            else:
                return len(numfreq) + 1

        return len(numfreq)
    

class CleanerSolution: #Same complexity
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = Counter(arr)
        freq = list(hashmap.values())

        heapq.heapify(freq)

        res = len(freq)
        while freq and k:
            f = heapq.heappop(freq)

            if k >= f:
                k -= f
                res -= 1

        return res
    
class BetterSolution: #Time complexity O(n), Space complexity O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = Counter(arr)
        freq = [0] * (len(arr) + 1) #we represent every possible freq using the indexes of this array

        for num, f in hashmap.items():
            freq[f] += 1

        res = len(hashmap)
        for f in range(1, len(freq)): #we don't count numbers with zero frequency so we start from 1
            remove = freq[f] #the number of values that have this freq

            if k >= remove * f:
                k -= f * remove
                res -= remove
            else:
                remove = k // f #this tells us the max number of time we subtract this f from k and thereby the max number of values that can be removed
                res -= remove
                break

        return res

