import sys
sys.stdin = open("s_input.txt", "r")

def min_array_sum(i, sm):
    global ans

    if ans < sm:    # 끝까지 가지 전에 합이 이미 최소값을 능가해버릴 경우, 바로 끝내버리고 다음 재귀 돌리기
        return      # 백트래킹

    elif i == N:
        if ans > sm:    # 최소값을 구하고 있으므로
            ans = sm
        return

    else:
        for x in range(N):
            if column_arr[x] == 0:  # 열 미사용 시
                column_arr[x] = 1   # 열 사용 표시
                min_array_sum(i+1, sm + arr[i][x])
                column_arr[x] = 0   # 사용 후 반드시 다시 0으로 clear 해줘야한다!
                                    # 결국 재귀 돌릴 때 또 써야하기 때문

T = int(input())

for tck in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    column_arr = [0] * 10   # 세로 중복 방지용 list (0이면 열 미사용, 사용 시 1로 변환해서 중복 방지)
                            # 어쩌피 세로 줄은 N개이고, 최대 10이므로 10칸

    ans = 90    # N은 최대 10, 10보다 작은 자연수 최대 9,  ans <= 10 * 9
    min_array_sum(0, 0)

    print(f'#{tck} {ans}')