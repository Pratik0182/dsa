class Solution:
    def isNStraightHand(self, hand: List[int], group: int) -> bool:
        N = len(hand)
        if N % group != 0:
            return False
        hand.sort()
        data = [[None, group] for _ in range(N // group)]
        for v in hand:
            placed = False
            for i in range(N // group):
                curr = data[i][0]
                if data[i][1] == 0:
                    continue
                elif curr is None:
                    data[i][0] = v
                    data[i][1] -= 1
                    placed = True
                    break
                elif v - 1 == curr:
                    data[i][0] += 1
                    data[i][1] -= 1
                    placed = True
                    break
            if not placed:
                return False
        return True