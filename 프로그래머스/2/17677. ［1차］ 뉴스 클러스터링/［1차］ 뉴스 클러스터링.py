from collections import Counter

def solution(str1, str2):
    # 소문자로 바꾸기
    str1, str2 = str1.lower(), str2.lower()
    
    # 2개씩 쪼개고, 알파벳 체크
    def make_multiset(s):
        multiset = []
        for i in range(len(s) - 1):
            part = s[i:i+2]
            if part.isalpha():
                multiset.append(part)
        return multiset
    
    arr1 = make_multiset(str1)
    arr2 = make_multiset(str2)
    
    # 각 멀티셋 원소들의 빈도를 카운트
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    
    # 자카드 유사도 계산하기 = 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나누기
    intersection = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())
    
    if union > 0:
        return int((intersection / union) * 65536)
    return 65536