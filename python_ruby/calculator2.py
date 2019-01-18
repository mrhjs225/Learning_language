class Cal(object):
    def __init__(self, v1, v2):
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

class CalMul(Cal):
    def multiply(self):
        return self.v1*self.v2
c1 = CalMul(10, 55)
print(c1.add())
print(c1.subtract())
print(c1.multiply())