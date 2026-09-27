class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix product arrays
        ans = [1] * len(nums)

        for index in range (1, len(nums)):
            # nums = [1, 2, 4, 6]
            # prefix = [1, 1, 1, 1]
            # prefix = [1, 1]
            # prefix = [1, 1, 2, 8]
            ans[index] = ans[index - 1] * nums[index - 1] 
 
        postfix = 1

        for index in range(len(nums) - 1, -1, -1):
            ans[index] *= postfix
            postfix *= nums[index]
        
        return ans