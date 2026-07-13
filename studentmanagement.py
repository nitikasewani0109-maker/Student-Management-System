# Student Management 
file_name="student_data.JSON"
ADMIN_PASSWORD=2345
TOTAL_MARKS=400
import json
#functions
def file_call():
    while True:
        try:
            with open(file_name,'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not exist")
            continue
def choice_call(message):
    while True:
        try:
            choice=int(input(message))

        except ValueError:
            print("Enter your answer as integer")
            continue
        return choice
def admin_addstudent():
        students=file_call()
        roll_number=choice_call("Enter the Roll Number of new student:")
        if roll_number in students:
            print("Roll number already exist")
        else:
            students[roll_number]=get_student_data(students,roll_number)
           
            with open(file_name,'w')as f:
                json.dump(students,f,indent=4)
def admin_viewstudents():
    students=file_call()
    for roll,data in students.items():
        print(roll,data)
def admin_searchstudent():
    students=file_call()
    admin_search=input("Enter the roll number to search:")
    if admin_search in students:
        student=students[admin_search]
        for key,value in student.items():
            if key=="marks":
                print("Marks:")
                for subject,mark in value.items():
                    print(subject,":",mark)
            else:
                print(key,":",value)

    else:
        print("Roll number do not exist")
def  get_student_data(students,roll_number):
        
            name=input("Enter Name:")
            age=choice_call("Enter age:")
            grade=input("Enter class:")
            fathername=input("Enter Fathers name:")
            mothername=input("Enter Mothers name:")
            print("------Marks------")
            maths=input("Maths:")
            physics=input("Physics:")
            chemistry=input("chemistry:")
            english=input("English:")
            

            students[roll_number]={
            "name":name,
            "age":age,
            "class":grade,
            "fathername":fathername,
            "mothername":mothername,
            "marks":{
                "maths":maths,
                "physics":physics,
                "chemistry":chemistry,
                "english":english
            }
        }
            return students[roll_number]
def admin_updatestudent():
    students=file_call()
    roll_number=str(choice_call("Enter the roll number to be updated:"))
    if roll_number in students:
        update_student=get_student_data(students,roll_number)
        with open(file_name,'w')as f:
            json.dump(students,f,indent=4)
    else:
        print("Roll number do not exist")
def admin_deletestudent():
    students=file_call()
    delete_students=input("Enter roll number to delete:")
    if delete_students in students:
        del students[delete_students]
        with open(file_name,'w') as f:
            json.dump(students,f,indent=4)

# Main menu----------------------------------------------------------------------------------------------------------------------------
while True:
    print("\n==========Student Management System=============")
    print("1. Student Portal")
    print("2. Admin Panel")
    print("3. Exit")
    choice=choice_call("Entr the choice:")
    if choice==1:
        # Student Functions-------------------------------------------------------------------------------------------------------------
        roll_number=choice_call("Enter your roll number:")
        with open(file_name,'r') as f:
            students=json.load(f)
        if roll_number in students:
            print("\n==========Welcome to Student Portal===========")
            print("1.Search my Record")
            print("2.View Report Card")
            print("3.Exit")
            student_choice=choice_call()
            search=(input("Enter your Roll number:"))
            if student_choice==1:
                
                student=(students[search])
                print("Name:",student["name"])
                print("Age:",student["age"])
                print("Class:",student["class"])
                print("Fathers name:",student["fathername"])
                print("Mothers name:",student["mothername"])
            elif student_choice==2:
                student=students[search]
                print("\n=========Report Card==========")
                print("Name:",student["name"])
                print("Maths:",student["marks"]["maths"])
                print("Physics:",student["marks"]["physics"])
                print("Chemistry:",student["marks"]["chemistry"])
                print("English:",student["marks"]["english"])
                print("\n--------------------------------")
                total=int(student["marks"]["maths"])+int(student["marks"]["physics"])+int(student["marks"]["chemistry"])+int(student["marks"]["english"])
                print("Total    :",total)
                percentage=(total/TOTAL_MARKS)*100
                print("Percentage:",percentage)
                if total<=120:
                    print("Fail")
                else:
                    print("Pass")
                    if total>=350:
                        print("A+")
                    elif total>=300 and total<350:
                        print("A")
                    elif total>=200 and total<300:
                        print("B")
                    elif total>=120 and total<200:
                        print("C")
                    else:
                        print("D")
        else:
            print("Roll number do not exist")
        ask=choice_call()
        if ask == 1:
            lines=file_call()
    elif choice==2:
        admin_ask= choice_call(("Enter the Password:"))
        if admin_ask == ADMIN_PASSWORD:
            print("\n===========Welcome to Admin Panel============")
            print("1. Add Student")
            print("2. View All Student")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            # Admin functions-------------------------------------------------------------------------------------------------------
            admin_choice=choice_call("Enter the admins choice:")
            if admin_choice==1:
                admin_addstudent()
                print("Student data added successfully")
            elif admin_choice==2:
                admin_viewstudents()
            elif admin_choice==3:
                admin_searchstudent()
            elif admin_choice==4:
                admin_updatestudent()
                print("Student data updated successfully")
            elif admin_choice==5:
                admin_deletestudent()
                print("Student data deleted successfuly")
            elif admin_choice==6:
                break
            else:
                print("Invalid choice")
        else:
            print("Incorrect password")    
    elif choice==3:
        break
    else:
        print("Invalid choice")    


