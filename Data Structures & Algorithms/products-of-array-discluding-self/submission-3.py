class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix product arrays
        prefix = [1] * len(nums)
        for index in range (1, len(nums)):
            # nums = [1, 2, 4, 6]
            # prefix = [1, 1, 1, 1]
            # prefix = [1, 1]
            # prefix = [1, 1, 2, 8]
            prefix[index] = prefix[index - 1] * nums[index - 1] 
 
        postfix = [1] * len(nums)
        for index in range(len(nums) - 2, -1, -1):
            postfix[index] = postfix[index + 1] * nums[index + 1]

        ans = [0] * len(nums)
        for index in range(len(nums)):
            ans[index] = prefix[index] * postfix[index]
        
        return ans