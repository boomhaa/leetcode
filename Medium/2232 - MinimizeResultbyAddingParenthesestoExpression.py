# link to the problem - https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

# You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.
# Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.
# Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.
# The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

# link to submission - https://leetcode.com/submissions/detail/741585259/

class Solution:
	def minimizeResult(self, exp: str) -> str:
		r=exp.index('+')
		res=10e10
		resstr=""
		for i in range(r):
			for j in range(r+2,len(exp)+1):
				tm=exp[:i]+'*('+exp[i:j]+')*'+exp[j:]
				tm1=exp[:i]+'('+exp[i:j]+')'+exp[j:]
				if tm[-1]=='*': tm=tm[:-1]
				if tm[0]=='*': tm=tm[1:]
				if eval(tm)<res:
					res=eval(tm)
					resstr=tm1
		return resstr