# 그리디 -> 규칙성 => 전체적용 (ex.정렬 후 규칙성 찾기)
# 반례 조심(극단적 Case)
# 10^4보다 크면 완전탐색은 아닐 것이다.
import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())
    lst_w = list(map(int, input().split()))
    lst_t = list(map(int, input().split()))

    # 무거운거 먼저!
    # [1] 내림차순 정렬
    lst_w.sort(reverse=True)
    lst_t.sort(reverse=True)

    # 화물 하나씩 꺼내서, 가능한 경우 트럭 이송
    # [2] 하나씩 짐을 내리면서 현재 트럭에 가능한지 체크
    i = ans = 0
    for n in lst_w:
        if n <= lst_t[i]:
            ans += n
            i += 1
            if i == M:
                break

    print(f'#{tck} {ans}')