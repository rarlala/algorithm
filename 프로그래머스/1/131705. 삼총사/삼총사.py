def solution(numbers):
    return [sum(i) for i in list(combinations_generator(3, numbers))].count(0)

def combinations_generator(count, numbers):
    if count == 0:
        yield []
        return
    
    if not numbers:
        return
    
    for x in combinations_generator(count - 1, numbers[1:]):
        yield [numbers[0]] + x
        
    for x in combinations_generator(count, numbers[1:]):
        yield x
