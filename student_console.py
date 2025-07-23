a=[]
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=int(grade)


    def display(self):
        print(f"{self.name},{self.grade} added in list")
        if self.grade>80:
            a.append((self.name,self.grade))
while True:
    name=input("Enter your name:")
    grade=int(input("Enter grade:"))
    student1=Student(name,grade)
    student1.display()
    print(a)
    if len(a)==3:
        break
