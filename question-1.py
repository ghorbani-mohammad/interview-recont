# How to overwrite the function of the following class so that it prints a beside returning func_X (inheritance)?

# Class A:
# 	def func_X(self, a):
# 		Return a*2

# Class B(A):


class A:
    def __init__(self):
        self.name = "objj"

    def func_x(self, a):
        return a*2

class B(A):
    def func_x(self, a):
        result = super().func_x(a) 
        print(result)
        return result


obj = B()
y = obj.func_x(3)
print(y)
print(obj.name)

