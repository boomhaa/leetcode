# link to the problem - https://leetcode.com/problems/design-an-ordered-stream/

# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.
# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.
# Implement the OrderedStream class:
# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

# link to submission - https://leetcode.com/submissions/detail/689729500/

class OrderedStream(object):

    def __init__(self, n):
        self.new_list=['']*n
        self.i=0
    def insert(self, idKey, value):
        self.new_list[idKey-1]=value
        list_for_returning=[]
        while self.i<len(self.new_list) and self.new_list[self.i]!="":
            list_for_returning.append(self.new_list[self.i])
            self.i+=1
        return list_for_returning
