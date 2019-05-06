#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)
            
        res = []
        if not root:
            return True
        inorder(root)
        for i in range(1, len(res)):
            if res[i].val <= res[i-1].val:
                return False
        return True

