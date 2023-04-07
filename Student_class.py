class Student:
    def __init__(self,student_id,first_name,last_name):
        self.student_id=int(student_id)
        self.first_name=first_name
        self.last_name=last_name
        self.grades=[]

    def add_grade(self,grade):
        if grade>=0 and grade<=100:
            self.grades.append(grade)
        else:
            print("grade out of range")

    def show_scores(self):
        print(f"Student {self.first_name} {self.last_name} grades are:{self.grades}")

    def score_average(self):
        score=0
        for grade in self.grades:
            score+=grade
        avg=score/len(self.grades)
        return avg

    def course_passed(self):
        grades_above60=0
        for grade in self.grades:
            if grade>60:
                grades_above60+=1
        if grades_above60<3:
            return False
        else:
            return True

studets={
    "John_Doe":Student(1,"Jhone","Doe"),
    "Linda_Jones":Student(2,"Linda","Jones")
}
studets["John_Doe"].add_grade(55)
studets["John_Doe"].add_grade(15)
studets["John_Doe"].show_scores()
print("Passed",studets["John_Doe"].course_passed())

studets["Linda_Jones"].add_grade(25)
studets["Linda_Jones"].add_grade(65)
studets["Linda_Jones"].add_grade(80)
studets["Linda_Jones"].add_grade(75)
studets["Linda_Jones"].show_scores()
print(studets["Linda_Jones"].score_average())
print("Passed",studets["Linda_Jones"].course_passed())