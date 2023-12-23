# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

from __future__ import annotations
# some of these types are deprecated: https://www.python.org/dev/peps/pep-0585/
from typing import Protocol, Iterator, Tuple, TypeVar, Optional
T = TypeVar('T')

Location = TypeVar('Location')
class Graph(Protocol):
    def neighbors(self, id: Location) -> list[Location]: pass

class SimpleGraph:
    def __init__(self):
        self.edges: dict[Location, list[Location]] = {}
    
    def neighbors(self, id: Location) -> list[Location]:
        return self.edges[id]

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': [],
}

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, x: T):
        self.elements.append(x)
    
    def get(self) -> T:
        return self.elements.popleft()

# utility functions for dealing with square grids
def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style):
    r = " . "
    if 'number' in style and id in style['number']: r = " %-2d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = " > "
        if x2 == x1 - 1: r = " < "
        if y2 == y1 + 1: r = " v "
        if y2 == y1 - 1: r = " ^ "
    if 'path' in style and id in style['path']:   r = " @ "
    if 'start' in style and id == style['start']: r = " A "
    if 'goal' in style and id == style['goal']:   r = " Z "
    if id in graph.walls: r = "###"
    return r

def draw_grid(graph, **style):
    print("___" * graph.width)
    for y in range(graph.height):
        for x in range(graph.width):
            print("%s" % draw_tile(graph, (x, y), style), end="")
        print()
    print("~~~" * graph.width)

# data from main article
DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,334,343,344,373,374,403,404,433,434]]

GridLocation = Tuple[int, int]

class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: list[GridLocation] = []
    
    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id: GridLocation) -> bool:
        return id not in self.walls
    
    def neighbors(self, id: GridLocation, lastdir: String) -> Iterator[GridLocation]:
        (x, y) = id
        if lastdir == "E" or lastdir == "W":
          neighbors = [(x, y-1), (x, y-2), (x, y-3), (x, y+1), (x, y+2), (x, y+3)]
#          neighbors = [(x, y+1), (x, y+2), (x, y+3)]
        if lastdir == "N" or lastdir == "S":
          neighbors = [(x-1, y), (x-2, y), (x-3, y), (x+1, y), (x+2, y), (x+3, y)]
#          neighbors = [(x+1, y), (x+2, y), (x+3, y)]
        if lastdir == "X":
          neighbors = [(x, y-1), (x, y-2), (x, y-3), (x, y+1), (x, y+2), (x, y+3), (x-1, y), (x-2, y), (x-3, y), (x+1, y), (x+2, y), (x+3, y)]
#          neighbors = [(x, y+1), (x, y+2), (x, y+3), (x+1, y), (x+2, y), (x+3, y)]

        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

class WeightedGraph(Graph):
    def cost(self, from_id: Location, to_id: Location) -> float: pass

class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.weights: dict[GridLocation, float] = {}
    
    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        weight = 0
        if to_node[0] - from_node[0] > 0:
          for i in range(from_node[0] + 1, to_node[0] + 1):
            weight += self.weights.get((i,to_node[1]), 1)
        elif to_node[0] - from_node[0] < 0:
          for i in range(to_node[0] + 1, from_node[0] + 1):
            weight += self.weights.get((i,to_node[1]), 1)
        elif to_node[1] - from_node[1] > 0:
          for i in range(from_node[1] + 1, to_node[1] + 1):
            weight += self.weights.get((to_node[0],i), 1)
        elif to_node[1] - from_node[1] < 0:
          for i in range(to_node[1] + 1, from_node[1] + 1):
            weight += self.weights.get((to_node[0],i), 1)
        else:
          weight += self.weights.get(to_node, 1)
#        for i in range(from_node[0] + 1, to_node[0] + 1):
#          weight += self.weights.get((i,to_node[1]), 1)
#        for i in range(from_node[1] + 1, to_node[1] + 1):
#          weight += self.weights.get((to_node[0],i), 1)
        return weight
diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]}

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, T, T]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: float, step: T):
        heapq.heappush(self.elements, (priority, item, step))
    
    def get(self) -> list[T, T]:
        item, step = heapq.heappop(self.elements)[1:3]
        return [item, step]

def dijkstra_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0, (0,0))
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far: dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        elements = frontier.get()
        current = elements[0]
        step = elements[1]

        if current == goal:
            break

        if step[0] > 0:
          lastdir = "E"
        elif step[0] < 0:
          lastdir = "W"
        elif step[1] > 0:
          lastdir = "N"
        elif step[1] < 0:
          lastdir = "S"
        else:
          lastdir = "X"
        for next in graph.neighbors(current, lastdir):
#        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                step = (next[0] - current[0], next[1] - current[1])
                frontier.put(next, priority, step)
                came_from[next] = current
    
    return came_from, cost_so_far

# thanks to @m1sp <Jaiden Mispy> for this simpler version of
# reconstruct_path that doesn't have duplicate entries

def reconstruct_path(came_from: dict[Location, Location],
                     start: Location, goal: Location) -> list[Location]:

    current: Location = goal
    path: list[Location] = []
    if goal not in came_from: # no path was found
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

diagram_nopath = GridWithWeights(10, 10)
diagram_nopath.walls = [(5, row) for row in range(10)]

