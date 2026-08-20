class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for v in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(v)
            else:
                arr2.append(v)
        return arr1 + arr2