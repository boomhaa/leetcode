# link to the problem - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
# Notice that you can return the vertices in any order.

# link to submission - https://leetcode.com/submissions/detail/696003822/

class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        s = {to for _, to in edges}
        return [i for i in range(n) if i not in s]