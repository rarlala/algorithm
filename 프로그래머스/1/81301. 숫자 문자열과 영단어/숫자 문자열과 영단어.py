def solution(s):
    number_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'} 
    
    answer = ''
    string = ''
    for (i, v) in enumerate(s):
        if v.isnumeric():
            answer += str(v)
        elif string + v in number_dict:
            answer += number_dict[string + v]
            string = ''
        else:
            string += v

    return int(answer)