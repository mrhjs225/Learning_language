class Cal
    def initialize(v1, v2)
        p v1, v2
        @v1 = v1
        @v2 = v2
    end
    def add()
        return @v1 + @v2
    end
    def subtract()
        return @v1 - @v2
    end
    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        end
    end
    def getV1()
        return @v1
    end
end

c1 = Cal.new(10, 10)
p c1.add()
p c1.subtract()

c2 = Cal.new(30, 20)
p c2.add()
p c2.subtract()

p Cal.new(50,50).add()

p "below result isn't use object"

def add(v1, v2)
    return v1 + v2
end
def subtract(v1, v2)
    return v1 - v2
end

num1 = 10
num2 = 10
p add(num1, num2)
p subtract(num1, num2)

num3 = 30
num4 = 20
p add(num3, num4)
p subtract(num3, num4)