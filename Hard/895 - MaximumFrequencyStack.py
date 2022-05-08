# link to the problem - https://leetcode.com/problems/maximum-frequency-stack/

# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
# Implement the FreqStack class:
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

# link to submission - https://leetcode.com/submissions/detail/695474414/

from collections import Counter, defaultdict


class FreqStack(object):

    def __init__(self):
        self.count_of_numbers = Counter()
        self.numbers = defaultdict(list)
        self.maxCount = 0

    def push(self, val):
        f=self.count_of_numbers[val]+1
        self.count_of_numbers[val]=f
        if f>self.maxCount:
            self.maxCount=f
        self.numbers[f].append(val)

    def pop(self):
        x=self.numbers[self.maxCount].pop()
        self.count_of_numbers[x]-=1
        if not self.numbers[self.maxCount]:
            self.maxCount-=1
        return x