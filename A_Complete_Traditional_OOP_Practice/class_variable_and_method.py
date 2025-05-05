class StudentGrade:
    std_grade="A"

    @classmethod
    def change_grade_power(cls, grade):
        if cls.std_grade == "A":
            cls.std_grade =grade
        elif cls.std_grade == "A+":
            cls.std_grade = grade
    
    @classmethod
    def show_std_grade(cls):
        print(cls.std_grade)




std_grade_1=StudentGrade()
print(std_grade_1.std_grade)
StudentGrade.change_grade_power("A+")
StudentGrade.show_std_grade()
print(std_grade_1.std_grade)