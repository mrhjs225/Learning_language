class C1:
    def m(self):
        return "parent"
class C2(C1):
    def m(self):
        return "child"
    def m2(self):
        return "child2"
    # pass ## 메소드가 존재하지 않는 클래스를 표시할때 이렇게 표시함
class C3(C2):
    def m(self):
        return super().m2()+" second child"
o = C2()
print(o.m())
o2 = C3()
print(o2.m())