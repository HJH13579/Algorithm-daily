# 완전 이진트리
# inorder 방식으로 값을 저장
# cnt += 1 : 1씩 증가시키면서

import sys
sys.stdin = open("s_input.txt", "r")

def inord(n):
    global cnt
    if 1 <= n <= N:
        inord(n*2)
        lst[n] = cnt
        cnt += 1
        inord(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0]*(N+1)
    # [1] inorder로 값을 저장
    cnt = 1
    inord(1)    # root부터 숫자 저장

    print(f'#{tc} {lst[1]} {lst[N//2]}')