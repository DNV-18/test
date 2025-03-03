import heapq


def Dijkstra(Graph, start):
    # Graph为字典存储的邻接表
    # shortest_paths记录到每个点到最短距离
    shortest_paths = {node: float('inf') for node in Graph}
    shortest_paths[start] = 0
    small_heap = [(start, 0)]  # 用优先队列（最小堆）处理到每个点的距离
    while small_heap:
        current_node, current_distance = heapq.heappop(small_heap)
        # 不会出现小于的情况，每次出队都是当前最小的值，理想状态下每次出去都是确定的点
        if current_distance > shortest_paths[current_node]:
            continue
        for neighbor, weight in Graph[current_node]:  # 确实一个点后更新通过这个点到达其他邻点的距离
            if shortest_paths[neighbor] > current_distance + weight:
                shortest_paths[neighbor] = current_distance + weight  # 更新最短路径
                heapq.heappush(small_heap, (neighbor, current_distance + weight))  # 加入待处理队列
    return shortest_paths


print("1main")
