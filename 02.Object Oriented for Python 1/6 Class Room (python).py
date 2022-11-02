class ClassRoom:
    def __init__(self, grade=0 ,homeRoomTeacher="", studentList=[] ):
        self.grade = grade
        self.homeRoomTeacher = homeRoomTeacher
        self.studentList = studentList
        self.numStudents = len(self.studentList)

    def add_student(self, student_name):
        if self.numStudents < 10:
            self.studentList.append(student_name)
            self.numStudents += 1
            return True
        else:
            return False

    def change_student(self, n , new_name):
        if n <= self.numStudents:
            self.studentList[n-1] = new_name
            return True
        else:
            return False

    def remove_student(self, student_name):
        if student_name in self.studentList:
            self.studentList.remove(student_name)
            self.numStudents -= 1
            return True
        else:
            return False

    def remove_student_no(self, n):
        if n < self.numStudents:
            self.studentList.pop(n)
            self.numStudents -= 1
            return True
        else:
            return False

    def __str__(self):
        return f'''Grade: {self.grade}
Homeroom Teacher: {self.homeRoomTeacher}
Students: {','.join(self.studentList)}'''

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_homeRoomTeacher(self):
        return self.homeRoomTeacher

    def set_homeRoomTeacher(self, homeRoomTeacher):
        self.homeRoomTeacher = homeRoomTeacher

    def get_studentList(self):
        return self.studentList

    def set_studentList(self, studentList):
        self.studentList = studentList

    def get_numStudents(self):
        return self.numStudents

    def set_numStudents(self, numStudents):
        self.numStudents = numStudents

school = ClassRoom(10, "Mr. Smith", ["John", "Jane", "Joe"], 3)
print(school)
print(school.add_student("Jack"))
print(school)
print(school.change_student(3, "Jack"))
print(school)
print(school.remove_student("Jack"))
print(school)
print(school.remove_student_no(2))
print(school)

