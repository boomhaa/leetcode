# link to the problem - https://leetcode.com/problems/goal-parser-interpretation/

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

# link to submission - https://leetcode.com/submissions/detail/687342932/

class Solution(object):
    def interpret(self, command):
        i = 0
        answer = []
        while i < len(command):
            if command[i] == '(':
                if command[i + 1] == ')':
                    answer.append('o')
                    i += 2
                elif command[i + 1] == 'a':
                    answer.append('al')
                    i += 4
            else:
                answer.append("G")
                i+=1
        return ''.join(answer)
