import tkinter as tk
import sys
from math import sin, cos, acos, pi
import time
from heapq import heappush, heappop, heapify

def calcd(node1, node2):
   y1, x1 = node1
   y2, x2 = node2
   if y1 == y2 and x1 == x2:
       return 0

   R   = 3958.76
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

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
lines = dict()
latitude_multiplier = -15
longitude_multiplier = 15
def create_grid(c):
    for edge1, edge2 in edge_list:
        line = c.create_line([(nodes_location[edge1][1]*longitude_multiplier+2050, nodes_location[edge1][0]*latitude_multiplier+950), (nodes_location[edge2][1]*longitude_multiplier+2050, nodes_location[edge2][0]*latitude_multiplier+950)], tag='grid_line')
        lines[(edge1, edge2)] = line

root = tk.Tk()

canvas = tk.Canvas(root, height=800, width=1200, bg='white')
create_grid(canvas)
canvas.pack(expand=True)


def get_children(node):
    return routes[node]

def dijkstra(start, end):
    start = city_id[start]
    end = city_id[end]
    closed = set()
    fringe = []
    lines_to_update = []
    count = 1
    heappush(fringe, (0, start, (start, )))
    while fringe:
        v = heappop(fringe)
        if v[1] == end: # current node matches end node (id)
            return v
        if v[1] not in closed: # if id not visited
            closed.add(v[1])  
            for c in get_children(v[1]): # c is (node, distance)
                temp = (v[0] + c[1], c[0], v[2] + (c[0], )) # temp is (current dist + distance, node)
                if (v[1], c[0]) in lines.keys():
                    canvas.itemconfig(lines[(v[1], c[0])], fill="red")
                    count += 1
                else:
                    canvas.itemconfig(lines[(c[0], v[1])], fill="red")
                    count += 1
                heappush(fringe, temp)
        if count % 1000 == 0:
            root.update()
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

# print(f"Time to create data structure: {data_struct_time} seconds")
# start = time.perf_counter() 
d = dijkstra(sys.argv[1], sys.argv[2])
path = d[2]
for count in range(1, len(path)):
    if (path[count-1], path[count]) in lines.keys():
        canvas.itemconfig(lines[(path[count-1], path[count])], fill="green", width=3)
    else:
        canvas.itemconfig(lines[(path[count], path[count-1])], fill="green", width=3)
    root.update()

root.mainloop()