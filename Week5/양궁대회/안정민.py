res, result = 0, [0] * 11

def solution(n, info):
    answer = []

    myinfo = [0] * 11
    dfs(0, n, 0, info, myinfo)

    if res == 0:
        return [-1]
    else:
        return result

def dfs(depth, n, idx, info, myinfo):
    global res, result

    if myinfo[idx] == info[idx]+1:
        idx += 1

    if depth == n:
        my, enermy = calc_score(info, myinfo) 
        diff = my-enermy

        if diff > res:
            res = my-enermy
            result = [x for x in myinfo]

        elif diff > 0 and diff == res:
            for i in range(10, -1, -1):
                if myinfo[i] > result[i]:
                    result = [x for x in myinfo]
                    break
                elif myinfo[i] < result[i]:
                    break

    for i in range(idx, 11):
        myinfo[i] += 1
        dfs(depth+1, n, i, info, myinfo)
        myinfo[i] -= 1

def calc_score(info, myinfo):
    my, enermy = 0, 0
    for i in range(11):
        if myinfo[i] > info[i]:
            my += 10-i
        elif myinfo[i] < info[i]:
            enermy += 10-i
        else:
            if info[i] != 0:
                enermy += 10-i
    return my, enermy