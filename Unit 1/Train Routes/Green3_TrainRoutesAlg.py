import sys
from math import sin, cos, acos, pi
import time

# HELPER
def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

# BASE
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

print(routes)

# for node in id_set: 
#     s1 = time.perf_counter()
#     reachable = set()
#     for edge in edge_list:
#         if edge[0] == node:
#             reachable.add((edge[1], calcd(nodes_location[edge[0]], nodes_location[edge[1]])))
#         elif edge[1] == node:
#             reachable.add((edge[0], calcd(nodes_location[edge[0]], nodes_location[edge[1]])))
#     routes[node] = reachable
#     e1 = time.perf_counter()
#     print(f"{e1-s1} seconds for {node} and {reachable}")
end = time.perf_counter()
print(f"{end - start} seconds")
# SEARCH
def dijkstra(start_node):
    return NotImplemented
def a_star(start_node):
    return NotImplemented

