def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]
    arr2 = list(map(list, zip(*arr2)))
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for x, y in zip(arr1[i], arr2[j]):
                answer[i][j] += x * y
        
    return answer