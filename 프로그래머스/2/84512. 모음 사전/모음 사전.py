def solution(word):
    string = "AEIOU"
    current_word = ["A"]
    count = 1
    
    while word != "".join(current_word):
        count += 1

        if len(current_word) < 5:
            current_word.append('A')
            continue

        for i in range(len(current_word) - 1, -1, -1):
            if string.index(current_word[i]) < 4:
                current_word[i] = string[string.index(current_word[i]) + 1]
                break
            current_word.pop()
    
    return count