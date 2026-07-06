import test_my_add as add
from day11 import test_my_add

print(add.sum(10, 20))
from test_my_mutil import sum


print(add.num)
print(add.add(12, 15.2))

print(sum(12, 14))

from P01_My_Add import *
from test_my_add import *
# print(str1)  # 因为P01_My_Add使用了 __all__，而这个变量不在__all__中，所以即使不带_，也无法使用
print(strqq)
print(num)

import sys
print(f"模块搜索导入顺序：{sys.path}")
# dir
print(dir(test_my_add))

from graphic import *
c1 = circle.Circle(10) 
print(c1.area(12))
