"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

# --------------------------------------------------------------------

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

# --------------------------------------------------------------------

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist")

# --------------------------------------------------------------------

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)
        return visited

# --------------------------------------------------------------------

    def dft(self, starting_vertex):
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                for next_vert in self.vertices[v]:
                    stack.push(next_vert)
        return visited

# --------------------------------------------------------------------

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for child_vert in self.vertices[starting_vertex]:
                self.dft_recursive(child_vert, visited)
        
        
# --------------------------------------------------------------------

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                if node == destination_vertex:
                    return path    
                visited.add(node)
                for next_node in self.vertices[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    queue.enqueue(new_path)
        return None

# --------------------------------------------------------------------

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            path = stack.pop()
            node = path[-1]
            if node not in visited:
                if node == destination_vertex:
                    return path
                visited.add(node)
                for next_node in self.vertices[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    stack.push(new_path)
        return None

# --------------------------------------------------------------------

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print('DFT',graph.dft(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # print('BFT', graph.bft(1))

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print('BFS',graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print('DFS',graph.dfs(1, 6))
