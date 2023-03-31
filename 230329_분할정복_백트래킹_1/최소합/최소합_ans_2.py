import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 왼쪽 위쪽 0으로 패딩: 1,1 => N,N 그림과 매치
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    # 결국 위쪽이나 왼쪽에서 이동해 왔을 것
    # 그럼 위쪽이나 왼쪽 중 작은 숫자를 현재 위치의 숫자에 더해오면 최소값 완성
    # 합의 최소값으로 이루어진 array s
    # [2] 규칙성 발견해서 반복처리
    # 훨씬 짧은 시간
    INF = 10 * 2 * N
    s = [[INF] * (N + 1) for _ in range(N + 1)]
    s[0][1] = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            s[i][j] = min(s[i - 1][j], s[i][j - 1]) + arr[i][j]

    ans = s[N][N]
    # print(f'#{test_case} {s}')
    print(f'#{test_case} {ans}')