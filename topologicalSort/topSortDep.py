#time complexity O( j + d )
#space complexity O( j + d )
def topologicalSort(jobs, deps):
    graph = createGraph(jobs , deps)
    return ordered(graph)

def createGraph(jobs , deps):
    graph = Graph(jobs)
    for job , dep in deps:
        graph.addDep(job , dep)
    return graph 

def ordered(graph):
    order = []
    l = list(filter(lambda node: node.numOfDeps == 0, graph.nodes))
    while(len(l)):
        node = l.pop()
        order.append(node.job)
        removeDeps(node , l)
    edges = any(node.numOfDeps for node in graph.nodes)
    return [] if edges else order

def removeDeps(node , l):
        while(len(node.deps)):
            dep = node.deps.pop()
            dep.numOfDeps -=1
            if(dep.numOfDeps == 0):
                l.append(dep)

class Graph:
    def __init__(self , jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addDep(self , job , dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.numOfDeps += 1

    def addNode(self , job):
        self.graph[job] = Node(job)
        self.nodes.append(self.graph[job])

    def getNode(self , job):
        if(job not in self.graph):
            self.addNode(job)
        return self.graph[job]
        
        
            
class Node:
    def __init__(self , job):
        self.job = job
        self.deps = []
        self.numOfDeps = 0