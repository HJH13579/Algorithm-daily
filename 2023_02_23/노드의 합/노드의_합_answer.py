# [1] 순회 : 부모 노드에서 시작, 자식노드 값을 더하기(post order)
# [2] 완전 이진 트리: leaf 노트(끝)에서 시작, 부모노드에게 누적
# [1] < [2]

def postord(n) # L 입력
    if 1 <= n <= N: # 존재하는 노드
        if lst[n] == 0  # 계산 필요한 부모(leaf X)
            lst[n] = postord(n*2) + postord(n*2+!)
        return lst[n]   # 0이든 아니든 리턴
    return 0    # 노드가 없는 경우

def postord(n): # L 입력
    if 1 <= n <= N:  # 존재하는 노드
        if tree[n] == 0:  # 현재노드(부모) 계산필요 (leaf X)
            tree[n] = postord(n * 2) + postord(n * 2 + 1)
        return tree[n]  # 0이든 아니든 리턴
    return 0  # 존재하지 않는 노드(노드가 없는 경우) => 0 리턴
    # 모든경로에서 반드시 리턴!!

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # [1] 완전이진트리에 데이터 저장
    tree = [0] * (N + 1)
    for _ in range(M):
        idx, d = map(int, input().split())
        tree[idx] = d

    # [2] 순회(post-order)
    # ans = postord(L)

    # [3] 루프로처리
    for n in range(N, L - 1, -1):
        tree[n // 2] += tree[n]  # 부모노드에 자식노드 값 누적
    ans = tree[L]
    print(f'#{tc} {ans}')