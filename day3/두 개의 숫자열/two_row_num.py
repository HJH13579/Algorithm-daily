import sys

sys.stdin = open("input.txt", "r")

T = int(input())


for tck in range(1, T+1):
    N, M = map(int, input().split())

    lst_N = list(map(int, input().split()))
    lst_M = list(map(int, input().split()))

    ans = -int(1e6)

    if N < M:
        for i in range(M - N + 1):
            multi1 = 0

            for j in range(N):
                multi1 += lst_N[j] * lst_M[j + i]

            if ans < multi1:
                ans = multi1

    # N > M의 경우 : M과 N을 교환하는 방법이 코드길이를 줄일 수 있다.
    # if N > M:
    #   N, M = M, N
    #   lst_N, lst_M = lst_M, lst_N

    if N > M:
        for x in range(N - M + 1):
            multi2 = 0

            for y in range(M):
                multi2 += lst_N[y + x] * lst_M[y]

            if ans < multi2:
                ans = multi2

    print(f'#{tck} {ans}')