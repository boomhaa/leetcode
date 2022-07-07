# link to the problem - https://leetcode.com/problems/search-suggestions-system/

# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.

# link to submission - https://leetcode.com/submissions/detail/740782019/

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        res = []
        for i in range(1,len(searchWord)+1):
            r = []
            for j in products:
                if j.startswith(searchWord[:i]) and len(r) < 3:
                    r.append(j)
            res.append(r)
        return res