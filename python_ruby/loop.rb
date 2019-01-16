while false do
    puts("hello world!")
end
i = 0
while i < 5 do
    if i % 2 == 0
        puts(i)
        puts("hello world!")
    end
    i+=1
end
i = 0
j = 0
gugu = [1,2,3,4,5,6,7,8,9]
while i < 9 do
    j = 0
    while j < 9 do
        puts((i+1).to_s()+"x"+(j+1).to_s()+"="+(gugu[i]*gugu[j]).to_s())
        j+=1
    end
    i += 1
end
puts("the end")

members = ["js", "citron", "someone"]
i = 0
while i < members.length do
    puts(members[i])
    i += 1
end
for member in members do
    puts(member)
end
i = 0
for i in (1..10) do
    puts(i)
end