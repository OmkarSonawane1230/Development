import heapq
goal=(1,2,3,4,5,6,7,8,0)
def h(s):
    d=0
    for i,v in enumerate(s):
        if v==0: continue
        x,y=divmod(i,3);gx,gy=divmod(v-1,3)
        d+=abs(x-gx)+abs(y-gy)
    return d

def neigh(s):
    i=s.index(0);x,y=divmod(i,3);res=[]
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            ni=nx*3+ny;l=list(s)
            l[i],l[ni]=l[ni],l[i];res.append(tuple(l))
    return res
    
def astar(start):
    pq=[(h(start),0,start,[])];vis=set()
    while pq:
        f,g,s,p=heapq.heappop(pq)
        if s in vis: continue
        vis.add(s);p=p+[s]
        if s==goal:
            for x in p: print(x)
            return
        for n in neigh(s):
            heapq.heappush(pq,(g+1+h(n),g+1,n,p))
astar((1,2,3,4,0,6,7,5,8))
