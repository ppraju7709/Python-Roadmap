import json

def menu():
    print("1. Add student")
    print("2. View all student")
    print("3. Search student")
    print("4. Update student")
    print("5. View Grades")
    print("6. Delete student")
    print("7. Analyze Performance")
    print("8. Show Topper")
    print("9. Save Data")
    print("10. Load Data")
    print("11.Exit")
    global choice
    choice = int(input("Enter choice (1/2/3/4/5/6/7/8/9/10/11) : "))
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number.")
        

# list of dictionaries
student = []
def add_stud():
    id = int(input("Enter Id :"))
    nm = input("Enter name :")
    age = int(input("Enter age :"))
    phno = int(input("Enter Contact no.:"))
    attendence = int(input("Enter your attendence :"))
    assignment = int(input("Enter Assignments You are Completed :"))
    maths = int(input("Enter marks of Maths :"))
    science = int(input("Enter marks of Science :"))
    english = int(input("Enter marks of English :"))
    avg = (maths + english + science)/3
    grade = assign_grade(avg)
    
    student.append({
        "id": id,
        "nm": nm,
        "age": age,
        "phno": phno,
        "attendence": attendence,
        "assignment": assignment,
        "maths": maths,
        "science": science,
        "english": english,
        "avg": avg,
        "grade": grade
    })
    save_data()

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 50:
        return "E"
    elif avg >= 40:
        return "Pass"
    else:
        return "Fail"


def view_all_stud():
    print("-"*55)
    print(f"{'ID':<5}{'Name':<25}{'Average':<10}{'Grade':<5}")
    print("-"*55)

    for stud in student:
        print(f"{stud['id']:<5}{stud['nm']:<25}{stud['avg']:<10.2f}{stud['grade']:<5}")
    print("-"*55)

def search_stud():
    searchid = int(input("Enter student ID: "))

    for stud in student:
        if stud['id'] == searchid:
            print("-"*40)
            print("ID :", stud['id'])
            print("Name :", stud['nm'])
            print("Age :", stud['age'])
            print("Phone :", stud['phno'])
            print("Maths :", stud['maths'])
            print("Science :", stud['science'])
            print("English :", stud['english'])
            print("Average :", stud['avg'])
            print("Grade :", stud['grade'])
            print("-"*40)
            return

    print("Student not found.")

def update_stud():
    a = input("Enter what you want to update (marks/attendence/assignments) :")
    b = int(input("Enter id :"))

    found = False

    for i in student:
        if i['id']==b:
            if a=="marks":
                m=int(input("Enter maths marks:"))
                s = int(input("Enter science marks :"))
                e = int(input("Enter english marks :"))
                i['maths']=m
                i['science']=s
                i['english']=e
                i['avg']=(i['maths']+i['science']+i['english'])/3

                i['grade']= assign_grade(i['avg'])

            if a=="attendence":
                at =int(input("Enter attendence :"))
                i['attendence']=at
            if a=="assignment":
                ass =int(input("Enter assignment :"))
                i['assignment']=ass
            print("updated successfully")
            save_data()
            return
    if not found:
        print("Student not found.")    
    
        
def view_grade():
    print("-"*55)
    print(f"{'ID':<5}{'Name':<35}{'Grade':<5}")
    print("-"*55)

    for stud in student:
        print(f"{stud['id']:<5} {stud['nm']:<35}{stud['grade']:<5}")
    print("-"*55)

def delete_stud():
    b = int(input("Enter id :"))
    for i in student:
        if i['id']==b:
            q = input("Do you want to delete student info (y/n) :")
            if q=='y':
                student.remove(i)
                print("deleted successfully")
            else:
                print("Deletion cancelled")
    save_data()
        
def analyze_performance():
    id = int(input("Enter student ID: "))
    for stud in student:
        if stud['id'] == id:

            print("Average:", stud['avg'])
            print("Grade:", stud['grade'])

            if stud['maths'] > stud['science'] and stud['maths'] > stud['english']:
                print("Strongest Subject : Maths")
            elif stud['science'] > stud['maths'] and stud['science'] > stud['english']:
                print("Strongest Subject : Science")
            else:
                print("Strongest Subject : English")

            if stud['maths'] < stud['science'] and stud['maths'] < stud['english']:
                print("Weakest Subject : Maths")
            elif stud['science'] < stud['maths'] and stud['science'] < stud['english']:
                print("Weakest Subject : Science")
            else:
                print("Weakest Subject : English")

            print("Attendance Status :")
            if stud['attendence'] >= 75:
                print("Attendance is Good.")
            else:
                print("Attendance is below 75%.")

            print("Assignment Status :")
            if stud['assignment'] == 10:
                print("Assignments Completed.")
            else:
                remain = 10 - stud['assignment']
                print(stud['assignment'], "Assignments Completed")
                print(remain, "Assignments Remaining")

            return
    print("Student not found.")

def show_topper():
        topper=max(student,key=lambda x:x['avg'])

        print("Topper :",topper['nm'])
        print("ID :", topper['id'])
        print("Average :",topper['avg'])
        print("Grade :",topper['grade'])

def save_data():
    with open("student.json",'w')as file:
        json.dump(student,file,indent=4)

    print("Data saved successfully")
    
def load_data():
    global student

    try:
        with open('student.json','r')as file:
            student = json.load(file)
    except FileNotFoundError:
        student = []
    
print("----------------------------------------")
print("     Student Performance Analyzer")
print("----------------------------------------")
load_data()
while True:
    print("\n Choose menu below to do operations : \n")
    
    menu()
    if choice == 1:
        add_stud()
    elif choice == 2:
        view_all_stud()
    elif choice == 3:
        search_stud()
    elif choice == 4:
        update_stud()
    elif choice == 5:
        view_grade()
    elif choice == 6:
        delete_stud()
    elif choice == 7:
        analyze_performance()
    elif choice == 8:
        show_topper()
    elif choice == 9:
        save_data()
    elif choice == 10:
        load_data()
    elif choice == 11:
        print("Exiting menu...")
        break
    else:
        print("Invalid Choice, Try again...")

    
