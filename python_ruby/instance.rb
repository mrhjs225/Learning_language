class C
    def initialize(v)
        @value = v
    end
    def show()
        p @value
    end
    def setValue(v)
        @value = v
    end
    def getValue()
        return @value
    end
end

c1 = C.new(10)
# p c1.value  # In ruby can't access variable in instance
# c1.value = 20
# p c1.value
c1.show()
c1.setValue(55)
p c1.getValue()

class D
    attr_reader :value
    attr_writer :value
    attr_accessor :value2
    def initialize(v)
        @value = v
        @value2 = v+1
    end
    def show()
        p @value
    end
end

d1 = D.new(555)
p d1.value
d1.value = 777
p d1.value