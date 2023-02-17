import sys
sys.stdin = open("s_input.txt", "r")

def row_length_check(n, m, arr):
    max_length = 0

    for i in range(n+2):
        stk_row = []

        for j in range(m+2):
            if arr[i][j] == 1:  # 1이 나오면
                stk_row.append(arr[i][j])  # stack
            else:
                length_row = len(stk_row)   # 구조물 길이 = stack 길이
                if max_length < length_row: # 가로 구조물 최대 길이 교체
                    max_length = length_row
                while stk_row:  # 스택에 내용물이 없어질 때까지 pop
                    stk_row.pop()

    return max_length


T = int(input())

for tck in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]   # padding
    arr_t = list(zip(*arr)) # 전치 행렬

    # 검사 방식: Stack에 1이 연속을 나올 때까지 push, 0이 나오면 stack의 길이 = 구조물의 길이 & 전부 pop해서 빈 stack 만들기
    # 문제점: 결국 0이 구조물의 끝을 내는 명령어, 근데 끝까지 0이 안 나오면 길이를 못 구함
    # 해결책: 0으로 padding

    ans = 0
    # 가로 길이 검사
    if ans < row_length_check(N, M, arr):
        ans = row_length_check(N, M, arr)

    # 세로 길이 검사
    if ans < row_length_check(M, N, arr_t):
        ans = row_length_check(M, N, arr_t)

    print(f'#{tck} {ans}')