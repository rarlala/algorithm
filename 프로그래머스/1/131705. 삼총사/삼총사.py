def solution(number):

    def find_sum_zero(selected_count, current_sum, start_index):
        if selected_count == 3:
            if current_sum == 0:
                return 1
            return 0
        
        if start_index == len(number):
            return 0
            
        return (find_sum_zero(selected_count + 1, current_sum + number[start_index], start_index + 1) + find_sum_zero(selected_count, current_sum, start_index + 1))
    
    return find_sum_zero(0, 0, 0)
    