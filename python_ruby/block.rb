5.times() {puts "times"}
3.upto(5) {|i| puts i}
5.times() {|i| puts i}
5.times {puts "is it done?"}

["a", "b", "c"].each() {|i| puts i.upcase()}

arr = ["hello", "world", "new"]

arr.each() {|i| puts i}

for string in arr do
    puts string
end

arr.delete_if() {|string|
    puts string
    string == "world"
}
puts arr