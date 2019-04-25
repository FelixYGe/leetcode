import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a_x = []
    a_y = []
    res = 0
    for line in range(n):
        x1, y1, x2, y2 = sys.stdin.readline().strip().split(' ')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1> x2:
            x1, x2 = x2, x1
        if y1> y2:
            y1, y2 = y2, y1
        if x1-x2 == 0:
            cnt = abs(y2-y1) + 1

            for i in a_x:
                if x1 == i[0]:
                    if y1 in range(i[2], i[3]+1):
                        cnt -= i[3] - y1 - 1
                    elif y2 in range(i[2],i[3]+1):
                        cnt -= y2 - i[2] - 1
            for ii in a_y:
                if x1 in range(ii[0], ii[1]+1):
                    if ii[2] in range(y1, y2+1):
                        cnt -= 1

            a_x.append([x1, x2, y1, y2])
        else:
            cnt = abs(x2-x1) + 1

            for j in a_y:
                if y1 == j[2]:
                    if x1 in range(j[0], j[1]+1):
                        cnt -= j[1] - x1 - 1
                    elif x2 in range(j[0],j[1]+1):
                        cnt -= x2 - j[0] - 1
            for jj in a_x:
                if y1 in range(jj[2], jj[3]+1):
                    if jj[0] in range(x1, x2+1):
                        cnt -= 1

            a_y.append([x1, x2, y1, y2])
        res += cnt
    print(res)


