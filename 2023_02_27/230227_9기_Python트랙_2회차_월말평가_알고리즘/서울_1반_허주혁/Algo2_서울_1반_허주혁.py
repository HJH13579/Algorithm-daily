def counting_star(lst):
    mn = N
    for x in lst:
        if x < 0:
            return -1
        else:
            if mn > x:
                mn = x
    return mn

T = int(input())

for tck in range(1, T+1):
    N, K, A, B = map(int, input().split())

    H = K // 2

    arr = [list(input().split()) for _ in range(N)]

    # 별의 최대/최소 행/열 인덱스 찾기
    star_idx_i = []
    star_idx_j = []

    star_idx_max_i = 0
    star_idx_min_i = N
    star_idx_max_j = 0
    star_idx_min_j = N

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                star_idx_i.append(i)
                star_idx_j.append(j)

    for m in star_idx_i:
        if m > star_idx_max_i:
            star_idx_max_i = m

    for m in star_idx_i:
        if m < star_idx_min_i:
            star_idx_min_i = m

    for n in star_idx_j:
        if n > star_idx_max_j:
            star_idx_max_j = n

    for n in star_idx_j:
        if n < star_idx_min_j:
            star_idx_min_j = n

    # 정사각형 안에 '*'가 모두 들어오지 않을 한계점까지 정사각형 크기를 줄이며 반복
    # star_idx_i의 최대값/최소값과 star_idx_j의 최대값/최소값이 모두 A-H<= <=A+H, B-H<= <=B+H 내에 있어야 한다.
    # 최대 확대 횟수는 각 행/열의 범위의 최소/최대 인덱스와 별의 최소/최대 인덱스의 차 중 가장 작은 값
    # 다만, 별들 중 단 하나라도 범위 밖에 있을 경우 == 차이 중 음수값이 하나라도 있을 경우, '-1' 출력

    range_max_i = A + H
    range_min_i = A - H
    range_max_j = B + H
    range_min_j = B - H

    alst = [star_idx_min_i - range_min_i, range_max_i - star_idx_max_i, star_idx_min_j - range_min_j, range_max_j - star_idx_max_j]

    ans = counting_star(alst)

    print(f'#{tck} {ans}')