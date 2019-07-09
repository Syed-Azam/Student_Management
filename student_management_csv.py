# PIAIC Assignment - Student Management System - Using CSV Datafile Format
import csv
def line(n): print('—' * n)
def pad(s, n): return s + (" " * (n - len(s)))
while True:
    print("╔═══════════════════════════╗")
    print("║ Student Management System ║")
    print("║    M A I N     M E N U    ║")
    print("╠═══════════════════════════╣")
    print('║   [ 1 ]  Add Student      ║')
    print('║   [ 2 ]  Search Student   ║')
    print('║   [ 3 ]  Edit Student     ║')
    print('║   [ 4 ]  Print Students   ║')
    print('║   [ 5 ]  Delete Student   ║')
    print('║   [ 6 ]  Exit             ║')
    print("╚═══════════════════════════╝")
    option = input("    Enter Choice [1/6] : ")
    print("\n")
    if option == '6':
        print("Thanks for using Student Management System")
        print("Good Bye")
        break
    elif option == '1':
        print("    Student Addition Menu")
        line(50)
        sl = []
        sl.append(input("Enter Name    : "))
        if sl[0] != "":
            sl.append(input("Enter Age     : "))
            sl.append(input("Enter Father  : "))
            sl.append(input("Enter Address : "))
            with open("students.csv", "a", newline="") as s:
                s = csv.writer(s, delimiter=",")
                s.writerow(sl)
            print("Student Added")
        else:
            print("Student Not Added Because Name was Blank")
        input()
        continue
    elif option == '2':
        print("    Student Searching Menu")
        line(30)
        sn = input("Enter Student Name : ")
        with open("students.csv") as s:
            s = list(csv.reader(s))
            print()
            line(74)
            print("Name      Age   Father             Address")
            line(74)
            found = False
            for ln in s:
                if ln[0] == sn:
                    found = True
                    print(pad(ln[0], 10)+pad(ln[1], 6)+pad(ln[2], 19)+pad(ln[3],44))
            if not found:
                print("Student Not Found")
            line(74)
        input()
        continue
    elif option == '3':
        print("    Student Edit Menu")
        line(40)
        sn = input("Enter Student Name : ")
        with open("students.csv") as s:
            data = list(csv.reader(s)) # make a nested list 
            if sn in [st[0] for st in data]: # Check student using list comprehension
                with open("students.csv", "w", newline="") as s:
                    writer = csv.writer(s, delimiter=",")
                    for row in data:
                        if row[0] != sn:
                            writer.writerow(row)
                        else:
                            row[1] = input("Enter Age     : ")
                            row[2] = input("Enter Father  : ")
                            row[3] = input("Enter Address : ")
                            writer.writerow(row)
                print(sn+"'s record has been updated")                
            else:
                print("Student Not Found")
        input()
        continue
    elif option == '4':
        print("    Student Print Menu")
        line(74)
        with open("students.csv") as s:
            s = csv.reader(s)
            print("Name      Age   Father             Address")
            line(74)
            for ln in s:
                print(pad(ln[0], 10)+pad(ln[1], 6)+pad(ln[2], 19)+pad(ln[3],44))
            line(74)
        input()
        continue
    elif option == '5':
        print("    Student Delete Menu")
        line(40)
        sn = input("Enter Student Name : ")
        with open("students.csv") as s:
            data = list(csv.reader(s)) # make a nested list 
            if sn in [st[0] for st in data]: # student name using list comprehension
                with open("students.csv", "w", newline="") as s:
                    writer = csv.writer(s, delimiter=",")
                    for row in data:
                        if row[0] != sn:
                            writer.writerow(row)
                print(sn+"'s record has been deleted")
            else:
                print("Student Not Found")
        input()
        continue
    else:
        print("Invalid Choice - Try Again\n")
        input("Press enter to continue......")
        continue