class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        data = []
        d = events[0][0]
        i = res = 0
        while data or i < len(events):
            while i < len(events) and events[i][0] <= d:
                s, e = events[i]
                heappush(data, e)
                i += 1
            if data:
                e = heappop(data)
                if d > e:
                    continue
                d += 1
                res += 1
            else:
                d = events[i][0]
        return res