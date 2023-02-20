import sys

sys.stdin = open("s_list2_연습문제1_in.txt", "r")

def my_abs(a, b):
    if a > b:
        a, b = b, a

    return b - a

T = int(input())

for tck in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]  # di, dj : 변화량
    dj = [1, 0, -1, 0]

    result = 0

    # [1] 전체 루프를 순회하면서, 각 요소 4방향 절대값 합을 구하기
    for i in range(N):
        for j in range(N):
            # 4방향에 대한 처리 진행
            for k in range(4):  # K : 방향
                ni, nj = i + di[k], j + dj[k]

    # 더 많이 쓰이는 방법, 다만 for문으로 못 돌리는 경우가 있다.
    # for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    #     ni, nj = i + di, j + dj

                # 반드시 list 범위 내인지 체크 후 사용
                if 0 <= ni < N and 0 <= nj < N:
                    result += my_abs(arr[i][j], arr[ni][nj])
                else:
                    pass

    print(f'#{tck} {result}')