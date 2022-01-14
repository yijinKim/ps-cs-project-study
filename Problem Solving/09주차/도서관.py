import sys
input = sys.stdin.readline
import heapq

N, M = map(int ,input().split())
books = list(map(int ,input().split()))

largest = max(max(books), -min(books))
pos_heap, neg_heap = [], []
for book in books:
    if book >= 0:
        heapq.heappush(pos_heap, -book)
    else:
        heapq.heappush(neg_heap, book)

distance = 0

while pos_heap:
    distance += heapq.heappop(pos_heap)
    for _ in range(M-1):
        if pos_heap:
            heapq.heappop(pos_heap)
while neg_heap:
    distance += heapq.heappop(neg_heap)
    for _ in range(M-1):
        if neg_heap:
            heapq.heappop(neg_heap)

print(-distance * 2 - largest)