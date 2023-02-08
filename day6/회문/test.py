import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]


    # arr = list(zip(*arr))

    print(f'#{test_case}')
    print(*arr)

    result = list(*arr)
    print(result)