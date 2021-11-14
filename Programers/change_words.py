import heapq

def possible(A,B):
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
    return count

def solution(begin, target, words):

    #바꿀 수 있는 글자 없는 경우 리턴
    if not(target in words):
        return 0

    words.append(begin)

    network_dic = dict()

    for i in range(len(words)):
        #각 단어마다 딕셔너리 생성
        network_dic[words[i]] = []
        for j in range(len(words)):
            #하나만 바꿀 수 있는 글자 딕셔너리에 추가
            if possible(words[i],words[j]) == len(begin) - 1:
                network_dic[words[i]].append(words[j])

    queue = [(0,begin)]

    while queue:

        length, node = heapq.heappop(queue)
        #찾으면 리턴
        if node == target:
            return length
        #바꿀수있는 글자가 없으면 패스
        if len(network_dic[node]) == 0:
            pass
        #바꿀수있는 글자 힙에 삽입
        else :
            for i in network_dic[node]:
                #다음 노드 값으로 큐에 삽입
                if i != begin:
                    alt = length + 1
                    heapq.heappush(queue,(alt,i))          
    return length
  
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
#답 :4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
#답 :0
