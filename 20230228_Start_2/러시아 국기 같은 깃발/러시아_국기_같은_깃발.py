import sys
sys.stdin = open("sample_input.txt", "r")

def counting(i, M, arr):
    cnt_W = 0
    cnt_B = 0
    cnt_R = 0

    for j in range(M):
        if arr[i][j] == 'W':
            cnt_W += 1
        if arr[i][j] == 'B':
            cnt_B += 1
        if arr[i][j] == 'R':
            cnt_R += 1

    return [cnt_W, cnt_B, cnt_R]

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    alst = []
    # 맨 윗줄은 항상 모두 W, 맨 아랫줄은 항상 모두 R
    # 중간엔 B
    # B줄을 기점으로 위에는 all W, 아래는 all R
    for i in range(1, N-1):
        cnt = 0

        j = i

        while 1:
            cnt += counting(j, M, arr)[0]
            cnt += counting(j, M, arr)[2]

            if j == N-2:
                break

            elif max(counting(j+1, M, arr)) != counting(j+1, M, arr)[1]:
                break

            j += 1

        for m in range(0, i):
            cnt += counting(m, M, arr)[1]
            cnt += counting(m, M, arr)[2]

        for n in range(i+1, N):
            cnt += counting(n, M, arr)[0]
            cnt += counting(n, M, arr)[1]

        alst.append(cnt)

    print(f'#{tck} {min(alst)}')