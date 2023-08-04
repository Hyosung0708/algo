import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    string_map = []
    for string in range(N):
        string_map.append(input()) # => 'GOFFAKWFSM'
        # string_map.append(list(input())) # => ['G', 'O', 'F', 'F', ...]

    # pprint(string_map)

    result = []

    # 가로 기준점 / 회문의 시작점을 잡기 위한 코드
    for row in range(N):
        for col in range(N-M+1):
            # print(string_map[row][col])

            for i in range(M//2):
                # front : 앞글자 부터 한칸씩(i의 증가량)증가
                f = string_map[row][col+i]
                # back : 뒷글자 부터 한칸씩(i의 감소량)감소
                b = string_map[row][col+M-1-i]

                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 똑같지 않다면
                else:
                    break
            
            # for을 끝까지 도는경우 / break를 만나지 않은경우 => 회문을 찾았다!!!
            else:
                
                for a in range(M):
                    result.append(string_map[row][col+a])

    # 세로 기준점 / 회문의 시작점을 잡기 위한 코드
    for col in range(N):
        for row in range(N-M+1):
            for i in range(M//2):
                # front : 앞글자 부터 한칸씩(i의 증가량)증가
                f = string_map[row+i][col]
                # back : 뒷글자 부터 한칸씩(i의 감소량)감소
                b = string_map[row+M-1-i][col]

                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 똑같지 않다면
                else:
                    break
            else:
                for a in range(M):
                    result.append(string_map[row+a][col])

    print(''.join(result))