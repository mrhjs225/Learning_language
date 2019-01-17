module Module_sub1 # 자바랑 비슷하게 파일 분리안해도 가능
    module_function()
    def a()
        return "a"
    end
    def b()
        return "ee"
    end
end

module Module_sub3
    module_function()
    def a()
        return "c"
    end
end