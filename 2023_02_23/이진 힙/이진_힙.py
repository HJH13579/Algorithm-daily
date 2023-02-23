import sys
sys.stdin = open("s_input.txt", "r")

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[c] < heap[p]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    heap = [0] * 501
    last = 0

    for x in lst:
        enq(x)

    ans_sum = 0
    while N != 0:
        N //= 2
        ans_sum += heap[N]

    print(f'#{tck} {ans_sum}')