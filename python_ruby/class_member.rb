require 'date'
d1 = Date.new(2010, 1, 1)
d2 = Date.new(2020, 2, 29)
p d1.year()
p d2.day()
p Date.today()

class Cs
    def Cs.now() ## class method!
        p "now!"
    end
    def instance_method()
        p "instance~"
    end
end
i = Cs.new()
Cs.now()
i.instance_method()
# Cs.instance_method() error
# i.now() error

class Cs2
    @@count = 0 # 초기화는 맨 처음 한번만
    def initialize()
        @@count += 1
    end
    def Cs.getCount()
        return @@count
    end
end

i1 = Cs2.new()
i2 = Cs2.new()
i3 = Cs2.new()
p Cs.getCount()
# p i1.getCount()