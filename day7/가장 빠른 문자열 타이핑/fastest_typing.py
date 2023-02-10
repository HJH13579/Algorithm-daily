import sys

sys.stdin = open("sample_input.txt", "r", encoding="UTF8")

T = int(input())

for tck in range(1, T + 1):

    A, B = map(str, input().split())
    A_only = []


    N = len(A)
    M = len(B)

    cnt = 0

    for i in range(N - M + 1):
        if A[i:i+M] == B:
            A_only = A.replace(A[i:i+M], '')
            cnt += 1

    mn_typing = len(A_only) + cnt

    print(f'#{tck} {A} {A_only} {cnt} {mn_typing}')



