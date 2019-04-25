def dfs(grid, pmNum, curProgrammerPos, pmRow, pmCol):
    programmerPos = copy.copy(curProgrammerPos)
    if grid[pmRow][pmCol] == 1:
        # print pmRow, pmCol
        grid[pmRow][pmCol] = 0
        pmNum -= 1
        programmerPos.append([pmRow, pmCol])
    return grid, pmNum, programmerPos



aa = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
row = len(aa)
col = len(aa[0])
# print row,col

ans = []
p_num = 0
p_pos = []
empty_num = 0
res = 0
from sys import exit
import copy

# print row,col
for row in range(row):
    for col in range(col):
        if aa[row][col] == 2:
            ans.append([row, col])
        elif aa[row][col] == 1:
            p_num += 1
            p_pos.append([row, col])



row = len(aa)
col = len(aa[0])
while p_num > 0:
    curProgrammerPos = ans
    for programmerRow, programmerCol in curProgrammerPos:
        if programmerRow > 0:
            if aa[programmerRow - 1][programmerCol] == 1:
                aa[programmerRow - 1][programmerCol] = 0
                p_num -= 1
                ans.append([programmerRow - 1, programmerCol])
            # print '1', programmerPos
        if programmerRow < row - 1:
            if aa[programmerRow + 1][programmerCol] == 1:
                aa[programmerRow + 1][programmerCol] = 0
                p_num -= 1
                ans.append([programmerRow + 1, programmerCol])
            # print '2', programmerPos
        if programmerCol > 0:
            if aa[programmerRow][programmerCol - 1] == 1:
                aa[programmerRow][programmerCol - 1] = 0
                p_num -= 1
                ans.append([programmerRow , programmerCol - 1])
            # print '3', programmerPos
        if programmerCol < col - 1:
            if aa[programmerRow][programmerCol + 1] == 1:
                aa[programmerRow][programmerCol + 1] = 0
                p_num -= 1
                ans.append([programmerRow, programmerCol + 1])
            # print '4', programmerPos
    res += 1
print res