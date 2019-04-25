# coding=utf-8

import sys

if __name__ == "__main__":
    n, k = sys.stdin.readline().strip().split()
    n = int(n)
    k = int(k)
    height = sys.stdin.readline().strip().split()
    height = [int(x) for x in height]
    height.sort(reverse=True)
    s = height[0]
    ans = 0
    h_cut = 0
    i = 1
    hh = 0
    while i < len(height):
        h = height[i]
        for j in range(i):
            h_cut = h_cut + height[j]
        h_cut = h_cut - i * height[i] - hh
        flag = 0
        if h_cut <= k:
            h_cut = 0
            if i < len(height)-1:
                i += 1
            continue
        while h_cut > k:
            h_cut -= i
            flag = 1
        ans += 1
        hh = hh + h_cut
        if flag == 0:
            i += 1
    print(ans)


# import sys
# from itertools import combinations
#
# if __name__ == "__main__":
#     a = sys.stdin.readline().strip()
#     a = a + ' '
#     i = 0
#     num = ''
#     num_beg = 0
#     numbers = ['0','1','2','3','4','5','6','7','8','9']
#     while a[i] != ' ':
#         if a[i] in numbers:
#             num = ''
#             num_beg = i - 1
#             num = num + a[i]
#             while a[i+1] in numbers:
#                 num = num + a[i+1]
#                 i += 1
#             num = int(num)
#         elif a[i] == '(':
#             begin = i+1
#             j = i+1
#             while a[j] != ')':
#                 j+=1
#             end = j
#             if num_beg == -1:
#                 a = num*a[begin:end] + a[end+1:]
#             else:
#                 a = a[:num_beg+1] + num*a[begin:end] + a[end+1:]
#             i = num_beg
#         elif a[i] == '[':
#             begin = i+1
#             j = i+1
#             while a[j] != ']':
#                 j+=1
#             end = j
#             if num_beg == -1:
#                 a = num*a[begin:end] + a[end+1:]
#             else:
#                 a = a[:num_beg+1] + num*a[begin:end] + a[end+1:]
#             i = num_beg
#
#         elif a[i] == '{':
#             begin = i+1
#             j = i+1
#             while a[j] != '}':
#                 j+=1
#             end = j
#             if num_beg == -1:
#                 a = num*a[begin:end] + a[end+1:]
#             else:
#                 a = a[:num_beg+1] + num*a[begin:end] + a[end+1:]
#             i = num_beg
#
#         i += 1
#     a = a[::-1]
#     a = a[1:]
#     print(a)