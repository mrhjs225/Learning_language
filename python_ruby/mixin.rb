module M1
    def m1_m
        p "m1_m"
    end
end
module M2
    def m1_m
        p "m2_m"
    end
end

class C
    include M1, M2
end

o = C.new()
o.m1_m()
# o.m2_m(