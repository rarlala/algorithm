def solution(people, limit):
    people.sort(reverse = True)
    c = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        left += 1
        c += 1
    
    return c