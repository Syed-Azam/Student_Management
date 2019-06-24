# PIAIC Assignment - Student Management System
def line(): print('—'*50)
def search(s, students): ## List Comprehension (Generate a Filtered List)
    return [e for e in students if e['Name'] == s]
def display(st): ## Print a Report if List is not Empty
    if st == []:
        print ("Sorry Student Record Not Found!")
    else:
        line()
        print("Name\tAge\tFather\tAddress")
        line()
        for d in st:
            print(d["Name"],'\t', d["Age"],'\t', d["Father"],'\t', d["Address"])
        line()
# putting some sample data in advance
students = [{"Name":"Kashif", "Age":"42", "Father":"Jamay", "Address":"A-36 Block A"},
            {"Name":"Atif", "Age":"41", "Father":"Jamay", "Address":"A-36 Block A"},
            {"Name":"Naveed", "Age":"40", "Father":"Jamay", "Address":"A-36 Block A"},
            {"Name":"Raheel", "Age":"28", "Father":"Naeem", "Address":"A-36 Block A"}]
while True:
    line()
    print("    Student Management System")
    print("       M A I N    M E N U    ")
    line()
    print('    Press 1 to Add Student')
    print('    Press 2 to Search Student')
    print('    Press 3 to Edit Student')
    print('    Press 4 to Print All Student')
    print('    Press 5 to Delete Student')
    print('    Press 6 to Exit')
    line()
    option = input("    Enter Choice [1/6] : ")
    line()
    print("\n")
    if option == '6':
        print("Thanks for using Student Management System")
        print("Good Bye")
        break
    elif option == '1':
        line()
        print("Student Addition Menu")
        line()
        student = {}
        student['Name']    = input("Student Name        : ")
        student['Age']     = input("Student Age         : ")
        student['Father']  = input("Student Father Name : ")
        student['Address'] = input("Student Address     : ")
        students.append(student)
        print("New Student Recorded has successfully added")
        input("Press enter to continue......")
        continue
    elif option == '2':
        line()
        print("Student Searching Menu")
        display(search(input("Enter Student Name : "), students))
        input("Press enter to continue......")
        continue
    elif option == '3':
        line()
        print("Student Edit Menu")
        sn = input("Enter Student Name : ")
        display(search(sn, students))
        for c in range(len(students)):
            if students[c]["Name"] == sn:
                students[c]['Age'] = input("Student Age (Modified) : ")
                students[c]['Father'] = input("Student Father Name (Modified) : ")
                students[c]['Address'] = input("Student Address (Modified) : ")
                print("Student record has updated")
        input("Press enter to continue......")
        continue
    elif option == '4':
        line()
        print("Student Printing Menu")
        display(students) 
        input("Press enter to continue......")
        continue       
    elif option == '5':
        line()
        print("Student Deletion Menu")
        line()
        sn = input("Enter Student Name : ")
        display(search(sn, students))
        for c in range(len(students)):
            if students[c]["Name"] == sn:
                sure = input("Are you sure to delete this student record : ")
                if sure.upper() == "Y" or sure.upper() == "YES":
                    del students[c]
                    print("Student record has deleted")
                    break
        input("Press enter to continue......")
        continue
    else:
        print("Invalid Choice - Try Again\n")
        input("Press enter to continue......")
        continue
