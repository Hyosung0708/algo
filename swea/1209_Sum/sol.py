import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    n = int(input())  # test no.
    result = 0
    column = [0]*100  # 각 열의 총합
    rightDown, leftDown = 0, 0

    for i in range(100):
        line = list(map(int, input().split()))
        for k in range(100):
            if i == k:
                rightDown += line[k]  # 우하향 대각선 합
            if i + k == 99:
                leftDown += line[k]  # 좌하향 대각선 합
            column[k] += line[k]  # 열의 합
        result = max(result, sum(line))  # 지금까지 행의 합 중 가장 큰 수

    result = max(result, max(column), rightDown, leftDown)  # 가장 큰 수 찾기

    print("#{} {}".format(n, result))