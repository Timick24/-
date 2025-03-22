from os import path


class BinaryTreeNode:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def insert(self, root, data):
        if root is None:
            return BinaryTreeNode(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        
        return root
class BinaryTree:
    def deleteNode(self, root, data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self.deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.deleteNode(root.right, data)
        else:
            if root.left is None and root.right is None: 
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.data = self.getMin(root.right).data
                root.right = self.deleteNode(root.right, root.data)

        return root
    
    def getMin(self, root):
        if root is None:
            return root
        
        while root.left is not None:
            root = root.left

        return root
    
class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = []

class Graph:
    def __init__(self):
        self.vertices = []
    def add_vertex(self, vertex_data):
        vertex = Vertex(vertex_data)
        self.vertices.append(vertex)
        return vertex
    
    def add_edge(self, src, dest):
        src = self.find_vertex(src)
        dest = self.find_vertex(dest)
        src.adjacent.appened(dest)

def topological_sort(self):
    indegrees = {v: 0 for v in self.vertices}

    for vertex in self.vertices:
        for neighbor in vertex.adjacent:
            indegrees[neighbor] += 1
    
    sorted_vertices = []

    for vertex in self.vertices:
        if indegrees[vertex] == 0:
            self.topogical_sort_util(vertex, sorted_vertices)
    
    return sorted_vertices

def topogical_sort_util(self, vertex, sorted_vetices):
    for neighbor in vertex.adjacent:
        idegrees[neighbor] -= 1 
        if idegrees[neighbor] == 0:
            self.topogical_sort_util(neighbor, sorted_vetices)
    sorted_vetices.appened(vertex)

def find_path(self, start, end):
    visited = set()
    path = []

    def dfs(vertex):
        visited.add(vertex)
        if vertex == end:
            return True
        
        for neighbor in vertex.adjacent:
            if neighbor not in visited:
                if dfs(neighbor):
                    path.append(vertex.data)
                    return True
        return False
    dfs(start)
return path in path else None