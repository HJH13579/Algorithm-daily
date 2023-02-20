import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    N = int(input())

    arr = [input() for _ in range(N)]

    cnt = 0
    result = 'NO'

    di = [0, 0, 1, -1, 1, -1, -1, 1]
    dj = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for x in range(8):
                    cnt = 1
                    for _ in range(4):

                        ni = i + di[x]
                        nj = j + dj[x]

                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            i = ni
                            j = nj
                            cnt += 1
                        else:
                            break

                    if cnt == 5:
                        result = 'YES'
                        break

    print(f'#{tck} {result}')
