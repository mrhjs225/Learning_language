def test() :
    print("aaa")
test()

def cal() :
    a = 3
    b = 4
    return a+b
print(cal())

def caltwo(a, b) :
    return a + b
print(caltwo(2, 3))

def printgugu(i, j) :
    print(str(i)+"x"+str(j)+"="+str(i*j))

j = 1
i = input("what kind of dan do you want?\n")
# i=3


for j in range(1,10) :
    printgugu(int(i), j)
