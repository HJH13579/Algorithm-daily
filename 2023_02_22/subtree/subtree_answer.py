def postord(n):
    global ans
    if n:
        postord(ch1[n])
        postord(ch2[n])
        ans += 1

# return으로 푸는 경우
def po_recur(n):
    if n:
        return po_recur(ch1[n]) + po_recur(ch2[n]) + 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    E, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # [1] 트리를 저장
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    # ans = 0
    # postord(S)      # 기준위치부터 순회(노드: +1)
    ans = po_recur(S)

    print(f'#{tc} {ans}')