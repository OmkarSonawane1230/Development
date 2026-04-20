import heapq

g = {
    0: [(1,2),(3,6)],
    1: [(0,2),(2,3),(3,8),(4,5)],
    2: [(1,3),(4,7)],
    3: [(0,6),(1,8),(4,9)],
    4: [(1,5),(2,7),(3,9)]
}

def prim(start):
    vis = set([start])
    pq = [(0,start)]
    cost = 0

    while pq:
        w,u = heapq.heappop(pq)
        if u not in vis:
            vis.add(u)
            cost += w
        for v,wt in g[u]:
            if v not in vis:
                heapq.heappush(pq,(wt,v))

    print("MST cost:", cost)

prim(0)