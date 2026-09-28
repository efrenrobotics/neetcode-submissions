class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map of number and index
        indexMap = {}
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in indexMap:
                return [indexMap.get(remainder), index]
            indexMap[num] = index
        return [-1, -1]