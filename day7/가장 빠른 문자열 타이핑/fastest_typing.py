import sys

sys.stdin = open("sample_input.txt", "r", encoding="UTF8")

T = int(input())

for tck in range(1, T + 1):

    A, B = map(str, input().split())

    N = len(A)
    M = len(B)

    cnt = 0

    for i in range(N - M + 1):
        if A[i:i+M] == B:
            A = A.replace(A[i:i+M], '')
            cnt += 1

    mn_typing = len(A) + cnt

    print(f'#{tck} {A} {cnt} {mn_typing}')
