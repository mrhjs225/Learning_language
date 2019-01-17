def test()
    puts("aaa")
end
test()

def cal()
    a = 3
    b = 4
    return a + b
end
puts(cal())

def caltwo(a, b)
    return a+b
end
puts(caltwo(2,3))

def printgugu(i, j)
    puts(i.to_s+"x"+j.to_s()+"="+(i*j).to_s())
end

puts("what kind of dan do you wnat?")
# i = gets.chomp()
i = 3
j = 1

for j in (1..9) do
    printgugu(i.to_i(), j)
end

def printsim
    puts("simple print")
end

printsim

puts "hello new world"

def test a, b, c
    puts(a+b*c)
end

test 1, 3, 4 # like lisp

def test2 a, b, c
    a = 1
    b = 2
    c = 3
    a + b
    c = 70
end

print(test2 1, 2, 3)