import sys
from math import sin, cos, acos, pi
import time
from heapq import heappush, heappop, heapify

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2
   if y1 == y2 and x1 == x2:
       return 0

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

data_struct_time = 0
start = time.perf_counter()

with open('rrNodeCity.txt') as f:
    city_id = dict()
    for line in f:
        id = line[:7]
        city_name = line[8:len(line)-1]
        city_id[city_name] = id

with open('rrEdges.txt') as f:
    edge_list = [line.split() for line in f]

with open('rrNodes.txt') as f:
    nodes_location = {line.split()[0] : (float(line.split()[1]), float(line.split()[2])) for line in f}
    id_set = {line.split()[0] for line in f}

with open('rrNodes.txt') as f:
    id_set = {line.split()[0] for line in f}

routes = dict()

for node in id_set:
    routes[node] = set()
for edge in edge_list:
    distance = calcd(nodes_location[edge[0]], nodes_location[edge[1]])
    routes[edge[0]].add((edge[1], distance))
    routes[edge[1]].add((edge[0], distance))

end = time.perf_counter()
data_struct_time = end - start
end, start = 0, 0

# SEARCH 
def get_children(node):
    return routes[node]

def dijkstra(start, end):
    start = city_id[start]
    end = city_id[end]
    closed = set()
    fringe = []
    heappush(fringe, (0, start))
    while fringe:
        v = heappop(fringe)
        if v[1] == end: # current node matches end node (id)
            return v[0]
        if v[1] not in closed: # if id not visited
            closed.add(v[1])  
            for c in get_children(v[1]): # c is (node, distance)
                temp = (v[0] + c[1], c[0]) # temp is (current dist + distance, node)
                heappush(fringe, temp)
    return None

def a_star(start, end):
    start = city_id[start]
    end = city_id[end]
    closed = set()
    fringe = []
    heappush(fringe, (calcd(nodes_location[start], nodes_location[end]), 0, start))
    while fringe:
        v = heappop(fringe)
        if v[2] == end:
            return v[1]
        if v[2] not in closed:
            closed.add(v[2])
            for c in get_children(v[2]):
                temp = (calcd(nodes_location[c[0]], nodes_location[end]) + v[1] + c[1], v[1] + c[1], c[0])
                heappush(fringe, temp)
    return None

print(f"Time to create data structure: {data_struct_time} seconds")
start = time.perf_counter() 
d = dijkstra(sys.argv[1], sys.argv[2])
end = time.perf_counter()
print(f"{sys.argv[1]} to {sys.argv[2]} with Dijkstra: {d} in {end - start} seconds")
end, start, d = 0, 0, 0
start = time.perf_counter()
d = a_star(sys.argv[1], sys.argv[2])
end = time.perf_counter()
print(f"{sys.argv[1]} to {sys.argv[2]} with A*: {d} in {end - start} seconds")
end, start, d = 0, 0, 0