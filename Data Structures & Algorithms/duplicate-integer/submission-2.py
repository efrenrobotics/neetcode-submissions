class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # to check if an array contains a duplicate, we instantiate an empty Number Set
        # we iterate through the array, if the current number is in number set then array contains duplicate, return true
        # otherwise, add number to set
        # return false

        numSet = set()

        for num in nums:
            if (num in numSet):
                return True
            numSet.add(num)
        
        return False