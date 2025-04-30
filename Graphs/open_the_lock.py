"""
https://leetcode.com/problems/open-the-lock/description/
"""

class MySolution: #Time complexity O(10^4), Space complexity O(10^4)
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque(['0000'])
        deadends = set(deadends)
        visited = set()
        count = 0

        while q:

            for _ in range(len(q)):
                cur = q.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return count
                cur = [*cur]

                for i, v in enumerate(cur):
                    s = cur.copy()

                    s[i] = str((int(s[i]) + 1 + 10)%10)

                    s1 = ''.join(s)
                    if s1 not in visited:
                        q.append(s1) 

                    visited.add(s1)

                    s[i] = str((int(s[i]) - 2 + 10)%10)
                    s2 = ''.join(s)
                    if s2 not in visited:
                        q.append(s2)

                    visited.add(s2)

            count += 1


        return -1


class CleanerSolution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque([("0000", 0)])
        visit = set(deadends)

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))
        return -1


                


        
