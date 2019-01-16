puts("please type something")
in_str = gets.chomp()
password1 = "1234"
password2 = "qwer"
if in_str == password1 or in_str == password2
    puts("right password")
else
    puts("wrong password")
end
puts("id please")
id = gets.chomp()
puts("password please")
password = gets.chomp()
if id == "man" and password == "0000"
    puts("login success")
else
    puts("fail")
end
a = 0
puts(!false)
if not a
    puts("false")
else
    puts("true")
end