def solution(numbers, target):
    #global answer
    answer = 0
    def dfs(num, level) :
        nonlocal answer
        #결과가 target이랑 같고 계산단계가 len(number)랑 같으면 리턴
        if level == len(numbers) :
            if num == target :
                answer += 1
            return
        
        #첫번째 수 +,-처리
        firstNum = [-num,num]
        
        if level == 1 :
            for i in firstNum:
                dfs(i+numbers[level],level+1)
                dfs(i-numbers[level],level+1)
        else:
            dfs(num+numbers[level],level+1)
            dfs(num-numbers[level],level+1)
            
    dfs(numbers[0], 1)
    
    return answer