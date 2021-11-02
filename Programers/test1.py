def solution(id_list, k):
    answer = 0
    array = []
    d = {}
    
    for i in id_list:
        id = i.split()
        id_not = list(set(id))
        for x in id_not:
            if d.get(x,0) < k:
                d[x] = d.get(x,0) +1
        
    return sum(d.values())
