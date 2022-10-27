def solution(arr):
    answer = []
    
    saveNum = -1
    for item in arr:
        if saveNum != item:
            saveNum = item
            answer.append(item)
    
    return answer
