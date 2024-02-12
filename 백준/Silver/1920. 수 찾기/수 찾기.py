N = int(input())
data_list = sorted(list(map(int, input().split())))

M = int(input())
search_list = list(map(int, input().split()))

for data in search_list:
    result = 0
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = int((left + right) / 2)

        if data == data_list[mid]:
            result = 1
            break

        if data <= data_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print(result)