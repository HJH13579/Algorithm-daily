# 재귀함수 : 단위작업의 반복
# 단위 작업
# [1] p = lst.pop(), left = [], right = []
# [2] lst의 요소 : n < p -> left 추가, p < n -> right 추가
# return qsort(left) + [p] + qsort(right)

# 종료 조건: len(lst) < 2

def qsort(lst):
    # [0] 종료조건: 정렬할 요소가 1개라면 종료!
    if len(lst) <= 1:
        return lst

    # [1] 단위작업: p기준으로 좌/우로 분리!
    p = lst.pop()
    left = []
    right = []
    for n in lst:
        if n < p:
            left.append(n)
        else:
            right.append(n)

    # [2] 왼쪽정렬한 결과 + [p] + 오른쪽을 정렬한 결과
    return qsort(left) + [p] + qsort(right)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    alst = qsort(lst)
    ans = alst[N // 2]
    print(f'#{test_case} {ans}')