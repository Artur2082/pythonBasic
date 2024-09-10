# arr = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
# arr = [0] #-> [0]
# arr = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
arr = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

zeros = [0]*arr.count(0)
arr = [v for v in arr if v != 0] + zeros
print(arr)

# ще одне рішення

# result = []
# zeros = []
# for x in arr:
#     if x == 0:
#         zeros.append(x)
#     else:
#         result.append(x)
# result.extend(zeros)
# print(result)
