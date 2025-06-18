class Solution(object):
    def minMaxDifference(self, num):
        N = int(log10(num)) + 1
        num = str(num)
        mx = next((val for val in num if val != '9'), -1)
        mi = num[0]
        if mx == -1:
            return int(num)
        low = high = 0
        for v in num:
            N -= 1
            cmx = 9 if v == mx else int(v)
            cmi = 0 if v == mi else int(v)
            high += cmx * 10**N
            low += cmi * 10**N
        return high - low 
