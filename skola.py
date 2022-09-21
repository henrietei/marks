class Student:
    name=None
    marks=None


    def __init__(self, name=None, marks=None):
        self.name=name
        self.marks=marks

        self.get_data()

    def set_data(self, name=None, marks=None):
        self.name=name
        self.marks=marks


    def get_data(self):
        print (self.name, 'atzime:', self.marks)

    def check_pass_fail(self):
        if self.marks>5:
            print("pass")
        else:
            print("fail")



student1=Student("henriete", 3)
student2=Student("anna", 8)
check1=student1.check_pass_fail()
check2=student2.check_pass_fail()
