class Student:
    no_of_leaves = 10

    def __init__(self,aexam,aresult,arole):
        self.exam = aexam
        self.result = aresult
        self.role = arole

    def printdetails(self):
        return f"the name is {self.exam}. Result is {self.result} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    def __mod__(self, other):
        return self.result % other.result

    def __mul__(self, other):
        return self.result * other.result

    def __sub__(self, other):
        return self.result - other.result

    def __str__(self):
        return f"Student Name is {self.exam}. result is {self.result} and role is {self.role}"

stu1 = Student("davide", 4.5, "good boy")






































print(str(stu1))



