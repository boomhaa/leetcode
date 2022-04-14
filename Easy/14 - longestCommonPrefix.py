#link to the problem - https://leetcode.com/problems/logngest-common-prefix/g

class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len=1000000000
        for i in range(len(strs)):
            if len(strs[i])<min_len:
                min_len=len(strs[i])
        stringer=""

        for i in range(min_len):
            count=0
            for j in range(1,len(strs)):
                if strs[0][i]==strs[j][i]:
                    count+=1
            if count==len(strs)-1:
                stringer+=strs[0][i]
            else:
                break
        if len(stringer)==0:
            return ""
        return stringer