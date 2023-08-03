import sys
sys.stdin = open('input.txt')


T=int(input())

for t in range(1,T+1):
    area=[[0 for _ in range(10)] for _ in range(10)]    # 원소가 0인 10x10행렬
    count=0                                             # 겹치는 칸의 개수
    N=int(input())

    for i in range(1,N+1):
        row1,col1,row2,col2,color=map(int,input().split()) # 첫번째 행렬인 (row1,col1), 두번째 행렬인 (row2,col3), color(문제에서 지정한대로 color=1이면 빨간색, color=2이면 파란색을 의미)

        for row in range(row1,row2+1):                  # 행의 시작과 끝까지
            for col in range(col1,col2+1):
                if color==1:                            # 만약 색이 빨간색이면
                    if area[row][col]==0:               # 만약 색이 아무것도 없는 빈칸이면
                        area[row][col]=1                # 빨간색으로 칠하고

                    elif area[row][col]==2:             # 만약 색이 파란색이면
                        area[row][col]=3                # 파란색을 보라색으로 칠해라.
                        count += 1                      # 그런다음 겹치는 칸의 개수를 세어주기 위해 +1을 해준다.

                else:                                   # 만약 색이 파란색이면
                    if area[row][col]==0:               # 만약 색이 아무것도 없는 빈칸이면
                        area[row][col]=2                # 파란색으로 칠해라.

                    elif area[row][col]==1:             # 만약 색이 빨간색이면
                        area[row][col]=3                # 빨간색을 보라색으로 칠해라.
                        count+=1                        # 그런다음 겹치는 칸의 개수를 세어주기 위해 +1을 해준다.


    print("#{} {}".format(t,count)) 








    ## 문제를 흐름의 순서에 따라 정리해봅시다.

# 1.원소가 0인 10x10격자 행렬(area 변수로 지정)을 리스트의 내포기능으로 만들어 줍니다. 그 후 문제에서 요구하는 겹치는 칸의 개수인 count라는 변수를 만들어 줍니다.

# 2.입력받는 순서에 맞게 첫번째 행렬인 (row1,col1), 두번째 행렬인 (row2,col3), color(문제에서 지정한대로 color=1이면 빨간색, color=2이면 파란색을 의미)를 사용자로부터 입력받을 수 있도록 해줍니다.

# 3.행과 열을 이중 for문으로 크게 두가지로 빨간색 행렬일때와 파란색행렬일 때로 나눠줍니다. 그 후 area[row][col](=>리스트의 슬라이싱)가 빈칸일때, 파란색일때, 빨간색일때로 구별해줘서
#   만약 빨간색으로 칠하려는데 이미 파란색이면 보라색, 파란색으로 칠하려는데 빨간색이면 보라색일때의 칸 수를 따로 세어줍니다.

# 4.마지막으로 테스트케이스의 t와 보라색인 부분을 세어준 count를 출력하면 끝입니다.