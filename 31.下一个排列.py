#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        idx = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                idx = i
                break
        if idx != 0:
            for i in range(len(nums)-1, idx-1, -1):
                if nums[i] > nums[idx-1]:
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                    break
        nums[idx:] = nums[idx:][::-1]

