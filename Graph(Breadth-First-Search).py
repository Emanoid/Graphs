###############################################################################
# STACK IMPLEMENTATION
import array as array
import ctypes as c

class MyList:
    def __init__(self):
        self._capacity = 10
        self._length = 0
        self._elements = (self._capacity * c.py_object)()
        for i in range(self._capacity):
            self._elements[i] = 0
    
    def get_cap(self):
        return self._capacity

    def _len_(self):
        return self._length

    def get_elem(self):
        return self._elements

    def _getitem_(self,index):
        return self._elements[index]

    def append(self, item):
        if self._length <= self._capacity-1:
            self._elements[self._length] = item
            self._length += 1 
        else:
            temp = (self._capacity * c.py_object)()
            len = 0
            for i in range(self._length):
                temp[i] = self._elements[i]
                len += 1
            self._capacity += 10
            self._elements = (self._capacity * c.py_object)()
            for i in range(self._capacity):
                self._elements[i] = 0
            for i in range(len):
                self._elements[i] = temp[i]
            self._elements[self._length] = item
            self._length += 1

    def remove(self, item):
        temp = (self._length * c.py_object)()
        for i in range(self._length):
            temp[i] = self._elements[i]
        bindex = 0
        for i in range(self._length):
            if temp[i] == item:
                bindex = 0 + i
        ntemp1 = ((self._length-1) * c.py_object)()
        ntemp = self.removehelper(ntemp1,temp,bindex,self._length)
        for i in range(self._capacity):
                self._elements[i] = 0
        for i in range(self._length-1):
            self._elements[i] = ntemp[i]
        self._length -= 1   

    def removehelper(self,l1,l2,bi,len):
        i = 0
        b = 0
        while i <= len-2:
            if i != bi:
                l1[i] = l2[b]
                i = i + 1
                b = b + 1
                #print(i)
            elif i == bi:
                b = b + 1
                l1[i] = l2[b]
                #print(b)
                i = i + 1
                b = b + 1
        return l1                 
    
    def print_elements(self):
        print(self._elements[0:self._length])

class Queue:

    def __init__(self):
        LIST = MyList()
        self._items = LIST
    
    def isEmpty(self):
        return self._items._len_() == 0

    def push(self, data):
        self._items.append(data)

    def pop(self):
        item = self._items._getitem_(0)
        self._items.remove(item)
        return item

    def top(self):
        return self._items._getitem_(0)

    def _len_(self):
        return self._items._len_()

    def print(self):
        i = 0
        while i <= self._len_()-1:
            print(self._items._getitem_(i))
            i = i + 1
'''
MyQueue = Queue()
#print(MyQueue.isEmpty())
for i in range(2):
    MyQueue.push(i+1)
#print(MyQueue.isEmpty())
#MyQueue.push(16)
MyQueue.pop()
#print(MyQueue.pop())
#print(MyQueue.top())
#print(MyQueue._len_())
MyQueue.print()
'''
############################################################################
class Graph:
    def __init__(self):
        self._graph = {}
        self._nodes = self._graph.keys()

    def getnodes(self):
        return list(self._nodes)

    def plot(self,node,edge):
        self._graph[node] = edge

    def remove(self,node):
        self._graph.pop(node)

    def changenodename(self,name,newname):
        self._graph[newname] = self._graph[name]
        self._graph.pop(name)

    def changeedge(self,node,edge):
        self._graph[node] = edge

    def bfp(self):
        visited = []
        queue = Queue()
        data = self.getnodes()[0]
        print(data)
        visited.append(data)
        queue.push(data)
        self.pep(data,visited,queue)

    def pep(self,data,visited,queue):
        for i in self._graph[data]:
            if i not in visited:
                print(i)
                visited.append(i)
                queue.push(i)
                if i ==  self._graph[data][len(self._graph[data])-1]:
                    queue.pop()
                    if queue.isEmpty() == False:
                        self.pep(queue.top(),visited,queue)
            else:
                if i ==  self._graph[data][len(self._graph[data])-1]: 
                    queue.pop()
                    if queue.isEmpty() == False:
                        self.pep(queue.top(),visited,queue)

    def bfs(self,key):
        if key in self.getnodes():
            return True
        else:
            return False

    def findpath(self,start,end):
        visited = []
        LIST = []
        queue =  Queue()
        LIST.append(start)
        visited.append(start)
        queue.push(start)
        if start == end:
            print(LIST)
        else:
            self.bfsfp(start,end,LIST,visited,queue)

    def bfsfp(self,start,end,LIST,visited,queue):
        for i in self._graph[start]:
            if i not in visited:
                LIST.append(i)
                visited.append(i)
                queue.push(i)
                if i == end:
                    print(LIST)
                if i == self._graph[start][len(self._graph[start])-1]:
                    queue.pop()
                    if queue.isEmpty() == False:
                        self.bfsfp(queue.top(),end,LIST,visited,queue)
            else:
                if i == self._graph[start][len(self._graph[start])-1]:
                    queue.pop()
                    if queue.isEmpty() == False:
                        self.bfsfp(queue.top(),end,LIST,visited,queue)

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
graph.plot('A',['B','C','D'])
graph.plot('B',['C','D','H'])
graph.plot('C',['F','D'])
graph.plot('D',['E'])
graph.plot('F',['A'])
graph.plot('E',['F'])
graph.plot('H',[])
#graph.breadthfirstprint('A')
#print(graph.breadthfirstsearch('H'))
#graph.bfp()
#print(graph.bfs('L'))
graph.findpath('A','F')
graph.findpath1('A','F')







