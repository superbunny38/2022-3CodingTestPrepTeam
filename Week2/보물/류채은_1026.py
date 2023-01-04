#보물
#1026
from itertools import permutations
import sys

def return_S(A,B):
    N = len(A)
    s = 0
    for i in range(N):
        s += A[i]*B[i]
    return s
        

N = int(input())
A = list(input().split())
A = [int(x) for x in A]

B = list(input().split())
B = [int(x) for x in B]

    
A = sorted(A)    
B = sorted(B, reverse = True)
min_s = return_S(A,B)
print(min_s)
