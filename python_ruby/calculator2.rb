class Cal
    attr_reader :v1, :v2
    attr_writer :v1
    @@_history = []
    def initialize(v1, v2)
        p v1, v2
        @v1 = v1
        @v2 = v2
    end
    def add()
        result = @v1 + @v2
        @@_history.push("add : #{@v1}+#{@v2}=#{result}")
        return result
    end
    def subtract()
        result = @v1 - @v2
        @@_history.push("subtract : #{@v1}-#{@v2}=#{result}")
        return result
    end
    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        end
    end
    def getV1()
        return @v1
    end
    def Cal.history()
        for item in @@_history
            p item
        end
    end
    def info()
        return "Cal => v1 : #{@v1}, v2 : #{@v2}"
    end
end

class CalMul < Cal
    def multifly()
        result = @v1 * @v2
        @@_history.push("multiply : #{@v1}*#{@v2}=#{result}")
        return result
    end
    def info()
        p "CalMul => #{super()}"
    end
end

c1 = CalMul.new(10, 10)
p c1.add()
p c1.multifly()
Cal.history()
num1 = 3
num2 = 4
puts "hello #{num1} world"
c2 = Cal.new(20, 55)
p c2.info()
c1.info()