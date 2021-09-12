class A:
    def printmyname(): print(__package__)

class B(A):
    pass

A.printmyname()
B.printmyname()