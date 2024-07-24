class Student:
    def __init__(self, id, name, batchname, yoe, gradeyear, psp):
        self.name = name
        self.id = id
        self.batchName = batchname
        self.yoe = yoe
        self.gradeYear = gradeyear
        self.psp = psp

    def __str__(self):
        return str(self.name) + " is Created"

class StudentBuilder(Student):
    def __init__(self):
        self.id = None
        self.name = None
        self.batchName = None
        self.yoe = None
        self.gradeYear = None
        self.psp = None

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_batchName(self, batch):
        self.batchName = batch
    def set_yoe(self, yoe):
        self.yoe = yoe
    def set_grade_year(self, gradeYear):
        self.gradeYear = gradeYear
    def set_psp(self, psp):
        self.psp = psp
    def build(self):
        return Student(self.id, self.name, self.batchName, self.yoe, self.gradeYear, self.psp)







        