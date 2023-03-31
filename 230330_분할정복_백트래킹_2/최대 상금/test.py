a = 123456

print(str(a))

b = list(str(a))

print(b)

b[1], b[2] = b[2], b[1]

print(b)

result = int(''.join(map(str, b)))

print(result)