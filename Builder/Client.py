from Builder.Student import *
class Client:
    if __name__ == '__main__':
        mybuilder = StudentBuilder()
        mybuilder.set_id(1)
        mybuilder.set_name("Anil")
        mybuilder.set_psp("20")
        mybuilder.set_yoe("2022")
        mybuilder.set_grade_year("2022")
        anil = mybuilder.build()

        print(anil)
