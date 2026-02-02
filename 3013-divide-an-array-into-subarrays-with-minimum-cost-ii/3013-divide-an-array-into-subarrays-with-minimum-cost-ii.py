from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        sl = SortedList(nums[1:dist+2])
        cur = sum(sl[:k])
        res = cur
        
        for i in range(dist + 2, len(nums)):
            new, old = nums[i], nums[i - dist - 1]
            
            sl.add(new)
            if sl.index(new) < k:
                cur += new - sl[k]
            
            idx = sl.index(old)
            sl.remove(old)
            if idx < k:
                cur += sl[k-1] - old
                
            res = min(res, cur)
            
        return res + nums[0]