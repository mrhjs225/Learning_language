while False :
    print("hello world!")
i = 0
while i < 5 :
    print("hello world!")
    i +=1
    if (i > 4) :
        break
gugu = [1,2,3,4,5,6,7,8,9]
i = 0
j = 0
while i < 9 :
    j = 0
    while j < 9 :
        print(i+1,"x",j+1,"=",gugu[i]*gugu[j])
        print(str(i+1)+"x"+str(j+1)+"="+str(gugu[i]*gugu[j]))
        j+=1
    i+=1
print("the end")

members=["js", "citron", "someone"]
i = 0
while i < len(members) :
    print(members[i])
    i += 1
for member in members:
    print(member)
i = 0
for i in range(1,10):
    print(i)

input = "one1"
database = ["one", "two", "three", "four"]
if input in database :
    print("input is existed in the database")
else :
    print("input isn't existed in the database")