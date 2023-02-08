import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    lst1 = list(input())

    lst1 = lst1[::-1]

    for i in range(len(lst1)):
        if lst1[i] == 'q':
            lst1[i] = 'p'
        elif lst1[i] == 'p':
            lst1[i] = 'q'
        elif lst1[i] == 'b':
            lst1[i] = 'd'
        elif lst1[i] == 'd':
            lst1[i] = 'b'

    print(f'#{tck}', end=' ')
    print(*lst1, sep='')
    
    
# 딕셔너리로 풀기
# dct = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}


