class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        B = 27
        N = len(word)
        def hash(s):
            h = 0
            p = 1
            for ch in s[::-1]:
                h += (ord(ch) - ord('a') + 1) * p
                p *= B
            return h
        
        res = 0
        for pattern in patterns:
            phash = hash(pattern)
            k = len(pattern)
            for i in range(N - k + 1):
                if hash(word[i:i+k]) == phash:
                    res += 1
                    break
        return res