class Solution(object):
    def findEvenNumbers(self, digits):
        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and j != k:
                        if digits[i] != 0:
                            if digits[k] % 2 == 0:
                                res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return sorted(res)