class AdjList:

    def __init__(self):
        self.adj_list = dict()

    def setNode(self, node):
        self.adj_list[node.getName()] = set()

    def printGraph(self):
        for k, v in self.adj_list.items():
            print(k ,v)


    def randomInitialize(self):
        pass