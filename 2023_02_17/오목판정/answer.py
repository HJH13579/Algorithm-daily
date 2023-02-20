# 범위 체크를 섬세하게 하거나 / padding을 싸주거나

# [1] 5개 연속 'o'
# [2] 모든 위치에서 4 방향으로 뻗어나가면서 : [(-1, 1), (0, 1), (1, 1), (1,0)]

import sys
sys.stdin = open("s_input.txt", "r")

def solve(arr):
    # 가능한 모든 기준위치를 순회
    for si in range(1, N+1):
        for sj in range(1, N+1):
            # 4방향, 뻗어가면서
            for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                for mul in range(5):
                    ni, nj = si + di * mul, sj + dj * mul
                    if arr[ni][nj] != 'o':
                        break
                else: # 모두 'o'인 경우
                    return 'YES'

    return 'NO'

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]
    ans = solve(arr)
    print(f'#{test_case} {ans}')