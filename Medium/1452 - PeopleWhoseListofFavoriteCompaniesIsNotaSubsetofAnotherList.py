# link to the problem - https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

# Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).
# Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

# link to submission - https://leetcode.com/submissions/detail/764845880/

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        for i in range(len(favoriteCompanies)):
            s = set(favoriteCompanies[i])
            flag = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if s.issubset(set(favoriteCompanies[j])):
                    flag = False
                    break
            if flag:
                ans += [i]
        return ans