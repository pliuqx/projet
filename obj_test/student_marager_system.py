# -*- coding: utf-8 -*-
"""
@File    :   student_marager_system.py
@Time    :   2023/08/15 15:52:25
@Author  :   应无所住 、何生其心
@Version :   python3.10
@Software:   VsCode
"""


"""
    学生管理系统
    项目计划：
        	1.完成数据模型类StudentModel
        	2.创建逻辑控制类StudentManagerController
		    3.完成数据：学生列表 __stu_list
		    4.行为：获取列表 stu_list,
		    5.添加学生方法 add_student
		    -------------14:30-------------
		    6.根据编号删除学生remove_student
		    -------------14:36-------------
		    7.根据编号修改学生update_student
		    #16:00
		    8.在界面视图类中，根据编号删除学生.
		    17:05
		    9.在界面视图类中，根据编号修改学生信息.
		    17:30

"""


class StudentModel:
    """
        学生类模型
    """
    def __init__(self, name="", age=0, score=0, id=0):
        """
        :param name:  学生姓名
        :param age:  年龄
        :param score:  成绩
        :param id:   学生对象的唯一标识
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id
        pass


class StudentManagerController:
    __init_id = 1000
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """

        :return:
        """
        return self.__stu_list

    def add_student(self, list_info):
        """
        :param list_info:  没有编号的学生信算息
        :return:
        """
        list_info.id = self.student_id()
        self.__stu_list.append(list_info)

    def student_id(self):
        """

        :return:
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id
    
    def del_stu(self,id):
        """

        :param id:
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)    
                return True
        return False
    
    def update_stu(self,stu_info):
        """

        :param stu_info:
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False
    
    def soft_stu(self):
        for r in range(len(self.__stu_list) -1):
            for c in range(r +1 ,len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r],self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]
        pass
    

class StudentManagerView:
    def __init__(self) :
        self.__manager = StudentManagerController()

    def __display_stu(self):
        print('学生管理系统主菜单')
        print('1)添加学生信息')
        print('2)显示学生信息')
        print('3)修改学生信息')
        print('4)删除学生信息')
        print('5)按学生成绩排序')
        print('6)退出学生信息系统')
    
    
    


if __name__ == "__main__":
    s01 = StudentModel("李四", 18, 100)
    sm01 = StudentManagerController()
    sm01.add_student(s01)
    for re in  sm01.stu_list:
        print(re.name,re.id)
    pass