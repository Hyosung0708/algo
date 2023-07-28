import sys
sys.stdin = open('input.txt', encoding='utf-8')


Man1 = input()
Man2 = input()

rcp = ['가위', '바위', '보']

Man1_idx = rcp.index(Man1)
Man2_idx = rcp.index(Man2)

# print(Man1_idx, Man2_idx)

result = Man1_idx - Man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')


# result = {0: 'Man1 Win!', 1: 'Man1 Lose!', 2: 'Man1 Draw!'}
# if Man1 == '가위' and Man2 == '가위':
#     print('Result : Draw')
# elif Man1 == '가위' and Man2 == '바위':
#     print('Result : Man2 Win!')