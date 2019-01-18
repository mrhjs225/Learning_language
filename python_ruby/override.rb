class C1
    def m()
        return "parent"
    end
end

class C2 < C1
    def m()
        return super()+" child"
    end
    def m2()
        return "child2"
    end
end

class C3 < C2
    alias :supm2 :m2
    def m()
        return supm2()+" second child"
    end
end

o = C2.new()
p o.m()
o2 = C3.new()
p o2.m()