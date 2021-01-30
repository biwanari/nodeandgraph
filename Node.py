class Node:


    def __init__(self, name, data = None):
        self.name =  name
        self._data = data


    def __str__(self):
        return f"Node id = {self.name} \n << Node Content --> {self._data} >> \n << datatype : {type(self._data)} >>"


    def getName(self):
        return self.name
    def getData(self):
        return str(self._data)

    def getTypofdata(self):
        return type(self._data)

    def setData(self, newData):
        self._data = newData