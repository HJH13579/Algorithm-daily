import sys
sys.stdin = open("s_input.txt", "r")

def bfs(n, m):
    cnt = 0

    queue = [n]

    while m not in queue:
        cnt += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node + 1 <= 10 ** 6 and node + 1 > 0:
                queue.append(node+1)
            if node * 2 <= 10 ** 6 and node * 2 > 0:
                queue.append(node*2)
            if node - 1 <= 10 ** 6 and node - 1 > 0:
                queue.append(node-1)
            if node - 10 <= 10 ** 6 and node - 10 > 0:
                queue.append(node-10)
    return cnt

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tck} {bfs(N, M)}')

