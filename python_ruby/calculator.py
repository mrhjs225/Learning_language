class Cal(object):
    def __init__(self, v1, v2): #관습적으로 self라는 이름을 씀
        if isinstance(v1, int):
            self.v1 = v1
        else:
            print("parameter1 isn't Integer.")
        if isinstance(v2, int):
            self.v2 = v2
        else:
            print("parameter2 isn't Integer")
    def add(self):
        return self.v1 + self.v2
    def subtract(self):
        return self.v1 - self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30, 20)
print(c2.add())
print(c2.subtract())
print(Cal(50,50).add())
c3 = Cal("one", 55)
c2.setV1("one")
print(c2.getV1())