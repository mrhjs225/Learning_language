class Cal(object):
    _history = []
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
        result = self.v1 + self.v2
        Cal._history.append("add : %d+%d=%d" %(self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1 - self.v2
        Cal._history.append("subtract : %d-%d=%d" %(self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)
            
class CalMul(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("multiply : %d*%d=%d" %(self.v1, self.v2, result))
        return result
    def info(self):
        print("CalMul => %s" % (super().info()))
c1 = CalMul(10, 55)
print(c1.add())
print(c1.subtract())
print(c1.multiply())
Cal.history()

num1 = 4
num2 = 3
print("hello world %d" % (num1))

c2 = Cal(20, 30)
print(c2.info())
c1.info()