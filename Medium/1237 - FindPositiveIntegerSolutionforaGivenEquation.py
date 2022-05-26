# link to the problem - https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

# Given a callable function f(x, y) with a hidden formula and a value z, reverse engineer the formula and return all positive integer pairs x and y where f(x,y) == z. You may return the pairs in any order.
# While the exact formula is hidden, the function is monotonically increasing, i.e.:
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)
# The function interface is defined like this:
# interface CustomFunction {
# public:
#   // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
#   int f(int x, int y);
# };
# We will judge your solution as follows:
# The judge has a list of 9 hidden implementations of CustomFunction, along with a way to generate an answer key of all valid pairs for a specific z.
# The judge will receive two inputs: a function_id (to determine which implementation to test your code with), and the target z.
# The judge will call your findSolution and compare your results with the answer key.
# If your results match the answer key, your solution will be Accepted.

# link to submission - https://leetcode.com/submissions/detail/707473437/

class Solution:
    def findSolution(self, customfunction, z):
        res, y = [], 1000
        for x in range(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])
        return res