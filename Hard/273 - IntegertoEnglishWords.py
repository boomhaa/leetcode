# link to the problem - https://leetcode.com/problems/integer-to-english-words/

# Convert a non-negative integer num to its English words representation.

# link to submission - https://leetcode.com/submissions/detail/734023682/

class Solution:
    def numberToWords(self, num: int) -> str:
        units1 = {
            1000000000: 'Billion ',
            1000000: 'Million ',
            1000: 'Thousand ',
            1: ''
        }
        units2 = {
            100: 'Hundred ',
            10: 'Tens ',
            1: ''
        }
        numbers = {
            0: "",
            1: "One ",
            2: "Two ",
            3: "Three ",
            4: "Four ",
            5: "Five ",
            6: "Six ",
            7: "Seven ",
            8: "Eight ",
            9: "Nine ",
            10: "Ten ",
            11: "Eleven ",
            12: "Twelve ",
            13: "Thirteen ",
            14: "Fourteen ",
            15: "Fifteen ",
            16: "Sixteen ",
            17: "Seventeen ",
            18: "Eighteen ",
            19: "Nineteen ",
            20: "Twenty ",
            30: "Thirty ",
            40: "Forty ",
            50: "Fifty ",
            60: "Sixty ",
            70: "Seventy ",
            80: "Eighty ",
            90: "Ninety "
        }
        if num == 0:
            return 'Zero'
        s = ''
        for e in units1:
            if num < e:
                continue
            subnum = num // e
            num %= e
            for m in units2:
                if subnum == 0:
                    break
                if subnum < m:
                    continue
                if m == 100:
                    s += numbers[subnum // m] + units2[m]
                    subnum %= m
                    continue
                if subnum > 19:
                    s += numbers[subnum - subnum % 10] + numbers[subnum % 10]
                else:
                    s += numbers[subnum]
                subnum = 0
            if e != 1:
                s += units1[e]
        return s.strip()
