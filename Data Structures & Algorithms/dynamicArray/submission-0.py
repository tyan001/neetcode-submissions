class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.myArr = [0] * capacity
        self.length = 0  

    def get(self, i: int) -> int:
        return self.myArr[i]

    def set(self, i: int, n: int) -> None:
        self.myArr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()

        self.myArr[self.length] = n
        self.length +=1

        print("Empty list")

    def popback(self) -> int:
        if self.myArr != None:
            lastVal = self.myArr[self.length-1]
            self.length -= 1
            return lastVal
        
        return -1

    def resize(self) -> None:
        if self.myArr != None:
            temp = [0] * (2*self.length)
            self.capacity = self.capacity * 2
            for i in range(self.length):
                temp[i] = self.myArr[i]
            self.myArr = temp

    def getSize(self) -> int:
        return self.length 
    
    def getCapacity(self) -> int:
        return self.capacity 