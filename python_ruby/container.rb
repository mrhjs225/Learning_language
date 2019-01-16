puts("hello".class)
puts(2.class)
puts(3.2.class)
vars=["one", "two", "three"]
puts(vars.class)
puts(vars)
puts(vars[1])
vars[1] = "actually one"
puts(vars)
human = ["name", "addr", 26, false]
puts(human)
puts(human[2])
human[3] = 3
puts(human)

if human.include?("addr")
    puts("human has address")
else
    puts("human hasn't address")
end
puts(human.first)