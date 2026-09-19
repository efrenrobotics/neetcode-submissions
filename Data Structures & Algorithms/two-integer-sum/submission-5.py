class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through list and create a position map of all numbers
        posMap = {}
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in posMap:
                return [posMap[remainder], index]
            posMap[num] = index
        return [0, 0]