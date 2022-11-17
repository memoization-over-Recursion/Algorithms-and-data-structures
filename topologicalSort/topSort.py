#time complexity O( j+d )
#space complexity O( j+d )
def topologicalSort(jobs, deps):
    graphForJobs = createGraph(jobs , deps)
    return orderJobs(graphForJobs)

def createGraph(jobs , deps):
    graph = Graph(jobs)
    for prereq , job in deps:
        graph.addPrereq(job , prereq)
    return graph

def orderJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while(len(nodes)):
        node = nodes.pop()
        cycle = depthFirst(node , orderedJobs)
        if cycle:
            return []
    return orderedJobs

def depthFirst(node , ordered):
    if(node.visited):
        return False
    if(node.visiting):
        return True
    node.visiting = True
    for n in node.prereq:
        cycl = depthFirst(n , ordered)
        if(cycl):
            return True
    
    node.visited = True
    node.visiting = False
    ordered.append(node.job)
    return False

class Graph:
    def __init__(self , jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self , job , prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereq.append(prereqNode)

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
        self.prereq = []
        self.visited = False
        self.visiting = False