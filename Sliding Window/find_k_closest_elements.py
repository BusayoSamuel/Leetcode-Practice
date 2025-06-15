"""
https://leetcode.com/problems/find-k-closest-elements/description/
"""

class IntuitiveSolution: #Time complexity O(logn + k), Space complexity O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

	#Find search the closest value to target
        val, idx = arr[0], 0
        while l <= r:
            m = (r+l)//2

            curDiff, resDiff = abs(arr[m] - x), abs(arr[idx] - x)
            if curDiff < resDiff or (curDiff == resDiff and arr[m] < arr[idx]): #keeps track of closest value to target
                val, idx = arr[m], m

            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                break

        start = idx 
        end = idx

        while end - start + 1 < k: #Starting from the closest value, we enlarge the window as appropriate
            if start - 1 >= 0 and end + 1 < len(arr):
                if abs(arr[start-1] - x) < abs(arr[end+1] - x):
                    start -= 1
                elif abs(arr[start-1] - x) > abs(arr[end+1] - x):
                    end += 1
                else:
                    if arr[start-1] <= arr[end+1]:
                        start -= 1
                    else:
                        end += 1
            elif start - 1 >= 0 :
                start -= 1
            else:
                end += 1

        return arr[start: end + 1] 


class SlightlyBetterSolution: #Time complexity O(log(n-k)), Space complexity O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (r + l)//2
            if x - arr[m] > arr[m+k] - x: #access if the lefmost value in curr window is less close to value immediately right of window 
                l = m + 1 #therefore the values to left would never be closer
            else:
                r = m #therefore values to right wouldn't be closer

        return arr[l:l+k]


class MySolution: #Time complexity O(n-k), Space complexity O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while l <= r and r - l + 1 > k:
            if abs(arr[r] - x) > abs(arr[l] - x):
                r -= 1
            elif abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r+1]
        
