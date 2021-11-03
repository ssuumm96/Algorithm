def solution(n, jump):
  x = 0
  y = 0
  arr = [[0 for col in range(n)] for row in range(n)]
  
  while n > 0 :
      m = n #이동횟수
        for i in range(m): // 오른쪽으로 jump번 이동하면서 배열을 채운다.
            y = y + jump;
            if y > n:
              y = n - 1
              break
            arr[x][y] = 1
        
        m-=1 // 아래쪽으로 이동하는 횟수는 오른쪽보다 한번 줄어든다.
        
        for i in range(m) : // 아래쪽으로 jump번 이동하면서 배열을 채운다.
            x = x + jump
            if x > n:
              x = n - 1
              break
            arr[x][y] = 1
        
        for i in range(m): // 왼쪽으로 jump번 이동하면서 배열을 채운다.
            y = y - jump
            if y < 0:
              y = 0
              break
            arr[x][y] = 1
        
        m-=1 // 윗쪽으로 이동하는 횟수는 왼쪽보다 한번 줄어든다.
        for i in range(m): // 윗쪽으로 jump번 이동하면서 배열을 채운다.
            x = x - jump
            if x < 0:
              x = 1
              break
            arr[x][y] = 1
        
        n = n -2

return [x,y]
