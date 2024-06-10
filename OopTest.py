class testClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def printValues(self):
        print(self.a,self.b)

test = testClass(1,2)
test.printValues()
newTest = testClass(1,2)
test.b = 3
newTest.printValues()
