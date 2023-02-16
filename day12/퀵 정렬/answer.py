# 재귀함수 : 단위작업의 반복
# 단위 작업
# [1] p = lst.pop(), left = [], right = []
# [2] lst의 요소 : n < p -> left 추가, p < n -> right 추가
# return qsort(left) + [p] + qsort(right)

# 종료 조건: len(lst) < 2

