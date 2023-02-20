p = 'ab'  # 찾을 패턴
t = 'aaabaaaabaaaaaabab'  # 전체 문장

M = len(p)
N = len(t)

def bf(p, t, M, N):  # lenOfText , lenOfPattern이 더 나은 변수 이름
    i = 0  # t에서의 비교위치
    j = 0  # p에서의 비교위치

    while i < N and j < M:  # 비교할 문장이 남아있고, 패턴을 찾기 전이면
        if t[i] != p[j]:  # 서로 다른 글자를 만나면
            i -= j  # 비교를 시작한 위치로
            j = -1  # 패턴의 시작 전으로
        i += 1
        j += 1

    if j == M:  # 패턴을 찾은 경우
        return i - M
    else:
        return -1

def bf2(p, t, M, N):  # lenOfText , lenOfPattern이 더 나은 변수 이름
    i = 0  # t에서의 비교위치
    j = 0  # p에서의 비교위치

    while i < N and j < M:  # 비교할 문장이 남아있고, 패턴을 찾기 전이면
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == M:  # 패턴을 찾은 경우
        return i - M
    else:
        return -1

def bf3(p, t, M, N):
    for i in range(N - M + 1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1

def bf4(p, t, M, N):
    cnt = 0
    for i in range(N - M + 1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
    return cnt

print(bf(p, t, M, N))
print(bf2(p, t, M, N))
print(bf3(p, t, M, N))
print(bf4(p, t, M, N))
