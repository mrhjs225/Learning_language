puts(Math.sqrt(16))
puts(Math.cos(0))

require_relative "module_sub1"
require_relative "module_sub2"


puts(Module_sub1.a())
puts(Module_sub2.a())
puts(Module_sub3.a())
puts(Module_sub1.b())