class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        '''
        odd -> 1 + (n - 1)2
            -> 2n - 1
        sumodd-> n/2*(1 + 2n - 1)
            -> n^2

        even -> 2 + (n - 1)2
            -> 2n
        sumeven -> n/2(2 + 2n)
            -> n + n^2
        '''
        '''
        so = n**2
        se = n + n**2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return gcd(so, se)
        '''

        '''
        common factor of odd and even sum n(n) n(n + 1)
        n and n + 1 cant be further factorized so n is hcf lmao
        '''
        return n