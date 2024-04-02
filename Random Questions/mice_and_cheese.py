"""
https://leetcode.com/problems/mice-and-cheese/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        arr = [] # [reward2, reward1, reward2 - reward1]

        for i in range(len(reward1)):
            arr.append([reward2[i], reward1[i], reward2[i] - reward1[i]]) 

        arr.sort(key = lambda x: x[2]) #the aim is to maximise the difference in the direction of reward1 > reward2 

        for i in range(len(arr)):
            if k: #once sorted, the first k elements would be the best candidates to swap 
                arr[i] = arr[i][1] 
                k -= 1
            else:
                arr[i] = arr[i][0]

        return sum(arr)
