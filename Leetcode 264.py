#Leetcode 264
import heapq


def nthUglyNumber(n):
    heap = [1]
    generated = []

    while len(generated) < n:
        smallest = heapq.heappop(heap)
        if smallest not in generated:
            generated.append(smallest)
            heapq.heappush(heap, smallest * 2)
            heapq.heappush(heap, smallest * 3)
            heapq.heappush(heap, smallest * 5)
    return(generated[n-1])
print(nthUglyNumber(10))