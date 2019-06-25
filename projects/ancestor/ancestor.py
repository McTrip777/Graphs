class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph():
    def __init__(self):
        self.vertices = {}

# --------------------------------------------------------------------

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

# --------------------------------------------------------------------

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].add(v1)   
        else:
            raise IndexError("That vertex doesn't exist")

# --------------------------------------------------------------------

    def earliest_ancestor(self, start):
        stack = Stack()
        stack.push([start])
        visited = set()
        new_path = None
        while stack.size() > 0:
            path = stack.pop()
            node = path[-1]
            if node not in visited:
                visited.add(node)
                for next_node in self.vertices[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    stack.push(new_path)
        if new_path == None:
            return -1
        else:
            return new_path[-1]

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(10)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(4)
    graph.add_vertex(11)
    graph.add_vertex(3)
    graph.add_vertex(5)
    graph.add_vertex(8)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(9)
    graph.add_edge(10, 1)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(4, 5)
    graph.add_edge(4, 8)
    graph.add_edge(11, 8)
    graph.add_edge(8, 9)

print("")
print(graph.earliest_ancestor(5))
print("")
