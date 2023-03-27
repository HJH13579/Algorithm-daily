# 가능한 모든 경우의 수 => 정답 (시간초과 주의!)
    # 복잡도 분석, 재귀는 단순하게!

# 이진 tree 먼저 생각 -> multi-tree

# [1] N을 정의(단계별 ~ 종료조건) : list의 index
# [2] tree 표현
# 종료 조건 -> 하부 호출
# 종료 조건은 무조건 제일 위 : if n == N
# n을 증가시켜가며, 나머지는 고정 for 재귀의 독립성

# 먼저 원본을 만들고 나서 가지치기 하자!

# 가지치기 안한 원본 ver.
import sys
sys.stdin = open("s_input.txt", "r")

def subset_sum(n, cnt, sm):
    global ans
    # [0] 가지치기는 가장 위에서, 순서로는 가장 마지막에 실행
    # cnt > CNT인 경우 정답 제외
    if cnt > CNT:
        return
    # sm > K인 경우 정답 제외 (양수만 있기 때문에 가능)
    elif sm > K:
        return

    # [1] 종료 조건(n에 관련) => 정답 처리
    elif n == N:
        if cnt == CNT and sm == K:
            ans += 1
        return
    # [2] 하부 호출
    subset_sum(n+1, cnt+1, sm + lst[n])
    subset_sum(n+1, cnt, sm)

T = int(input())

for tck in range(1, T+1):
    CNT, K = map(int, input().split())
    N = 12
    lst = [n for n in range(1, N+1)]

    # main loop에서는 dfs의 가장 위 노드를 호출!
    # n, cnt, sm
    ans = 0
    subset_sum(0, 0, 0)

    print(f'#{tck} {ans}')
