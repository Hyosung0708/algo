import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# 상하좌우 이동표시
move = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(): # 너비우선탐색 함수 
    global queue
    count = 0 
    # temp가 빈리스트면 queue도 빈리스트, return 0으로 이동   
    while queue:
        # 지나온 길을 표시할 temp
        temp = []        
        while queue:
            # 출발지점 가로(x),세로(y) 좌표를 꺼내서 
            y,x = queue.pop()
            # 상하좌우로 이동
            for i,j in move:
                dy = y+i
                dx = x+j
                # 맵을 벗어나지 않는다면
                if 0 <=dy < N and 0 <= dx < N:	
   		            # 경로의 값이 0이면 방문처리하고 
                    if not map_list[dy][dx]:                       
                        map_list[dy][dx] = 1
                        # 좌표를 second_queue에 추가
                        temp.append((dy,dx))
                    # 도착지에 도착하면 현재 카운트 리턴
                    if map_list[dy][dx] == 3:
                        return count
        # 큐가 비면서 한칸 이동하면 카운트 증가
        count += 1
        queue = temp # 세컨큐를 기본큐에 대입
    return 0 

T = int(input()) 
for tc in range(1, 1+T):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            #2를 찾는다면 큐에 넣고 브레이크
            if map_list[i][j] == 2:
                queue.append((i, j))
                break
        #esle는 브레이크에 걸리지 않았을때만 동작한다.
        #못찾았다면 위로 올린다.
        else: continue
        #2를 찾았다면 더이상의 반복문은 필요가 없으므로 정지
        break
    #결과값을 출력한다.
    print(f'#{tc} {bfs()}')