import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    string = input()

    # Stacking
    # [1] '(': push
    # [2] ')': pop
    # [3] '(' & '(': 막대 +1
    # [4] '(' & ')': cut (ans += 막대 축적 수)
    # [5] ')' & ')': 막대 -1

    stk = ['(']
    num_rod = 0

    for i in range(1, len(string)):
        if string[i] == '(':
            if not stk:
                stk.append(string[i])
            elif string[i-1] == '(':





    print(f'#{tck} {string}')