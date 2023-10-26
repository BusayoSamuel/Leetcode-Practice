class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        stack = []
        pairs = []

        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        pairs = sorted(pairs,reverse=True)

        for i in range(len(pairs)):
            time = (target - pairs[i][0])/pairs[i][1]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        