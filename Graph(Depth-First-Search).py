class Graph:
    def __init__(self):
        self._graph = {}
        self._nodes = self._graph.keys()

    def getnodes(self):
        return list(self._nodes)
        
    def getgraph(self):
        return self._graph

    def plot(self,node,edge):
        self._graph[node] = edge

    def remove(self,node):
        self._graph.pop(node)

    def changenodename(self,name,newname):
        self._graph[newname] = self._graph[name]
        self._graph.pop(name)

    def changeedge(self,node,edge):
        self._graph[node] = edge

    def dfp(self,data,visited):
        if data not in visited:
            print(data)
            visited.append(data)
            for i in self._graph[data]:
                self.dfp(i,visited)

    def dfs(self,key):
        if key in self.getnodes():
            return True
        else:
            return False

    def findpath(self,start,end,visited,LIST):
        if start not in visited:
            LIST.append(start)
            if start == end:
                print(LIST)
            visited.append(start)
            for i in self._graph[start]:
                self.findpath(i,end,visited,LIST)

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
graph.plot('B',['D','A','H'])
graph.plot('C',['D'])
graph.plot('D',['E'])
graph.plot('E',['F'])
graph.plot('F',['A'])
graph.plot('H',[])
graph.findpath('A','H',[],[])
graph.findpath1('A','H')
#graph.dfp('A',[])
#print(graph.dfs('L'))