def heuristic(a: GridLocation, b: GridLocation) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0, (0,0))
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[(0,0,'X')] = 0
    
    while not frontier.empty():
        elements = frontier.get()
        current = elements[0]
        step = elements[1]

        if current == goal:
            break

#        if step[0] > 0:
#          lastdir = "E"
#        elif step[0] < 0:
#          lastdir = "W"
#        elif step[1] > 0:
#          lastdir = "N"
#        elif step[1] < 0:
#          lastdir = "S"
        if came_from[current] == None:
          lastdir = "X"
        elif current[0] - came_from[current][0] > 0:
          lastdir = "E"
        elif current[0] - came_from[current][0] < 0:
          lastdir = "W"
        elif current[1] - came_from[current][1] > 0:
          lastdir = "S"
        elif current[1] - came_from[current][1] < 0:
          lastdir = "N"
        else:
          lastdir = "X"
        for next in graph.neighbors(current, lastdir):
#        for next in graph.neighbors(current):
            nextdir = ""
            if next[0] - current[0] > 0:
              nextdir = "E"
            elif next[0] - current[0] < 0:
              nextdir = "W"
            elif next[1] - current[1] > 0:
              nextdir = "S"
            elif next[1] - current[1] < 0:
              nextdir = "N"
            else:
              nextdir = "X"
            cfc_cur = (current[0], current[1], lastdir)
            cfc_nxt = (next[0], next[1], nextdir)
            new_cost = cost_so_far[cfc_cur] + graph.cost(current, next)
            if cfc_nxt not in cost_so_far or new_cost < cost_so_far[cfc_nxt]:
                cost_so_far[cfc_nxt] = new_cost
#                priority = new_cost + heuristic(next, goal)
                priority = new_cost
                step = (next[0] - current[0], next[1] - current[1])
                frontier.put(next, priority, step)
                came_from[next] = current
#                nextdir = ""
#                if next[0] - current[0] > 0:
#                  nextdir = "E"
#                elif next[0] - current[0] < 0:
#                  nextdir = "W"
#                elif next[1] - current[1] > 0:
#                  nextdir = "N"
#                elif next[1] - current[1] < 0:
#                  nextdir = "S"
#                else:
#                  nextdir = "X"
#                for nextest in graph.neighbors(next, nextdir):
#                    new_cost = cost_so_far[next] + graph.cost(next, nextest)
#                    if nextest not in cost_so_far or new_cost < cost_so_far[nextest]:
#                        cost_so_far[nextest] = new_cost
#                        priority = new_cost + heuristic(nextest, goal)
#                        priority = new_cost
#                        step = (nextest[0] - next[0], nextest[1] - next[1])
#                        frontier.put(nextest, priority, step)
#                        came_from[nextest] = next
#                        nextestdir = ""
#                        if nextest[0] - next[0] > 0:
#                          nextestdir = "E"
#                        elif nextest[0] - next[0] < 0:
#                          nextestdir = "W"
#                        elif nextest[1] - next[1] > 0:
#                          nextestdir = "N"
#                        elif nextest[1] - next[1] < 0:
#                          nextestdir = "S"
#                        else:
#                          nextestdir = "X"
#                        for nextestest in graph.neighbors(nextest, nextestdir):
#                            new_cost = cost_so_far[nextest] + graph.cost(nextest, nextestest)
#                            if nextestest not in cost_so_far or new_cost < cost_so_far[nextestest]:
#                                cost_so_far[nextestest] = new_cost
#                                priority = new_cost + heuristic(nextestest, goal)
#                                priority = new_cost
#                                step = (nextestest[0] - nextest[0], nextestest[1] - nextest[1])
#                                frontier.put(nextestest, priority, step)
#                                came_from[nextestest] = nextest
    
    return came_from, cost_so_far

def breadth_first_search(graph: Graph, start: Location, goal: Location):
    frontier = Queue()
    frontier.put(start)
    came_from: dict[Location, Optional[Location]] = {}
    came_from[start] = None
    
    while not frontier.empty():
        current: Location = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from

class SquareGridNeighborOrder(SquareGrid):
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x + dx, y + dy) for (dx, dy) in self.NEIGHBOR_ORDER]
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return list(results)

def test_with_custom_order(neighbor_order):
    if neighbor_order:
        g = SquareGridNeighborOrder(30, 15)
        g.NEIGHBOR_ORDER = neighbor_order
    else:
        g = SquareGrid(30, 15)
    g.walls = DIAGRAM1_WALLS
    start, goal = (8, 7), (27, 2)
    came_from = breadth_first_search(g, start, goal)
    draw_grid(g, path=reconstruct_path(came_from, start=start, goal=goal),
              point_to=came_from, start=start, goal=goal)

class GridWithAdjustedWeights(GridWithWeights):
    def cost(self, from_node, to_node):
        prev_cost = super().cost(from_node, to_node)
        nudge = 0
        (x1, y1) = from_node
        (x2, y2) = to_node
        if (x1 + y1) % 2 == 0 and x2 != x1: nudge = 1
        if (x1 + y1) % 2 == 1 and y2 != y1: nudge = 1
        return prev_cost + 0.001 * nudge
