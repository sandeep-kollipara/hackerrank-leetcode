# 1. Two Sum - LeetCode (Original 20230519)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = -1
        for i in range(len(nums)):
            nums_2 = [y + nums[i] for y in nums[i+1:len(nums)]]
            if target in nums_2:
                j = nums_2.index(target)+i+1
                break
        return i, j
