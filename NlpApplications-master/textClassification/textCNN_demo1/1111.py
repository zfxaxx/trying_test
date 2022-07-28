# try:
#     num=eval(input("请输入一个数："))
#     print(num**2)
# # except NameError:
# #     print("输入错误1，请重新输入一个数")
# except ValueError:
#     print("输入错误2，请重新输入一个数")
# except :
#     print("输入错误3，请重新输入一个数")
# else:
#     print("执行语句1")
# finally:
#     print("执行语句2")
import operator

# print(operator.truediv(3,1))

# num = eval(input("请输入一个数字："))
# print(num)
# print(type(num))


class MyTest(object):

    def __init__(self):
        self.name = "zhangsan"
        self.age = 20

    def __getattr__(self, item):
        print(self.__dict__)
        return item



sample = MyTest()
sample.gender = 'male'
print(sample.dd)
# print(sample.__dict__)