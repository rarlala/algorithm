def solution(numbers):
    return [sum(i) for i in combinations(3, numbers)].count(0)

def combinations(count, numbers):
    if count == 0:
        return [[]]

    if not numbers:
        return []

    when_first_selected = [[numbers[0]] + x for x in combinations(count - 1, numbers[1:])]
    when_first_not_selected = combinations(count, numbers[1:])

    return when_first_selected + when_first_not_selected