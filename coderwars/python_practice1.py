print((80+75+55)/3)
a = 3
if a % 2 == 1:
    print("odd")
else:
    print("even")

num="881120-1068234"
num_array=num.split("-")
print(num_array[0])
print(num_array[1])
print(num_array[1][0])

problem3 = "a:b:c:d"
print(problem3.replace(":", "#"))

problem4 = problem3.split(":")
answer4 = "#".join(problem4)
print(answer4)

list_p1 = ["Life", "is", "too", "short"]
list_a1 = " ".join(list_p1)
print(list_a1)
list_p1 = [1,3,5,4,2]
print(list_p1)
list_p1.sort()
list_p1.reverse()
print(list_p1)

tuple1 = (1,2,3)
tuple2 = (4,)
print(tuple1+tuple2)
a = {}
print(a)
a[3] = "hello"
print(a)
a[3] = "who?"
print(a)
print(a.keys())
a["name"]="gildong"
print(a)
a.clear()
a[("1",)]="python"
print(a)
s1 = set([1,3,5,7,19])
print(s1)
s2 = set([3,6,7,444])
print(s2)
print(s1&s2)
a = [1,1,1,2,2,3,3,3,4,4,5]
print(a)
s3 = set(a)
print(s3)
a = {"1","2"}
print(type(a))
a = {}
print(type(a))
a=set()
print(type(a))
print(a)
# input1 = input("first")
# input2 = input("second")
# total = int(input1)+int(input2)
# print(total)
print("you", "need","python")
f = open("C:/Users/mrhjs/Desktop/Programming/Learn/coderwars/helloword.txt", "w")
f.write("hello writing world!")
f.close()
f2 = open("abc.txt", "w")
f2.write("aaa\nbbb\nccc\nddd\n")
f2.close()
f3 = open("abc.txt", "r")
line = f3.readlines()
print(line)
line.reverse()
print(line)
f3.close()
f3 = open("abc.txt", "w")
print(len(line))
for i in range(0,len(line)):
    f3.write(line[i])
    i+=1
f3.close()
