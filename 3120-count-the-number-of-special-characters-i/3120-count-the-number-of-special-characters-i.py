class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #print(ord('A'), ord('a'))
        diff = ord('a') - ord('A')
        sp = set()
        for ch in set(word):
            sp.add(ord(ch))
        res = 0
        for ch in set(word):
            if ord(ch) + diff in sp:
                res += 1
        return res