"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(1)
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        isMatch = True
        i = 0
        j = 0

        while j < len(sandwiches) and isMatch:
            isMatch = False
            
            for k in range(i, len(students)):
                if students[i] == sandwiches[j]:
                    isMatch = True
                    j += 1
                else:
                    students.append(students[i])
                i += 1

        return len(students) - i

class CleanerSolution: #Timr conplexity O(n), Space complexity O(1) because the size of cnt is always 2
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches: #sandwiches have to be served in order
            if cnt[s] > 0:
                cnt[s] -= 1
                res -= 1
            else:
                return res #If there is no match, then the remaining students can't be fed

        return res 
            


        
