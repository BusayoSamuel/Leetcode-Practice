"""
https://leetcode.com/problems/unique-email-addresses/description/
"""

class Solution1: #Time complexity O(n), Space complexity O(n)
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()

        for email in emails:
            prefix, suffix = email.split("@")
            sameas = []
            for i in range(len(prefix)):
                if prefix[i] == "+":
                    break

                if prefix[i] != ".":
                    sameas.append(prefix[i])
                
            sameas = "".join(sameas)
            uniques.add((sameas, suffix))

        return len(uniques)
    
class Solution2: #Same time complexity
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()

        for email in emails:
            i = 0
            local = ""

            while email[i] not in ["@", "+"]:
                if email[i] != ".":
                    local += email[i]
                i += 1

            while email[i] != "@":
                i += 1
            domain = email[i+1:]

            uniques.add((local, domain))

        return len(uniques)
                    