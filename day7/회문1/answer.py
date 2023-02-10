# 물론 i,j index로 풀이 가능
# '가능한 경우' 줄 단위 list로 푸는 것이 최고

# 줄단위 접근 (<= arr_t)

# 한 동작이 한 눈에 들어와야 한다.

# 다중 루프일 때는 한 번에 탈출 원할 때 : 함수화
# 여러번 쓰이는 같은 기능 : 함수화

def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(N - M + 1):
            if lst[i:i + M] == lst[i:i + M][::-1]:
                cnt += 1
    return cnt


# T = int(input())
T = 10
for test_case in range(1, T + 1):
    M = int(input())
    N = 8
    arr = [list(input()) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')