T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    for _ in range(M):
        q.append(q.pop(0))
    ans = q[0]
    print(f'#{tc} {ans}')
