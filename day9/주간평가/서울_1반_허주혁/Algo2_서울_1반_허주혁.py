def my_abs(a, b):   # 절댓값 함수
    if a > b:
        c = a - b
    else:
        c = b - a
    return c

T = int(input())

for tck in range(1, T + 1):
    N = int(input())

    r, c = map(int, input().split())

    arr = [[0] * 10 for _ in range(10)]

    cnt = 0 # 획득 점수

    for _ in range(N):
        A, B, K = map(int, input().split())

        if my_abs(A, r) + my_abs(B, c) > K: # 망치 이동 시간 > 두더지 stop 시간 일 때,
            # 망치 위치만 갱신 (가로 이동 후 세로 이동)
                # if 가로 이동 거리 >= 시간
                    # 시간만큼만 가로 이동
                # else 가로 이동 거리 < 시간
                    # 가로 이동 -> (시간-가로 이동 거리)만큼 세로 이동
            if my_abs(B, c) >= K:
                if B >= c:
                    r, c = r, c + K
                else:
                    r, c = r, c - K
            else:
                if A >= r:
                    r, c = r + (K - my_abs(B, c)), B
                else:
                    r, c = r - (K - my_abs(B, c)), B

        else:   # 망치 이동 시간 =< 두더지 stop 시간 일 때,
            r, c = A, B # 망치 위치 = 두더지 위치
            cnt += 1    # 획득 점수 +1 점

    print(f'#{tck} {cnt}')