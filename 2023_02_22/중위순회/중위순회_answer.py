def inord(n):
    if 1 <= n <= N:  # 노드가 존재하는 경우
        inord(n * 2)  # left
        alst.append(lst[n])  # 단위작업
        inord(n * 2 + 1)  # right


T = 10
for tc in range(1, T + 1):
    N = int(input())
    # [1] 완전이진트리에 데이터 저장
    lst = [0] * (N + 1)
    for i in range(1, N + 1):
        tlst = input().split()
        lst[i] = tlst[1]

    # [2] 순회하면서 데이터 읽기
    alst = []
    inord(1)
    print(f'#{tc} {"".join(alst)}')