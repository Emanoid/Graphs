class Graph:
    #A Graph is:
    #   A dictionary of Nodes
    #A Node
    #   A int/string &
    #   A list

    def __init__(self):
        self._graph = {}
        self._nodes = self._graph.keys()

    def plot(self,node,edge):
        self._graph[node] = edge

    def remove(self,node):
        self._graph.pop(node)

    def change_node(self,node,newnode):
        temp_edge = self._graph[node]
        self.remove(node)
        self._graph[newnode] = temp_edge

    def change_edge(self,node,newedge):
        self._graph[node] = newedge

    def print(self):
        print(self._graph)

    def findpath1(self,start,end):
        path = []
        visited = []
        if start == end:
            path.append(start)
            print(path)
        else:
            return self.find_path(start,end,path,visited)

    def find_path(self,start,end,path,visited):
        path.append(start)
        if start in self._nodes:
            visited.append(start)
            children = self._graph[start]
            if end in children:
                path.append(end)
                print(path)
            else:
                for i in children:
                    if i not in visited:
                        return self.find_path(i,end,path,visited)

                    
graph = Graph()
graph.plot('A',['B','C'])
graph.plot('B',['C','D'])
graph.plot('C',['D'])
graph.plot('D',['E'])
graph.plot('E',['F'])
graph.plot('F',['A'])
#graph.remove('D')
#graph.change_node('C','G')
#graph.change_edge('A',['B','D'])
#graph.change_edge('A',['B','D'])
#graph.print()
#print(graph.getnodes())
graph.findpath('A','D')







