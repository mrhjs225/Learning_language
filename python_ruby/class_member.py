class Cs:
    @staticmethod
    def static_method():
        print("static method")
    @classmethod
    def class_method(cls):
        print("class method")
    def instance_method(self):
        print("instance method")

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()

class Cs2:
    count = 0
    def __init__(self):
        Cs2.count += 1
    @classmethod
    def getCount(cls):
        return Cs2.count
i1 = Cs2()
print(i1.count)
print(Cs2.getCount())
i2 = Cs2()
print(i2.count)
i3 = Cs2()
print(Cs2.getCount())
