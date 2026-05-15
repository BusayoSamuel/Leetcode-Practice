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

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(list(zip(position, speed)), reverse=True)

        for car in cars:
            pos, spd = car

            time = (target - pos)/spd

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)

class MySolution: #Same complexity as above
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = list(zip(position, speed))
        print(pos_and_speed)
        pos_and_speed.sort(key=lambda x:x[0], reverse=True)

        stack = []

        for pos, speed in pos_and_speed:
            time = (target - pos)/speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        
        
        
