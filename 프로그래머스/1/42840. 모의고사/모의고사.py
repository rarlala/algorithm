def solution(answers):
    score = [0,0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i, value in enumerate(answers):
        if value == one[i % len(one)]:
            score[1] += 1
        if value == two[i % len(two)]:
            score[2] += 1
        if value == three[i % len(three)]:
            score[3] += 1
            
    max_score = max(score)
    return list(filter(lambda x: score[x] == max_score, range(len(score))))