# link to the problem - https://leetcode.com/problems/design-hashset/

# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

# link to submission - https://leetcode.com/submissions/detail/701527507/

class MyHashSet:

    def __init__(self):
        self.s = [0 for i in range(1000001)]

    def add(self, key):
        if self.s[key] == 0:
            self.s[key] = 1

    def remove(self, key):
        if self.s[key] == 1:
            self.s[key] = 0

    def contains(self, key):
        return True if self.s[key] == 1 else False