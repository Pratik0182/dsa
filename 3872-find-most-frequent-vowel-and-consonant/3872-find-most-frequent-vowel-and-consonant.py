class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        vow = defaultdict(int)
        con = defaultdict(int)
        con['A'] = 0
        vow['A'] = 0
        for ch in s:
          if ch in vowels:
            vow[ch] += 1
          else:
            con[ch] += 1
        return max(vow.values()) + max(con.values())