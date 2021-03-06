from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
  """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
  ### TODO
  def helper(visited, frontier):
    if len(frontier) == 0:
      return visited

    else:
      distance, edges, node = heappop(frontier)
      if node in visited:
        return helper(visited, frontier)

      else:
        visited[node] = (distance, edges)

        for neighbor, weight in graph[node]:
          heappush(frontier, (distance+weight, edges+1, neighbor))
        return helper(visited, frontier)

  frontier = []
  heappush(frontier,(0, 0, source))
  visited = dict()
  return helper(visited, frontier)
          


  
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
  ###TODO
  def bfs_helper(visited, frontier, parent):
    if len(frontier) == 0:
      return parent
    else:
      node = frontier.popleft()
      visited.add(node)
      
      # neighbors = graph[node]
      for i in graph[node]:
        if i not in visited and i not in frontier:
          frontier.append(i)
          parent[i] = node
      # frontier.extend(filter(lambda n: n not in visited, graph[node]))
      return bfs_helper(visited, frontier, parent)
  frontier = deque()
  frontier.append(source)
  visited = set()
  parent = dict()
  return bfs_helper(visited, frontier, parent)
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


graph = get_sample_graph()
parents = bfs_path(graph, 's')
print(parents)

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'


    
def get_path(parents, destination):
  """
     Returns:
       The shortest path from the source node to this destination node 
       (excluding the destination node itself). See test_get_path for an example.
     """
  ###TODO
  path = '' 
  def get_path_helper(parents, destination, path):
      if destination in parents:
          destination = parents[destination]
          return get_path_helper(parents, destination, destination+path)
      else:
          return path
  return get_path_helper(parents, destination, path)
        
    
  #   if len(frontier) == 0:
  #     return path
  #   else:
  #     node = frontier.popleft()
  #     parent = parents[node]
  #     visited.add(node)
      
      
  #     path = parent 
  #     print(path)
  #     for i in parents:
  #       if i not in visited and i not in frontier:
  #         frontier.append(i)
  #         #path = parent 
  #     return get_path_helper(visited, frontier)

  # return get_path_helper(visited, frontier)

  


    
print(get_path(parents, 'd'))

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'

  
graph = {
              's': {('a', 1), ('c', 4)},
              'a': {('b', 2)}, # 'a': {'b'},
              'b': {('c', 1), ('d', 4)}, 
              'c': {('d', 3)},
              'd': {},
              'e': {('d', 0)}
            }

