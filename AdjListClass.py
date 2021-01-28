from Dot import *
class AdjList:

    def __init__(self):
        self.adj_list = dict()

    

    def setNode(self, node):
        self.adj_list[node.getName()] = set()




    def printGraph(self):
        for k, v in self.adj_list.items():
            print(k ,v)

if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D', [1,2,3,4,5,6])
    G = AdjList()
    G.setNode(a)
    G.setNode(b)
    G.printGraph()