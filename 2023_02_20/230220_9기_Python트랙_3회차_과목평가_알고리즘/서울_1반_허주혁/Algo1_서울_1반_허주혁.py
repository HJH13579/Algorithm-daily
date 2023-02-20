T = int(input())

for tck in range(1, T+1):
    N = int(input())

    arr_hi = [list(map(int, input().split())) for _ in range(N)]

    lst_height = [] # 봉우리 높이를 담을 list
    ans = 0

    for i in range(1, N-1): # 가장자리는 봉우리에서 제외(= 자동 패킹), 안쪽만 탐색
        for j in range(1, N-1):
            for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)):   # 주변 8개 구역
                if arr_hi[i][j] <= arr_hi[i + di][j + dj]:  # 8개 구역 중 하나라도 같거나 크면
                    break   # 다음 가장자리
            else:   # break 없이 다 돌면 = 8개 구역 모두 다 작으면
                lst_height.append(arr_hi[i][j]) # 봉우리로 인정, list에 추가

    if not lst_height or len(lst_height) == 1:  # 봉우리가 없거나 1개이면
        ans = -1

    else:   # 봉우리가 2개 이상이면
        mx = 0  # hi가 0 이상
        mn = 10 # 10 이하

        for x in lst_height:    # 최대 높이 봉우리
            if mx < x:
                mx = x

        for y in lst_height:    # 최소 높이 봉우리
            if mn > y:
                mn = y

        ans = mx - mn   # 봉우리 높이 차이

    print(f'#{tck} {ans}')