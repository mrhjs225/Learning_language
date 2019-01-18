class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")

class C2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")

class C3(C2, C1):
    def m(self):
        print("C3 m")
    # pass

o = C3()
o.c1_m()
o.c2_m()
o.m()
print(C3.__mro__)