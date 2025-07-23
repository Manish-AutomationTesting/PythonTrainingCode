class Employee:
    # Hidden data member of employee class:
    __salary = 1000


e1 = Employee()
# print(e1.__salary)--this is not right way to accessing hidden private variable

#Access private hidden variable by using tricky syntax:
print(e1._Employee__salary)



