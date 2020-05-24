from math import inf
from heapq import heappop, heappush

def a_star(graph, start, target):
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]

  paths_and_distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < paths_and_distances[neighbor]:
        paths_and_distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))

  return paths_and_distances
