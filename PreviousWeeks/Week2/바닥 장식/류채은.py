#1388
#바닥장식-그래프쓴건지모르겠..
mat = []

#세로 가로 입력
h,w = map(int,input().split())
#배열 입력
for _ in range(h):
    tmp_deco = input()
    mat.append(list(tmp_deco))

count = 0
for i in range(h):
    for j in range(w):
        if mat[i][j] == '-':
            mat[i][j] = 'x'
            count+=1
            if j+1 < w and mat[i][j+1] == '-':
                right_idx = j+1
                while right_idx < w and mat[i][right_idx]=='-':
                    mat[i][right_idx] = 'x'
                    right_idx +=1
            
        elif mat[i][j] == '|':
            mat[i][j] = 'x'
            count +=1
            if i+1<h and mat[i+1][j] == '|':
                low_idx = i+1
                while low_idx < h and mat[low_idx][j] == '|':
                    mat[low_idx][j] = 'x'
                    low_idx +=1
        else:
            continue
print(count)
