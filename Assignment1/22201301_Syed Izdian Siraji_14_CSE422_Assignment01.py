import heapq 

def A_star(graph,heuristic,start,dest):
    pqueue=[]
    traversed = {}
    visited = []
    heapq.heappush(pqueue,(heuristic[start],start,0,None))
    while pqueue:
        f_n,current,g_n,parent = heapq.heappop(pqueue)
        traversed[current] = parent
        visited.append(current)
        if current == dest:
            path = current
            temp =  traversed[current]
            while temp != None:
               path = temp + '->'+ path
               if temp not in traversed.keys():
                   print("No Path Found")
                   break
               temp = traversed[temp]
               
            print(f'Path: {path}\nTotal distance: {g_n} km')   
            return    

        for ch_node,cost in graph[current].items():
            if ch_node not in visited:
                newf_n = g_n + heuristic[ch_node] + cost
                new_g_n = g_n + cost
                heapq.heappush(pqueue,(newf_n,ch_node,new_g_n,current))

with open('Input file.txt','r') as fil:
    graph = {}
    heuristic = {}
    fil = fil.readlines()
    for i in fil:
        new_fil = i.strip().split()
        heuristic[new_fil[0]] = int(new_fil[1])
        graph[new_fil[0]] = {}
        
        for e in range(2,len(new_fil),2):
            graph[new_fil[0]][new_fil[e]] = int(new_fil[e+1])
  
A_star(graph,heuristic,'Arad','Bucharest')         
