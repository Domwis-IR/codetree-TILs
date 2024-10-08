n = int(input())

arr = [int(input()) for _ in range(n)]
# print(arr)

non_ascend_idx = -1

def same_num(idx, arr):
    length = 1
    for i in range(idx, 0, -1):
        if arr[i-1] == arr[i]:
            length += 1
        else:
            break
    return length

def change_num(idx1, idx2, arr):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
        non_ascend_idx = i+1


count = 0
is_not_ascend = True
while is_not_ascend:
    same_num_len = same_num(non_ascend_idx - 1, arr)
    change_num(non_ascend_idx, non_ascend_idx - same_num_len, arr)
    # print("same_num_len", same_num_len)
    # print(arr)
    count += 1
    non_ascend_idx -= same_num_len

    if arr[non_ascend_idx - 1] < arr[non_ascend_idx]:
        is_not_ascend = False

print(count)