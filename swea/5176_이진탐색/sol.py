import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def inorder(idx):
    global count

    if idx <= N:

        # 왼쪽 자식
        inorder(idx*2)

        # 현재 노드
        tree[idx] = count
        count += 1

        # 오른쪽 자식
        inorder(idx*2 + 1)

for tc in range(1, T+1):
    N = int(input())


    tree = [0] * (N+1)

    count = 1

    inorder(1)

    print(tree[1], tree[N//2])














# 문제

# - 1부터 N까지의 자연수를 이진탐색트리에 저장하려고 한다. 
# - 이진탐색트리의 루트 값과, N/2 노드(소수점 버림) 값을 출력하시오. 
#- 트리의 값은 왼쪽 자식노드 < 현재 노드 < 오른쪽 자식노드 를 만족

# 풀이접근

# - 리스트를 이용해 1~N 의 트리를 만듦
# - 제일 왼쪽부터 규칙에 맞게 값을 넣어줌 (재귀함수 활용)

