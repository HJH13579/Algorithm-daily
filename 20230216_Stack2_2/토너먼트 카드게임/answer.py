# 백트래킹은 재귀를 쓸 수 밖에 없다.
# 재귀는 가능한 모든 수를 구하는 쪽으로 생각 + 끝나는 지점(N)을 생각.

# 단위행동
# [1] 왼쪽, 오른쪽 나눠서 각각 승자
# [2] 각 승자의 승패를 정해서 return(s~e 승자를 찾는)
# 종료 조건: s == e