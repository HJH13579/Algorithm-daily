# 괄호()의 중요성 : 계산 순위
# elif의 중요성 : if만 계속 쓰면 결과가 달라진다.


import sys

sys.stdin = open("s_in.txt", "r")

T = int(input())

def Binarysearch(n, d):
    start_idx = 0
    end_idx = n - 1

    while start_idx <= end_idx: # 검색 구간이 남아있으면
        middle_idx = (start_idx + end_idx) // 2
        if arr[middle_idx] < d: # 왼쪽
            start_idx = middle_idx + 1
        elif arr[middle_idx] > d:   # 오른쪽
            end_idx = middle_idx - 1
        else:
            return middle_idx + 1   # 첫 번째 위치가 1이므로 +1

    return 0    # 검색 실패 시 0 반환

for tck in range(1, T+1):
    N, D = map(int, input().split())

    arr = list(map(int, input().split()))

    result = Binarysearch(N, D)

    print(f'#{tck} {result}')