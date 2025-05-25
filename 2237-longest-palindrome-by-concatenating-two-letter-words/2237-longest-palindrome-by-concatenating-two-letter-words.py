class Solution(object):
    def longestPalindrome(self, words):
        data = set(words)
        freq = Counter(words)
        same = True
        seen = set()
        res = 0
        for w in data:
            if w in seen:
                continue
            IW = w[::-1]
            if w == IW and freq[w] % 2 and same:
                res += 2 * freq[w]
                same = False
            elif w == IW and freq[w] % 2:
                res += 2 * (freq[w] - 1)
            elif w == IW:
                res += 2 * freq[w]
            else:
                res += 4 * min(freq[w], freq.get(IW, 0))
            seen.add(w)
            seen.add(IW)
        return res