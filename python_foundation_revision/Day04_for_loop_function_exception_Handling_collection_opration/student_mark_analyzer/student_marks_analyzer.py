# Canel confirmation function
def confirmation():
    confi_status = True
    while confi_status:
        try:
            confi = int(input("Enter : "))
        except ValueError:
            print("invalid Number! You input as latter not number. enter 1 for Yes or 0 for No")
            continue
        if confi == 0 or confi == 1:
            return confi
        else:
            print("invalid Option! please Enter Right option. enter 1 for Yes or 0 for No")

# roll number function
def roll_number():
    print(f'===========================\nAdding Student Number {sr_no} Details \n===========================')
    unique_roll = True
    while unique_roll:
        stu_roll_no = input("Enter Student Roll Number : ")
        # roll number validation
        if stu_roll_no in stu_data:
            print("Roll Numer alredy Existing, Roll Number is not store Duplicate")
            print(stu_data.get(stu_roll_no))
        else:
            stu_data[stu_roll_no] = ""
            unique_roll = False
    return stu_roll_no

# Student Add form
def call_student_form(stu_roll_no):
    stu_name = input("Enter Student Name : ")
    subject_status = True
    while subject_status:
        try:
            print("Attention Please! if you enter mark less or equal to Zero or greater then 100 then your mark is consider 0 without warning. So please Enter your currect and Right mark under 1 to 100.")
            math = float(input("Enter Math Marks : "))
            science = float(input("Enter Science Marks : "))
            english = float(input("Enter English Marks : "))
            subject_status = False
        except ValueError:
            print("Please Enter all Subject Mark as a Number (with decimal or without decimal) not string")
            continue
    if math <= 0 or math > 100:
        math = 0
    if science <= 0 or science > 100:
        science = 0
    if english <=0 or english > 100:
        english = 0
    total_number = math+science+english
    average = round(total_number/3,2)
    percentage = round((total_number/300)*100,2)
    math_status = 'Pass' if math >= 40 else 'Fail'
    science_status = 'Pass' if science >= 40 else 'Fail'
    english_status = 'Pass' if english >= 40 else 'Fail'
    if math_status == 'Fail':
        pass_status = "Fail"
    elif science_status == 'Fail':
        pass_status = "Fail"
    elif english_status == 'Fail':
        pass_status = "Fail"
    elif percentage <= 40:
        pass_status = "Fail"
    else:
        pass_status = "Pass"
    stu_data[stu_roll_no] = {
        "name": stu_name,
        "math": math,
        "science": science,
        "english": english,
        "total": total_number,
        "average": average,
        "status": {
            "math_status": math_status,
            "science_status": science_status,
            "english_status": english_status,
            "overall_status": pass_status,
            }
        }
    print(f"Student name {stu_name}, Roll Number {stu_roll_no} Data Succefully Added \n")

# student Data
stu_data = {}
# main program
login = True
while login:
    print('''========== STUDENT MARKS ANALYZER ==========
1. Add Students Data
2. Show All Results
3. Show Topper
4. Show Pass/Fail List
5. Remove a Student
6. Exit
==============================================''')
    try:
        choose = int(input("Choose your option under 1 to 6 : "))
        print("\n")
    except ValueError:
        print("invalid choosen Option! Please enter only number.")
        continue
    if choose <= 0:
        print("Not Valid Option Choose! Enter only greater then o (positive number)")
    elif choose == 1:
        while True:
            try:
                stu_num = int(input("Enter How Many Add Student Data in number. if Enter zero then cancle this add sudent data : "))
            except ValueError:
                print("invalid Number! You input a latter not number. Please Enter Number like 123,555,1,2,3.........")
                continue
            if stu_num < 0:
                print("Invalid Input! If add Student data then please Not enter number is less then or qual to Zero. Always Enter number is grater then Zero.")
            elif stu_num == 0:
                print("Are you sure you want to close Add Student Data Pannel? Enter 1 for Yes or 0 for No")
                close_add_student_data = confirmation()
                if close_add_student_data == 1:
                    break
                else:
                    continue
            else:
                for total_student in range(stu_num):
                    sr_no = total_student+1
                    roll = roll_number()
                    call_student_form(roll)
                break
    elif choose == 2:
        for roll_numb, details in stu_data.items():
            print("=================================")
            print(f'Student Roll Number  = {roll_numb}')
            print(f"Student Name = {details['name']}")
            print(f"Subject Wise Marks : \n => Math = {details['math']} ({details['status']['math_status']}) \n => Science = {details['science']} ({details['status']['science_status']}) \n => English = {details['english']} ({details['status']['english_status']})")
            print(f"Total Marks = {details['total']} out of 300")
            print(f"Average Mark = {details['average']}")
            print(f"Overall Status = {details['status']['overall_status']}")
            print("=================================\n")
    elif choose == 3:
        topper = -1
        topper_roll = ""
        topper_name = ""
        for roll, student in stu_data.items():
            if student['total'] > topper:
                topper_roll = roll
                topper_name = student['name']
                topper = student['total']
        print(f'Topper Student Roll Number {topper_roll}, Name {topper_name}, and Total Number {topper}')
    elif choose == 4:
        for roll, student in stu_data.items():
            print(f"Roll Number {roll}, Student Name {student['name']} and this student status is = {student['status']['overall_status']}")
    elif choose == 5:
        while True:
            student_roll_number = input("Enter Student Roll Number to delete student Data : ")
            try:
                del_stu_name = stu_data.get(student_roll_number)['name']
            except TypeError:
                print("This roll number not found. Please Enter Right Roll Number")
                print("if to be continue then enter 0 for continue or enter 1 for goto to main menu.")
                confir = confirmation()
                if confir == 0:
                    continue
                else:
                    break
            del stu_data[student_roll_number]
            print(f"Student Roll Number {student_roll_number} and Student name {del_stu_name} Data Deleted Succusssfully.")
            break
    elif choose == 6:
        print("Are you sure you want to close student marks analyser? Enter 1 for Yes or 0 for No")
        choosen_option = confirmation()
        if choosen_option == 1:
            login = False
        else:
            continue
    else:
        print("Please Choose Valid Option Under 1 to 6.")
