def solution(array, commands):
    result = []
    for [i, j, k] in commands:
        slice_array = array[i - 1:j]
        result.append(sorted(slice_array)[k - 1])
    return result