



# Python program to search student record using dictionary 

# Student class to get student details and print...
class Student:
    def GetStudent(self):
        self.__rollno = input("Enter Roll No:")
        self.__name = input("Enter Name:")
        self.__MicroprocessorMarks = int(input("Enter Microprocessor Marks:"))
        self.__Python_ProgarmmingMarks = int(input("Enter Python Programming  Marks:"))
        self.__Computer_NetworksMarks = int(input("Enter Computer Network Marks:"))
        return(self.__rollno)

    def PutStudent(self):
        print(self.__rollno,self.__name,((self.__MicroprocessorMarks+self.__Python_ProgarmmingMarks+self.__Computer_NetworksMarks)/3))
    def Search(self,min,max):
        per = (self.__MicroprocessorMarks+self.__Computer_NetworksMarks+self.__Python_ProgarmmingMarks)/3
        if(per>=min and per<=max):
            return True
        else:
            return False

# creating a dictionary to store student record 
studentDict = dict()
n = int(input("How Many Students you Want To Input? : "))
for i in range(n):
 S = Student()
 rollno = S.GetStudent()
 studentDict.setdefault(rollno,S)

# Searching for student records with roll numbers provided by the user.
rollno = input("Enter Roll Number you Want Search?")
S = studentDict.get(rollno,"Not Found!")
if(isinstance(S,Student)):
    S.PutStudent()
else:
    print(S)

# Printing records of all users with marks greater than 60% 
print("All students who scored more that 60 percentage are : ")
gradeAStudent = list(filter(lambda s:s.Search(60,100),studentDict.values()))
if(len(gradeAStudent) == 0):
    print("Record Not Found!")
else:
    for S in gradeAStudent:
        S.PutStudent()
