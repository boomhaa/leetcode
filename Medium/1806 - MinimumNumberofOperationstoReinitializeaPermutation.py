# link to the problem - https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

# You are given an even integer n. You initially have a permutation perm of size n where perm[i] == i (0-indexed)
# In one operation, you will create a new array arr, and for each i:
# If i % 2 == 0, then arr[i] = perm[i / 2].
# If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
# You will then assign arr to perm.
# Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.

# link to submission - https://leetcode.com/submissions/detail/729058559/

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        res=0
        arr=list(range(n))
        diff=1
        while diff>0:
            diff=0
            new=[el for el in arr]
            for i,el in enumerate(arr):
                new[i]=arr[i//2] if i%2==0 else arr[n//2+(i-1)//2]
                if i!=new[i]: diff+=1
            arr=new
            res+=1
        return res