# 14 min
import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        if "I" in operation:
            _, value = operation.split("I ")
            value = int(value)
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
        elif len(min_heap) and len(max_heap):
            _, value = operation.split("D ")
            value = int(value)
            if value < 0:
                poped = heapq.heappop(min_heap)
                if -poped in max_heap:
                    max_heap.remove(-poped)
            else:
                poped = heapq.heappop(max_heap)
                if -poped in min_heap:
                    min_heap.remove(-poped)

        # print(min_heap)
        # print(max_heap)
        # print("----------------")

    if len(min_heap):
        return [max(min_heap), min(min_heap)]
    else:
        return [0, 0]

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	)
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	)