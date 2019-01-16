print(type("something"))
var = "sea"
print(type(var))
var = 5
print(type(var))
print(type(4/3))

print(type(["one", "two", "three"]))
vars = ["one", "two", "three"]
gugu = [1,2,3,4,5,6,7,8,9]
print(vars[1])
vars[1] = "actually one"
print(vars)

human = ["name", "addr", 25, False] # 여러개의 유형을 쓸 수 있음..
print(human)
human[0] = True
print(human)

if "addr" in human :
    print("human has address")
else :
    print("human hasn't address")
human.append(178)
print(human)
print(len(human))
del(human[0], human[2]) # quite tricky
print(human)