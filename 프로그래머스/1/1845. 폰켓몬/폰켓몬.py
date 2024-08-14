def solution(nums):
    answer = 0
    maxNums = int(len(nums) / 2)
    newNums = len(set(nums))
    
    if newNums >= maxNums:
        return maxNums
    else:
        return newNums