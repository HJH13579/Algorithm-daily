import sys
sys.stdin = open("input.txt", "r")

def preorder(n):
    if n in ch1:
        preorder(n*2)
        alst.append(ch2[n])
        preorder(n*2+1)

for tck in range(1, 11):
    V = int(input())

    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)

    for i in range(1, V+1):
        lst = list(map(str, input().split()))
        ch1[i] = int(lst[0])
        ch2[i] = lst[1]

    alst = []
    preorder(1)

    print(f'#{tck}', "".join(map(str, alst)))
