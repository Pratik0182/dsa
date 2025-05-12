import random

class Solution(object):
    def findSecretWord(self, words, master):
        seen = set()
        D = defaultdict(lambda: defaultdict(set))
        for w1 in words:
            for w2 in words:
                if w1 != w2:
                    curr = sum(a == b for a, b in zip(w1, w2))
                    D[w1][curr].add(w2)

        candidates = words[:]
        C = random.choice(candidates)
        while True:
            if C in seen:
                C = random.choice([w for w in candidates if w not in seen])
            seen.add(C)
            cnt = master.guess(C)
            if cnt == 6:
                return C
            candidates = [w for w in candidates if w != C and sum(a == b for a, b in zip(w, C)) == cnt]
            best = None
            score = float('inf')
            data = set(candidates)
            for w in candidates:
                worst = max([len(D[w][f] & data) for f in D[w]])
                if worst < score:
                    score, best = worst, w
            C = best