#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (60.66%)
# Likes:    656
# Dislikes: 0
# Total Accepted:    64.7K
# Total Submissions: 106.5K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 非常常见的一道算法题，将所有数字进行异或操作即可。对于异或操作明确以下三点：
        # 1. 一个整数与自己异或的结果是0
        # 2. 一个整数与0异或的结果是自己
        # 3. 异或操作满足交换律，即a^b=b^a

        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res

