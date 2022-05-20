# link to the problem - https://leetcode.com/problems/decode-xored-array/

# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique

# link to submission - https://leetcode.com/submissions/detail/687322856/

class Solution(object):
    def decode(self, encoded, first):
        answer=[first]
        for elem in encoded:
            answer.append(answer[-1]^elem)
        return answer
