# # for문으로 부분집합 생성하기
#
# A = [1, 2, 3, 4]
# bit = [0] * 4
# s = 0
# for i in range(2):
#   bit[0] = i
#   for j in range(2):
#     bit[1] = j
#     for k in range(2):
#       bit[2] = k
#       for l in range(2):
#         bit[3] = l
#         print(bit, end = ' ')
#         for p in range(4):
#           if bit[p]:
#             print(A[p], end=' ')
#             s += A[p]
#         print()
#         print(s)

# 비트 연산자로 부분집합 생성하기

arr = [3, 6, 7, 1, 5, 4]

n =  len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분 집합의 개수, 0 ~ 2^n - 1
  s = 0
  cnt = 0

  for j in range(n):  # 원소의 수만큼 비트를 비교함
    if i & (1<<j):  # i의 j번 비트가 1인 경우
      print(arr[j], end=", ")   # j번 원소 출력
      s += arr[j]
      cnt += 1
      # print(s)
  print()
  print(s)
  print(cnt)
print()
# print(s)


# # # 재귀로 부분집합 생성하기
#
# def subset(arr):
#
#     bit = [0] * 10
#     n = 0
#
#     for i in range(2):
#         bit[n] = i
#
#         n += 1
#
#         subset(n)
#
#     if n == 9:
#         return [arr[m] for m in range(10) if (bit[m])]