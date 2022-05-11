# link to the problem - https://leetcode.com/problems/subdomain-visit-count/

# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

# link to submission - https://leetcode.com/submissions/detail/697563934/

class Solution:
    def subdomainVisits(self, cpdomains):
        d = {}
        result = []
        for c in cpdomains:
            l = c.split(' ')
            value = int(l[0])
            domains = l[1].split('.')
            i = 0
            for i in range(len(domains)):
                domain = '.'.join(domains[i:])
                if domain in d.keys():
                    d[domain] += value
                else:
                    d[domain] = value
        for key, value in d.items():
            result.append(' '.join([str(value), key]))
        return result
