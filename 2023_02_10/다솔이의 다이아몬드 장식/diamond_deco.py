import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = input()

    print('.', end='')

    for i in N:
        print(f'.#..', end='')

    print()

    print('.', end='')

    for i in N:
        print(f'#.#.', end='')

    print()

    print('#', end='')

    for i in N:
        print(f'.{i}.#', end='')

    print()

    print('.', end='')

    for i in N:
        print(f'#.#.', end='')

    print()

    print('.', end='')

    for i in N:
        print(f'.#..', end='')

    print()