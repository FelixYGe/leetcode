#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums[idx] = nums[-1]
                del nums[-1] 
            else:
                idx += 1
        return len(nums)

