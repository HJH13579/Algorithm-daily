# 트리의 저장
# [1] 완전이진트리(노드번호 연속) -> 번호로 접근
#       왼쪽 :  n * 2
#       오른쪽: n * 2 + 1
#       부모노드: n // 2
# 존재노드: n != 0 & n <= N

# [2] 완전이진트리가 아닌 경우 -> 자식노드 저장
#       왼쪽 : ch1[n]
#       오른쪽: ch2[n]
# 존재노드: n != 0

def preord(n):
    if n:   # 존재하는 노드라면 처리
        alst.append(n) # 방문: 필요한 처리
        preord(ch1[n])  # 왼쪽노드
        preord(ch2[n])  # 오른쪽노드


import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    V = int(input())
    lst = list(map(int, input().split()))
#   [1] 트리 구조를 저장(일반트리 => left/right : 자식노드 저장
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)

    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    alst = []
    preord(1)

    print(f'#{tck}', *alst)