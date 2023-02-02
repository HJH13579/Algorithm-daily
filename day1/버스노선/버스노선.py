import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    for i in range(N):
        [Ai, Bi].append(list(map(int, input().split())))
    P = int(input())
    C = []
    for j in range(P):
        C.append(int(input()))

