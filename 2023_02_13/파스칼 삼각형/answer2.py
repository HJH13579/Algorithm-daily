# 내부가 전부 1인 삼각형 대형을 만들어 놓고, 법칙을 적용해서 파스칼 값을 채워넣는 방법
# [1] 모두 1값인 삼각형 arr
# [2] 범위의 값 계산
# for i(1, N)
#   for j(1, i)
#       arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())

    # 출력할 대상 값만 리스트로 만들어서 계산
    # [1] 모두 1인 삼각형 모양 arr 생성
    arr = [[1]*(i+1) for i in range(N)]

    for i in range(1, N):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{tck}')
    for lst in arr:
        print(*lst)
