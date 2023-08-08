import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    
    for i in range(m):
        queue.append(queue.pop(0))
    
    print('#{} {}'.format(tc, queue[0]))
