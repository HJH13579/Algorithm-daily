# [1] 절반 나눠서 -> 양쪽 sort
# [2] 양쪽 합침(merge)

import sys
sys.stdin = open("s_input2.txt", "r")

def msort(lst):
    global ans
    # [1] 종료 조건: 재귀함수의 처음은 종료조건!
    if len(lst) < 2:
        return lst
    # [2] 절반 나눠서(left, right) 양쪽 정렬
    m = len(lst) // 2
    left = msort(lst[:m])
    right = msort(lst[m:])
    # [0] 정답 처리 부분(ans)
    if left[-1] > right[-1]:
        ans += 1

    # [3] left, right에서 작은 값부터 merge
    ret = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1

    ret += left[l:] + right[r:] # 남은 값을 모두 붙임(left와 right 중 하나는 빈 리스트)
    return ret

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    lst = msort(lst)
    print(f'#{tck} {lst[N//2]} {ans}')