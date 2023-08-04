import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    result = []

    # 배열 입력
    arr = []
    for i in range(N):
        arr.append(input())

    # 가로 (r은 row c는 column)
    for r in range(N):
        for c in range(N - M + 1):
            if arr[r][c : c + M] == arr[r][c : c + M][ : : -1]: # 회문 체크
                result.append(arr[r][c : c + M]) # 맞으면 결과 리스트 추가


    # 세로
    for r in range(N - M + 1):
        for c in range(N):
            c_list = [] # 세로 열 리스트 생성
            for i in range(M):
                c_list.append(arr[r+i][c])
            if c_list == c_list[ : : -1]: # 세로줄 회문 체크
                result.append(''.join(c_list)) # 맞으면 결과 리스트 추가


    print('#{} {}'.format(tc, result))
