class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        sum = 0
        for num in nums:
            sum += num
            self.arr.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.arr[right]
        leftSum = self.arr[left - 1] if left > 0 else 0
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)