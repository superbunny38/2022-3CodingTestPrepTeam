#1932
#정수 삼각형

N = int(input())#삼각형 크기
triangle = []

for _ in range(N):
    floor = list(input().split())
    floor = [int(x) for x in floor]
    triangle.append([0]+floor+[0])

for i in range(N-1,-1,-1):
    #print(i)
    for j in range(i+1):
        triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])

print(triangle[0][1])
