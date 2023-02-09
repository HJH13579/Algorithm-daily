import sys

sys.stdin = open("s_input.txt", "r", encoding="UTF8")

T = int(input())

for tck in range(1, T + 1):

    arr = [list(map(int, input().split())) for _ in range(9)]

    # [1] 1~9 숫자가 있는 리스트와 비교 (but 숫자 정렬이 필요)
    # [2] 어쩌피 스도쿠 룰이 1~9만 쓰임. 그럼 set(집합) 써서 중복을 방지해서 성분 개수가 9개이기만 하면 되는 거 아닐까
    #     범용성은 떨어지지만, 이 룰 안에서만큼은 효율적
    # [3] 1~9 숫자마다 count, 모든 성분의 값이 1이면 통과

    # [2]
    result = 1
    # 가로 검증
    for i in range(9):
        set_row = set([])

        for j in range(9):
            set_row.add(arr[i][j])

        if len(set_row) != 9:
            result = 0
            break

        else:
            continue

    # 세로 검증
    for j in range(9):
        set_column = set([])

        for i in range(9):
            set_column.add(arr[i][j])

        if len(set_column) != 9:
            result = 0
            break

        else:
            continue

    # 3 x 3 작은 격자 검증
    for x in range(3):
        for y in range(3):

            set_grid3 = set([])

            for i in range(3):
                for j in range(3):
                    set_grid3.add(arr[i+3*x][j+3*y])

            if len(set_grid3) != 9:
                result = 0
                break

            else:
                continue

    print(f'#{tck} {result}')