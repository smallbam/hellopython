#coding=utf-8
print("Welcome to python world.")
print("中国人民解放军。")
print("以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；")
print("以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。")
print("Hi",)
print("Indent")

a, b, c = 1, 2, "john" 
print(a, b, c)

str = 'Hello World!'
print(str)          # 输出完整字符串
print(str[:])       # 输出完整字符串
print(str[0])       # 输出字符串中的第一个字符
print(str[2:5])     # 输出字符串中第三个至第五个之间的字符串
print(str[6:])      # 输出从第七个字符开始的字符串
print(str[:5])      # 输出字符串中前五个字符
print(str * 2)      # 输出字符串两次
print(str + "TEST") # 输出连接的字符串


list = ["yanchao", 798, 133.33, "123456"]
tinyList = [123, "debug"]
print(list)              # 输出完整列表
print(list[0])           # 输出列表的第一个元素
print(list[1:3])         # 输出第二个至第三个元素 
print(list[1:])          # 输出从第三个开始至列表末尾的所有元素
print(tinyList * 2)      # 输出列表两次
print(list + tinyList)   # 打印组合的列表

print("tuple元组用()标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。")

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name' : 'john', 'code' : 6734, 'dept' : 'sales'}
print(dict['one'])         # 输出键为'one' 的值
print(dict[2])             # 输出键为 2 的值
print(tinydict)            # 输出完整的字典
print(tinydict.keys())     # 输出所有键
print(tinydict.values())   # 输出所有值

print("身份运算符, is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。")

print("test if, result is :",)
num = 4     
if num == 5:            # 判断num的值
    print('alliance_leader')      
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')    # 条件均不成立时输出

for letter in 'Python' :
   if letter == 'h' :
      pass
      print('这是pass块，pass 不做任何事情，一般用做占位语句。')
   print('当前字母 :', letter)
print("for x in X Good bye!")

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)) :
   print('当前水果 :', fruits[index])
print("for x in X Good bye!2")

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0 :
	number = numbers.pop()
	if (number % 2 == 0) :
	    even.append(number)
	else :
	    odd.append(number)
print("even is :")
print(even)
print("odd is :")
print(odd)

print("My name is %s and weight is %d kg!" % ('Zara', 21))

list1 = ['physics', 'chemistry', 1997, 2000];
print(list1);
del list1[2];
print("After deleting value at index 2 : ")
print(list1);

L = ['Google', 'Alibaba', 'Baidu', 'JD']
print(L[2])  #读取列表中第三个元素
print(L[-2]) #读取列表中倒数第二个元素
print(L[1:]) #从第二个元素开始截取列表

import time
ticks = time.time()
print("当前时间戳为:", ticks)
localtime = time.localtime(ticks)
print("本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

import calendar
cal = calendar.month(2018, 1)
print("以下输出2018年1月份的日历:")
print(cal);


# 可写函数说明
sum = lambda arg1, arg2 : arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

# 可写函数说明
def sum(arg1, arg2):
   # 返回2个参数的和."
   total = arg1 + arg2
   print("函数内 : ", total)
   return total;
def printFunction (function) :
  str = "python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。"
  print("函数的返回值是 ：", function)
  print(str)
# 调用printFunction函数，传入参数是sum函数
printFunction(sum(100, 100))


# 导入模块
import support
# 现在可以调用模块里包含的函数了
str = "Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。"
print("start call support.print_func()")
support.print_func(str)
# 只导入模块里的函数
print("start call support.print_func() agian")
from support import print_func
print_func(str)
print("包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包。")

#一对""" 或者一对 '''可注释多行
"""
str = raw_input("raw_input请输入：");
print "你输入的内容是: ", str
str = input("input 达式作为输入，并将运算结果返回 请输入：");
print "你输入的内容是: ", str
"""

# 打开一个文件
print("file object = open(file_name [, access_mode][, buffering])")
fo = open("support.py", "r")
print("文件名: ", fo.name)
print("访问模式 : ", fo.mode)
print("是否已关闭 : ", fo.closed)

###python3.x 不支持
#print("末尾是否强制加空格 : ", fo.softspace)
# 关闭打开的文件
fo.close()
print("是否已关闭 : ", fo.closed)

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
finally:
    print("最后总是要执行我")

class Employee:
  '所有员工的基类'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
   print("Total Employee %d" % Employee.empCount)

  def displayEmployee(self):
    print("Name : ", self.name,  ", Salary: ", self.salary)

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp1.displayCount()
emp2.displayEmployee()
emp1.displayCount()
emp2.displayCount()
print("Total Employee %d" % Employee.empCount)
print("单下划线、双下划线、头尾双下划线说明:")
print("__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的")
print("_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *")
print("__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。")

import re
line = "Cats are smarter than dogs";
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")