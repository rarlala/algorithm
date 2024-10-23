number_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'} 

def solution(s):
    answer = ''
    word = ''
    for (i, v) in enumerate(s):
        if v.isdigit():
            answer += v
        else:
            word += v
            
        if word in number_dict:
            answer += number_dict[word]
            word = ''
    
    return int(answer)