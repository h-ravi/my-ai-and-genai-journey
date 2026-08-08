import json
# empty File Create if not exist
try:
    file = open("students.json","x")
    file.close()
except FileExistsError:
    pass

# update list after new running
try:
    with open("students.json","r") as file_in_list:
        all_students = json.load(file_in_list)
except json.JSONDecodeError:
    all_students = []

# update database
def update_student_list():
    with open("students.json","w") as add_details:
        json.dump(all_students, add_details, indent=4)
# Show All Student list
def all_stu():
    try:
            for stu_details in all_students:
                print(f"=================================================")
                print(f"Student ID Number : {stu_details['id']}\nStudent Name : {stu_details['name']}\nAge : {stu_details['age']}\nCourse : {stu_details['course']}\nFee Paid : {stu_details['fees_paid']}")
                print(f"=================================================\n")              
    except json.JSONDecodeError:
        print("Student Database Currently Empty. No Student Record")
# Found Student
def found_stu():
    while True:
        try:
            find_id = int(input("Enter Student ID : "))
        except ValueError:
            print("Student ID is number not name or latter. Please Enter ID in Only Number")
            continue
        if find_id <= 0:
            print("Less Then or Equal To Zero ID Number is Not Allowed. Please Enter Greater Then Zero ID Number.")
        else:
            found = False
            try:
                    for stu_details in all_students:
                        if stu_details['id'] == find_id:
                            print(f"=================Student Details=================")
                            print(f"Student ID Number : {stu_details['id']}\nStudent Name : {stu_details['name']}\nAge : {stu_details['age']}\nCourse : {stu_details['course']}\nFee Paid : {stu_details['fees_paid']}")
                            print(f"=================================================")
                            found = True
                            break
                    if found == False:
                        print("Student Details Not Found.")
                        continue
                    else:
                        break
            except json.JSONDecodeError:
                found = False
    return find_id
# main
login = True
while login:
    print("===== Student Management =====\n1. Add Student Details\n2. Show All Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
    try:
        choose = int(input("Choose your option in number (like 1,2,3..6) : "))
    except ValueError:
        print("Please Choose Option In number Not Name.")
        continue
# Add Students Details
    if choose == 1:
        # ID Number Input
        while True:
            try:
                id_no = int(input("Enter Student ID Number (only Number Not latter) : "))
            except ValueError:
                print("Please Enter Only Numeric Roll Number.")
                continue
            if id_no <= 0:
                print("Less Then or Equal To Zero ID Number is Not Allowed. Please Enter Greater Then Zero ID Number.")
                continue
            else:
                found = False
                try:
                    with open("students.json","r") as in_all_stu:
                        student = json.load(in_all_stu)
                        for stu_details in student:
                            if stu_details['id'] == id_no:
                                print("This Student ID already exist and Duplicate Student ID is Not Allowed. Please Enter Unique Student ID.")
                                found = True
                                break
                except json.JSONDecodeError:
                    found = False
            if found == True:
                continue
            else:
                break
        # Student Name input
        while True:
            stu_name = input("Enter Student Full Name : ")
            if stu_name.strip() == "":
                print("Name is not leave empty. please enter student name")
            else:
                break
        # student age
        while True:
            try:
                stu_age = int(input("Enter Student Age : "))
            except ValueError:
                print("Please Enter Only Number Value. Not words/latter")
            if stu_age <= 0:
                print("Student age equal or less then Zero")
            else:
                break
        # Course Name
        while True:
            course_name = input("Enter Course Name : ")
            if course_name.isdigit():
                print("Course Name is not in digit. please enter full course name.")
            else:
                break
        # fee paid or not
        while True:
            try:
                fee_status = int(input("Enter Fee Status. Input 1 for paid or 0 for not paid : "))
            except ValueError:
                print("Please input 1 for paid or 0 for not paid.")
                continue
            if fee_status == 0 or fee_status == 1:
                if fee_status == 0:
                    fee_status = False
                    break
                elif fee_status == 1:
                    fee_status = True
                    break
            else:
                print("Please input 1 for fees paid or 0 for not fees paid.")
                continue
        new_stu = {
            "id" : id_no,
            "name" : stu_name,
            "age" : stu_age,
            "course" : course_name,
            "fees_paid" : fee_status
        }
        all_students.append(new_stu)
        update_student_list()
        print(f"Student ID Number {id_no} Data was Successfully Added in json Database.")
#2. Show All Students
    elif choose == 2:
        all_stu()
#3. Search Student only ID
    elif choose == 3:
        found_stu()
#4. Update Student Details
    elif choose == 4:
        find_id = found_stu()
        print("\nWhat do you want to update in the student details?")
        while True:
            print("\n1. Student Name\n2. Student Age\n3. Course\n4. Fees Status\n5. Exit")
            try:
                choose_update_option = int(input("Choose Update Option under 1,2,3,4 : "))
            except ValueError:
                print("You Choose Invalid Option. Please Choose Valid Option.")
                continue
            if choose_update_option <= 0 or choose_update_option > 5:
                print("You Choose Invalid Option. Please Choose Valid Option.")
                continue
            else:
                    for stu_details in all_students:
                        if stu_details['id'] == find_id:
                            match choose_update_option:
                                case 1:
                                    new_name = input("Enter Student Change Name : ")
                                    stu_details['name'] = new_name
                                    break
                                case 2:
                                    while True:
                                        try:
                                            new_age = int(input("Enter Student age for Update : "))
                                        except ValueError:
                                            print("Please Enter Age only in number.")
                                            continue
                                        if new_age <= 0 or new_age > 40: # Take 40 max Student Age
                                            print("Please Enter Valid Student Age")
                                            continue
                                        else:
                                            stu_details['age'] = new_age
                                            print()
                                            break
                                    break
                                case 3:
                                    new_course = input("Enter New Course Name : ")
                                    stu_details['course'] = new_course
                                    break
                                case 4:
                                    while True:
                                        try:
                                            new_fee_status = int(input("Enter Fee Status. Input 1 for paid or 0 for not paid : "))
                                        except ValueError:
                                            print("Please input 1 for paid or 0 for not paid.")
                                            continue
                                        if new_fee_status == 0 or new_fee_status == 1:
                                            if new_fee_status == 0:
                                                new_fee_status = False
                                                break
                                            elif new_fee_status == 1:
                                                new_fee_status = True
                                                break
                                        else:
                                            print("Please input 1 for paid or 0 for not paid.")
                                            continue
                                    stu_details['fees_paid'] = new_fee_status
                                case 5:
                                    break
                                case _:
                                    print("Invalit Opion. Please Choose Right Option.")
                                    continue
                    break
        update_student_list()
        print(f"Student ID Number {find_id} Data was Successfully updated in json Database.\n")

#5. Delete Student
    elif choose == 5:
        find_id = found_stu()
        print("Are yue sure to deleting this student data? enter 1 for yes or 2 for no.")
        while True:
            try:
                confirm = int(input("Enter : "))
            except ValueError:
                print("Invallid Confirmation. Enter 1 for yes or 2 for no.")
                continue
            if confirm <= 0 or confirm > 2:
                print("Invallid Confirmation. Enter 1 for yes or 2 for no.")
                continue
            elif confirm == 1:
                for index, stu_details in enumerate(all_students):
                    if stu_details['id'] == find_id:
                        del all_students[index]
                        break
                update_student_list()
                print("Student Data Delete Successfully.")
                break
            elif confirm == 2:
                break
            else:
                print("Invallid Confirmation. Enter 1 for yes or 2 for no.")
    elif choose == 6:
        login = False
    else:
        print("Invalid Option! Please choose under given option")
