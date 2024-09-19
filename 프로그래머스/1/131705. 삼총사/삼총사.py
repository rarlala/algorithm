def solution(number):
    answer = 0

    def find_sum_zero(selected_count, current_sum, start_index):
        nonlocal answer
        if selected_count == 3:
            if current_sum == 0:
                answer += 1
            return
        
        if start_index == len(number):
            return
            
        find_sum_zero(selected_count + 1, current_sum + number[start_index], start_index + 1)
        find_sum_zero(selected_count, current_sum, start_index + 1)
    
    find_sum_zero(0, 0, 0)
    return answer
    