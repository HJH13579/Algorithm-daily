# for i in range(0, N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):

lst = [1, 2, 3, 4, 5]
lst_sort = []
N = len(lst)

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            lst_sort.append([lst[i], lst[j], lst[k]])

print(lst_sort)