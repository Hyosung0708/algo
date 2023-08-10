import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    import heapq
    heapq.heapify(numbers)

    heap = [0] * (N+1)
    heap_size = 0

    for i in range(N):
        heap_size += 1
        # 맨 마지막 노드에 삽입하려는 데이터를 할당
        heap[heap_size] = numbers[i]

        child_idx = heap_size
        parent_idx = child_idx // 2

        # 힙의 조건에 맞도록 교환 반복
        while parent_idx and heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

            child_idx = parent_idx
            parent_idx = child_idx // 2

    node = N // 2
    total = 0

    # 조상에 조상에 조상을 찾다가 루트를 찾을 때 까지 반복
    while node:
        total += heap[node]
        node //= 2

    print(total)