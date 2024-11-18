"""
https://leetcode.com/problems/validate-binary-tree-nodes/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)

        root = 0

        for i in range(n):
            if i not in hasParent:
                root = i
                break

        stack = [root]
        visited = set()
        cur = None

        while stack:
            cur = stack.pop()

            if cur in visited:
                return False

            visited.add(cur)

            if rightChild[cur] != -1:
                stack.append(rightChild[cur])

            if leftChild[cur] != -1:
                stack.append(leftChild[cur])

        return len(visited) == n


class OtherSolution: #Same complexity
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)

        root = 0

        for i in range(n):
            if i not in hasParent:
                root = i
                break

        visited = set()

        def dfs(i):
            if i == -1:
                return True

            if i in visited:
                return False

            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])

        return dfs(root) and len(visited) == n
            
            

        
            
            

        
            
            

        
