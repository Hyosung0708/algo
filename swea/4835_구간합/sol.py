import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    min_total = 1000000000
    max_total = 0
    
    # 구간합을 구하기 위한 i => 뒤의 M개의 데이터를 더하기 위한 시작점
    # index out of range 에러를 발생시키지 않기 위해
    for i in range(N-M+1):

        total = 0
        # 시작점을 기준으로 오른쪽 M개를 구하기 위한 반복
        for j in range(M):
            total = total + numbers[i+j]
        
        if total < min_total:
            min_total = total

        if total > max_total:
            max_total = total

    result = max_total - min_total

    print(f'#{tc} {result}')