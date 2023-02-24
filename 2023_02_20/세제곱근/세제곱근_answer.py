# 숫자가 매우 크다 => 이진탐색
# while s <= e:
# 범위 s(시작) ~ e(끝)에서 m(중간값)을 정하고 찾고자 하는 값이 속해있는 쪽으로 s/e -> (m+1)/(m-1)로 지정

# while s <= e:
#     m = (s+e) // 2
#     if m ** 3 == N:     # 발견
#         ans <- m
#         break
#     elif m ** 3 < N:    # N이 오른쪽 -> 오른쪽 탐색
#         s <- m + 1
#     else:

# 조건을 만족하는 최대값을 구해라!
# while s <= e:
#     m == (s+e) // 2
#     if check(m, ...) == True:
#         ans <- m # 이 값이 최대값일수도
#         s <- m+1
#     else:

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s, e = 1, N
    ans = -1
    while s<=e:
        m = (s+e)//2
        if m**3 == N:   # 세제곱근 찾음!
            ans = m
            break
        elif m**3 < N:  # 오른쪽에 찾는 값(N)이 있음
            s = m+1
        else:
            e = m-1
    print(f'#{tc} {ans}')



