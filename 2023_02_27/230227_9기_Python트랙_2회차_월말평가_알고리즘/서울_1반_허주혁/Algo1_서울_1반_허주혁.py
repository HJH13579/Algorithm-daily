T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_cost = 0
    cnt_tree = 0
    max_idx_i = 0
    max_idx_j = 0

    for i in range(N):
        for j in range(M):
            if j % 2 == 0:  # 가장 왼쪽 세로 줄부터 한 줄 씩 띄어 == 짝수열만
                sum_cost += arr[i][j]   # 짝수열만 비용 합
                cnt_tree += 1   # 나무 숫자 counting

                # 최대값 구하기, 최대값이 같을 경우 큰 열 번호가 와야함으로 '=' 필요
                if arr[max_idx_i][max_idx_j] <= arr[i][j]:
                    max_idx_i = i
                    max_idx_j = j

    # 문제에선 첫번째가 1열이지만, arr상 첫번째 인덱스는 0부터 시작
    # 답 출력 시 열 번호에 +1 필요

    print(f'#{tck} {sum_cost} {cnt_tree} {arr[max_idx_i][max_idx_j]} {max_idx_j+1}')