from grid import Grid
from arrays import Array


class Cube():
    
    def __init__(self, rows, columns, high, fill_value=None) -> None:
        self.data = Grid(rows,columns)
        for row in range(rows):
            for column in range(columns):
                self.data[row][column] = Array(columns,fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def get_long(self):
        return len(self.data[0][0])

    def fill(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for l in range(self.get_long()):
                    self[row][col][l] = row*col*l

    def __getitem__(self,index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += "["
                for l in range(self.get_long()):
                    result += str(self.data[row][col][l]) + " "
                result += "]"

            result += "\n"

        return str(result)
