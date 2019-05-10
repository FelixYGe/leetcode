#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (43.35%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 22.9K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m==n:
            return head
        node_m_before = dummy = ListNode(-1)
        dummy.next = head

        for i in range(m-1):
            node_m_before = node_m_before.next

        prev = None
        cur = node_m_before.next
        node_m = node_m_before.next

        for i in range(n-m+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        node_m_before.next = prev
        node_m.next = cur

        return dummy.next


