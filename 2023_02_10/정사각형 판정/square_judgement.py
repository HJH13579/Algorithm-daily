import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    N = int(input())

    arr = [list(map(str, input())) for _ in range(N)]

    # [1] 노가다 : 일정 크기의 정사각형이 있는지 일일이 확인 => 비범용적인 코드
    # [2] '#'의 연속된 가로 길이(2 이상)를 측정, 그만큼의 세로에서도 빈틈없이 채워져 있는지 확인

    # [1]
    # '#' 개수 카운팅 부터

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                cnt += 1

    result = 'no'

    for x in range(1, N + 1):

        for i in range(N - x + 1):
            for j in range(N - x + 1):

                num = 0

                for m in range(x):
                    for n in range(x):
                        if arr[m+i][n+j] == '#':
                            num += 1

                if num == x * x and num == cnt:
                    result = 'yes'


    # [2]
    # for lst in arr:
    #     for x in lst:
    #         if x == '#':


    print(f'#{tck} {result}')