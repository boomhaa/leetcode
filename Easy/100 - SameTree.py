#link to the problem - https://leetcode.com/problems/same-tree/

#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)