#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (71.20%)
# Total Accepted:    7K
# Total Submissions: 9.9K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,1]
# 
# 示例 2:
# 
# 输入: 5
# 输出: [0,1,1,2,1,2]
# 
# 进阶:
# 
# 
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
# 
# 
#
class Solution:
    def countBits(self, num: int) -> List[int]:
        # 思路 1 - 时间复杂度: O(Nk) k is number of bits in num*- 空间复杂度: O(N)******
        # def hammingWeight(n):
        #     cnt = 0
        #     while n != 0:
        #         n &= n-1
        #         cnt += 1
        #     return cnt
    
        # res = []
        # for i in range(num+1):
        #     res.append(hammingWeight(i))
        # return res


        # 思路 1 - 时间复杂度: O(N)- 空间复杂度: O(N)******
        # DP 算法
        # DP 的思路其实不难，就是“把每天当成是末日来相待”，并且这一天发生的事能记下来就记下来。 转换到实际问题上，就是把每一步都当时是最后一步来操作，然后沿途记下一些以后需要的数据即可。
        # 本题是求二进制数中1的个数，首先，创建一个数组dp，数组的索引i就是数字i，索引i对应的值就是数字i二进制数的1的个数。
        # 我们知道，任何一个十进制数字num都可以转换成二进制，并且，转换后的二进制长度是x = floor(log(num, 2)) + 1位，这x位数字除了第一位是1之外，其他位都是0或1。
        # 所以，可以把num拆成两个数的和，其中第一个数是p = 2**(x-1)，第二个数就是num - p。如果num == p, 因为p = 2**(x-1)中数字1的个数是1，那么此时num的二进制数中的1的个数就是1，即dp[num] = 1，否则，dp[num] = dp[p] + dp[num-p](num-p一定小于p)。
        # 总结一下，关键点在于c = a + b,如何找到合适的a、b.
        # 首先只有一轮循环，在每一轮循环里面有log函数，但是基本上可以忽略不计，所以总时间复杂度为O(N)，空间也为O(N)
        from math import log, floor
        dp = [0] * (num+1)
        for i in range(1, num+1):
            x = floor(log(i, 2)) + 1
            p = int(pow(2, x-1))
            if p == i:
                dp[i] = 1
            else:
                dp[i] = dp[p] + dp[i-p]
        return dp


        # 思路 2 - 时间复杂度: O(N)- 空间复杂度: O(N)******
        # dp的另外一种方法，状态方程为 P(x) = P(x&(x-1)) + 1
        # dp = [0] * (num+1)
        # for i in range(1, num+1):
        #     dp[i] = dp[i&(i-1)] + 1
        # return dp

