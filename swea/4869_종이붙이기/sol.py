import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def function(N):
    if N%10 == 0:
        if N == 10: # N = 10일때 1반환
            return 1
        elif N == 20: # 20x20일 때 3반환
            return 3
        else:
            return function(N-10) + (2*function(N-20))
        
    else:
        print("10의 배수만 입력하세요.")

for t in range(1, T+1):
    N = int(input())
    count = function(N)
    print("#{} {}".format(t,count))


# 이 문제를 풀기위해서 먼저 패턴을 유의깊게 봐야합니다.
# N을 밑변의 길이라고 두고 그림을 그려보면
# N=10인 경우인 20x10 F(1)=1
# N=20인 경우인 20x20 F(2)=3
# N=30인 20x30은 문제에서 나와있는데로 F(3)=5
# N=40인 20x40은 F(4)=11 (일일히 그림을 그려봤을때)
# N=50인 20x50인 F(5)=21
# ...
# N=70인 20x60인 문제에서 나와있는데로 F(7)=85
# ...
# 여기서 입력받는 값을 10의 배수라고 하였지만 기타 10의 배수값이 아닌 경우를 
# 따로 처리하라는 말이 없었으므로 임의로 "10의 배수로 입력하세요"라는 문구를 넣었다.

# a_1값이 10일때는 1을 반환
# a_2값이 20일때는 3을 반환해준다.(why? 초기값이 F(1)=1, F(2)=3이니까)
# 그 다음 재귀함수를 적용해서 피보나치 수열처럼 그 다음의 수열을 만들어나가게 한다. 