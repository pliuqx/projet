# -*- coding: utf-8 -*-
'''
@File    :   open_clos.py
@Time    :   2023/08/28 10:32:31
@Author  :   应无所住 、何生其心
@Version :   python3.10
@Software:   VsCode
'''


class Staff:
    def __init__(self):
        self.__sta_list = []

    @property
    def sta_list(self):
        return self.__sta_list

    def add_staff(self, staff):
        self.__sta_list.append(staff)

    def calculate_employee_salaries(self, sta_obj):
        for item in self.__sta_list:
            re = item.count_wages()
            print(re)
        pass
    

class Count:
    def __init__(self, salary=0):
        self.salary = salary

    def count_wages(self):
        pass


class Programmer(Count):
    def __init__(self, name,salary,val):
        super().__init__(salary)
        self.name = name 
        self.val = val
        
        
    def count_wages(self):
        return self.salary + self.val * 0.05


class Sale(Count):
    def __init__(self, name,salary,val ):
        super().__init__(salary)
        self.naem = name 
        self.val = val

    def count_wages(self):
        return self.salary + self.val * 0.05
        pass


if __name__ == "__main__":
    p01 = Programmer("zs",1000,10000)
    ss01 = Sale("ls",2000,20000)
    s01 = Staff()
    s01.add_staff(p01)
    s01.add_staff(ss01)
    aa = s01.calculate_employee_salaries(p01)
    # bb = s01.calculate_employee_salaries(ss01)
    print(aa)
    

