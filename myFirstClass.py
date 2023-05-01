class MyClass:
    number_of_students = 0
	
    def __init__(self, name, gen, city):
        self.student_name = name
        self.student_gender = gen
        self.spudent_city = city
        self.addStudent()
    
    def addStudent(self):
        MyClass.number_of_students += 1

