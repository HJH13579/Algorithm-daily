# 사과 먹기 게임1
import sys
sys.stdin = open("sample_input.txt", "r")

direction_dic = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # while 돌릴 거 아니면 마지막 사과 찾기
    mx = 0
    for i in range(N):
        for j in range(N):
            if mx < arr[i][j]:
                mx = arr[i][j]

    # n번 사과 좌표값 찾기(시작점(0,0)을 0번 사과로 지정)
    apple_idx_lst = [[0, 0]]
    for k in range(1, mx+1):
        for idx_i in range(N):
            for idx_j in range(N):
                if k == arr[idx_i][idx_j]:
                    apple_idx_lst.append([idx_i, idx_j])

    # 깔끔한 풀이, 규칙성이 안 보인다.
    # 현재 위치와 도착할 위치간의 관계, 그리고 그 전에 움직이고 있던 방향으로 규칙성이 보인다.
    # 일단 풀어야한다. Hard Coding.

    cnt = 0
    direction_lst = [1]
    for x in range(1, len(apple_idx_lst)):
        # Case 1
        if (apple_idx_lst[x][0] - apple_idx_lst[x-1][0]) < 0 and (apple_idx_lst[x][1] - apple_idx_lst[x-1][1]) > 0:
            if direction_lst[x-1] == 1:
                cnt += 3
                direction_lst.append(4)
            elif direction_lst[x-1] == 2:
                cnt += 2
                direction_lst.append(1)
            elif direction_lst[x-1] == 3:
                cnt += 3
                direction_lst.append(1)
            elif direction_lst[x-1] == 4:
                cnt += 1
                direction_lst.append(1)

        # Case 2
        if (apple_idx_lst[x][0] - apple_idx_lst[x-1][0]) > 0 and (apple_idx_lst[x][1] - apple_idx_lst[x-1][1]) > 0:
            if direction_lst[x-1] == 1:
                cnt += 1
                direction_lst.append(3)
            elif direction_lst[x-1] == 2:
                cnt += 3
                direction_lst.append(3)
            elif direction_lst[x-1] == 3:
                cnt += 3
                direction_lst.append(1)
            elif direction_lst[x-1] == 4:
                cnt += 2
                direction_lst.append(3)

        # Case 3
        if (apple_idx_lst[x][0] - apple_idx_lst[x-1][0]) > 0 and (apple_idx_lst[x][1] - apple_idx_lst[x-1][1]) < 0:
            if direction_lst[x-1] == 1:
                cnt += 2
                direction_lst.append(2)
            elif direction_lst[x-1] == 2:
                cnt += 3
                direction_lst.append(3)
            elif direction_lst[x-1] == 3:
                cnt += 1
                direction_lst.append(2)
            elif direction_lst[x-1] == 4:
                cnt += 3
                direction_lst.append(2)

        # Case 4
        if (apple_idx_lst[x][0] - apple_idx_lst[x-1][0]) < 0 and (apple_idx_lst[x][1] - apple_idx_lst[x-1][1]) < 0:
            if direction_lst[x-1] == 1:
                cnt += 3
                direction_lst.append(4)
            elif direction_lst[x-1] == 2:
                cnt += 1
                direction_lst.append(4)
            elif direction_lst[x-1] == 3:
                cnt += 2
                direction_lst.append(4)
            elif direction_lst[x-1] == 4:
                cnt += 3
                direction_lst.append(2)

    print(f'#{tck} {cnt}')