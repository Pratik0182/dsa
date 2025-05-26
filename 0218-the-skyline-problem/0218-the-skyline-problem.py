class Solution(object):
    def getSkyline(self, buildings):
        data = defaultdict(list)
        res = []
        seen = set()
        for x1, x2, height in buildings:
            seen.add(x1)
            seen.add(x2)
            data[x1].append((-height, 1))
            data[x2].append((-height, 0))
        hp = [0]
        heapify(hp)
        for x in sorted(list(seen)):
            for height, mode in data[x]:
                if mode == 1:
                    heappush(hp, height)
                else:
                    temp = []
                    while hp and hp[0] != height:
                        temp.append(heappop(hp))
                    if hp and hp[0] == height:
                        heappop(hp)
                    for h in temp:
                        heappush(hp, h)
            if not res or res[-1][1] != -hp[0]:
                res.append([x, -hp[0]])
        return res