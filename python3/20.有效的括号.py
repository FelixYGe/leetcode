#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        stark = []
        leftp = '([{'
        rightp = ')]}'

        for char in s:
            if char in leftp:
                stark.append(char)

            if char in rightp:
                if not stark:
                    return False
                
                tmp = stark.pop()
                if char ==')' and tmp !='(':
                    return False
                if char ==']' and tmp !='[':
                    return False
                if char =='}' and tmp !='{':
                    return False
                
        return stark == []
