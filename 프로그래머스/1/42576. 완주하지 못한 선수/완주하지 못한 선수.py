def solution(participant, completion):
    person_dict = {}
    
    for i in participant:
        if i in person_dict:
            person_dict[i] = person_dict[i] + 1
        else:
            person_dict[i] = 1
    
    for i in completion:
        if i in person_dict:
            person_dict[i] = person_dict[i] - 1
    
    for i in person_dict:
        if person_dict[i] > 0:
            return i
        