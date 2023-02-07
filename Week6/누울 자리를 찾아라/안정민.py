import re

def getSpaceCnt(n, board):
    rowCnt, colCnt = 0, 0
    reg = re.compile("\\.{2,}")
    for row in board:
        rowCnt += len(reg.findall(row))
    for c in range(n):
        col = ""
        for r in range(n):
            col += board[r][c]
        colCnt += len(reg.findall(col))

            
    return rowCnt, colCnt

n = int(input())
board = [input() for _ in range(n)]
print(*getSpaceCnt(n, board))