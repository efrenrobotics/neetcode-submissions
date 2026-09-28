class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums) * 2
        tgt = len(nums)
        i = 0
        for index, num in enumerate(ans):
            if index == tgt:
                i = 0
            ans[index] = nums[i]
            i += 1
        return ans
        