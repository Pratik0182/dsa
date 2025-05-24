class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for idx, w in enumerate(words):
            if x in w:
                res.append(idx)
        return res