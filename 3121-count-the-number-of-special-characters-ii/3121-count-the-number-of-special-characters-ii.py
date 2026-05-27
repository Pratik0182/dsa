from collections import defaultdict
import heapq
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        diff = ord('a') - ord('A')
        pq = defaultdict(list)
        for idx, ch in enumerate(word):
            if ch.islower():
                heapq.heappush(pq[ch], -idx)
            else:
                heapq.heappush(pq[ch], idx)
        res = 0
        ##abacacABABC
        ##012345678, A = {6, 8}... a = {0,2,4}
        for ch in set(word):
            if ch.islower():
                conj = chr(ord(ch) - diff)
                if conj in pq and -pq[ch][0] < pq[conj][0]:
                    res += 1
        return res