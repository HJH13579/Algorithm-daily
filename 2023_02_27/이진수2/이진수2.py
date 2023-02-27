import sys
sys.stdin = open("s_input1.txt", "r")

def myBinary(num):
    global binary_string

    if num == 0:
        return 0

    if num * 2 >= 1:
        binary_string += '1'
        return myBinary(num*2 - 1)

    else:
        binary_string += '0'
        return myBinary(num*2)

T = int(input())

for tck in range(1, T+1):
    string = float(input())

    binary_string = ''

    myBinary(string)

    if len(binary_string) > 12:
        ans = 'overflow'
    else:
        ans = binary_string

    print(f'#{tck} {ans}')