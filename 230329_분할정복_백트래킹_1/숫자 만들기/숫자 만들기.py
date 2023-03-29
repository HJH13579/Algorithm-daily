import sys
from itertools import permutations
from collections import deque

sys.stdin = open("s_input.txt", "r")

symbol_num_dic = {0: '+', 1: '-', 2: '*', 3: '/'}

def symbol(symbol_num_lst):
    lst = []
    for x in range(4):
        for _ in range(symbol_num_lst[x]):
            lst.append(symbol_num_dic[x])
    return lst

def calculator(equation):
    stk = deque()
    for x in equation:
        if isinstance(x, int):
            stk.append(x)
        else:
            if x == '+':
                stk.append(stk.popleft() + stk.popleft())
            elif x == '-':
                stk.append(stk.popleft() - stk.popleft())
            elif x == '*':
                stk.append(stk.popleft() * stk.popleft())
            elif x == '/':
                try:
                    stk.append(int(stk.popleft() / stk.popleft()))
                except ZeroDivisionError:
                    break
    return stk.pop()

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    symbol_num_lst = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))

    ans_lst = []

    combination_symbol_lst = set(permutations(symbol(symbol_num_lst), N-1))

    for symbols in combination_symbol_lst:
        equation_lst = [0] * (2 * N - 1)
        for idx in range(len(equation_lst)):
            if idx == 0:
                equation_lst[idx] = num_lst[idx]
            else:
                if idx % 2 != 0:
                    equation_lst[idx] = num_lst[idx // 2 + 1]
                else:
                    equation_lst[idx] = symbols[idx // 2 - 1]

        ans_lst.append(calculator(equation_lst))

    print(f'#{tck} {max(ans_lst) - min(ans_lst)} {len(combination_symbol_lst)}')