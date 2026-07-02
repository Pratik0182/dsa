class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        '''
        abc
        3*N 
        '''
        arr = [0] * 3 # a, b, c
        res = 0
        i = 0
        l = 0
        while i < N:
            if s[i] == 'a':
                arr[0] += 1
            elif s[i] == 'b':
                arr[1] += 1
            else:
                arr[2] += 1
            while arr[0] > 0 and arr[1] > 0 and arr[2] > 0:
                res += N - i
                if s[l] == 'a':
                    arr[0] -= 1
                elif s[l] == 'b':
                    arr[1] -= 1
                else:
                    arr[2] -= 1
                l += 1
            i +=1
        return res