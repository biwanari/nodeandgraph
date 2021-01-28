import Dot

class AdjMatrix:

    def __init__(self, row, cols):
        self.matrix = [ [None for i in range(row)] for j in range(cols) ]
        self.row = row
        self.cols = cols

    def __str__(self):
        return str(self.matrix)

    def setNode(self, node: Dot, x,y):
        if x <= self.row and y <= self.cols:
            if self.matrix[x][y] == None:
                self.matrix[x][y] = node.getData()
            else: 
                return 'Node not void, choose another cell'

    def getNode():
        pass
if __name__ == "__main__":
    #d1 = Dot.Node(101)
    #matrix = AdjMatrix(3,10)
    #print(matrix)
    #matrix.setNode(d1, 1,1)
    #print(matrix)
    pass