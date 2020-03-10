class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def push(self, item):
        self.data[self.length]=item
        self.length+=1

    def pop(self):
        lastitem=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastitem

    def delete(self,index):
        deleted_item = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]

        del self.data[self.length-1]
        self.length-=1
        return deleted_item


arr = MyArray()
arr.push(5)
print(arr)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
print(arr)
arr.delete(3)
print(arr)