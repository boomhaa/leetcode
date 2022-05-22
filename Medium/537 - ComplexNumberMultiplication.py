# link to the problem - https://leetcode.com/problems/complex-number-multiplication/

# A complex number can be represented as a string on the form "real+imaginaryi" where:
# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100, 100].
# i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

# link to submission - https://leetcode.com/submissions/detail/704846907/

class Solution:
    def complexNumberMultiply(self, a, b):
        num1 = a.split('+')
        num1[0] = int(num1[0])
        num1[1] = int(num1[1][:-1])
        num2 = b.split('+')
        num2[0] = int(num2[0])
        num2[1] = int(num2[1][:-1])
        real = str(num1[0]*num2[0] - num1[1]*num2[1])
        img = str(num1[1]*num2[0] + num1[0]*num2[1]) + 'i'
        result = real + '+' + img
        return result