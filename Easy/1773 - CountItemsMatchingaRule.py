# link to the problem - https://leetcode.com/problems/count-items-matching-a-rule/

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

# link to submission - https://leetcode.com/submissions/detail/689718858/

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        indexes={'type':0,
                 'color':1,
                 'name':2}
        index=indexes[ruleKey]
        count=0
        for i in range(len(items)):
            if ruleValue==items[i][index]:
                count+=1

        return count