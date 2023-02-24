# IM Level: 그냥 다 구하고 해도 풀리는 난이도와 충분한 시간 제공
# IM 평가 시험은 어렵게 생각하지 말고 다 구해보자.
# 최대 한 번 : 모두 해보고, 가장 좋은 결과를 저장
# sort 방법 중 하나 : n개 중 1개/2개/3개 뽑는 모든 조합

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    lst = list(input())

    N = len(lst)

    mx = mn = int("".join(lst))

    for i in range(N-1):
        for j in range(i+1, N):
            lst[i], lst[j] = lst[j], lst[i]
            if int(lst[0]) != 0 and mx < int("".join(lst)):
                mx = int("".join(lst))
            if int(lst[0]) != 0 and mn > int("".join(lst)):
                mn = int("".join(lst))
            lst[i], lst[j] = lst[j], lst[i] # 원상 복구

    print(f'#{tck} {mn} {mx}')
