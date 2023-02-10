# 끝나는 기준 : 0인 겨우 or 끝 idx (cnt == 0 or cnt == k)
#
# arr[] == 1 : cnt += 1
# arr[] == 0 => cnt == K: cnt = 0
#
# 패딩 : 맨 오른쪽열 + 맨 아래행
#
# <전치행렬>
# - Array 내의 원소를 대각선 축을 기준으로 서로 위치를 바꾼 행렬 (행과 열을 교환하여 얻은 행렬)
#
# - 방법 [1]
# for i in range(N):
#     for j in range(N):
#         if i < j:
#             arr[i][j], arr[j][i] == arr[j][i], arr[i][j]
#
# - 방법 [2]
# Arr_T = list(zip(*arr)) # 요소가 tuple
# Arr_T = list(map(list, zip(*arr)))  # 값 수정 필요 시 -> list에 map
#
# 코딩은 항상 Top-Down 방식으로!


def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:  # 단어를 넣을 수 있는 공백
                cnt += 1
            else:  # 칸 없음!
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]   # 패딩 : 맨 오른쪽열 + 맨 아래행


    # arr와 arr_t 로 각각 개수를 계산
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')