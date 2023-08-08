import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def section_sum(idx, total):
    global answer

    if idx == N:
        if total < answer:
            answer = total
            return
        
    if total > answer:
        return
    
    for i in range(N):
        if i not in visited:
            visited.append(i)
            section_sum(idx + 1, total + matrix[idx][i])
            visited.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 30
    visited = []
    section_sum(0, 0)
    print('#{} {}'.format(tc, answer))



# 1. 현재 행을 의미하는 idx라는 변수와 현재까지의 합을 의미하는 total 변수를 매개변수로 하는 dfs 함수를 만듦.

# 2. 재귀함수의 종료조건은 idx = N . idx가 N이라는 소리는 모든 행을 돌았다는 소리.

# 3. 지금까지의 합이 answer(최소값을 저장해둔 변수)보다 크다면 바로 return(가지치기)

# 4. visited라는 리스트를 만들어서 지금까지 지나온 열들을 넣어줌

# 5. 0~N-1까지 돌면서 visited에 없으면 방문기록에 넣어주고 다음 재귀함수를 돌림.

# (다음 재귀함수는 idx+1을 해주고 total에 현재 방문한 좌표의 값을 추가 한 후 돌림)

# 6. 재귀함수를 다 돌린후 방문 기록을 pop을 해줘야 현재 i를 빼고 다시 다른 i값으로 돌릴 수 있음.