class Student():
    pass


mingyue = Student()

class PythonStudent():

    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print(" I'm doing my homework ")

        return None

yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.name)

yueyue.doHomework()
