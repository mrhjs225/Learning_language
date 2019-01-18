class C(object):
    def __init__(self, v) :
        self.value = v
    def show(self) :
        print(self.value)
    def setValue(self, v) :
        self.value = v
    def getValue(self) :
        return self.value
c1 = C(10)
print(c1.value)
c1.value=20
print(c1.value)
c1.show()
c1.setValue(55)
print(c1.getValue())


class D(object) :
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
    def setValue(self, v):
        self.__value = v
d1 = D(100)
# print(d1.__value) # can't access
d1.show()
d1.setValue(555)
d1.show()