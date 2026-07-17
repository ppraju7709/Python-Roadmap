def menu():
    print("1. Add student")
    print("2. View all student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Analyze Performance")
    print("7. Show Topper")
    print("8. Rank students")
    print("9. Save Data")
    print("10. Load Data")
    print("Exit")

# list of dictionaries
student = [
    {
        "id":1,
        "nm":"Sanika Jadhav",
        "age":19,
        "phno":34562874254,
        "attendence":92,
        "assignment":8,
        "maths":77,
        "science":50,
        "english":98,
        "avg":75,
        "Grade":'B'
    },
    {
        "id":2,
        "nm":"Vaishnavi Solanki",
        "age":20,
        "phno":92762874254,
        "attendence":83,
        "assignment":7,
        "maths":87,
        "science":80,
        "english":78,
        "avg":81.66,
        "Grade":'A'
    }
]
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

def view_all_stud():
    print("-"*40)
    print(f"{'ID':<5}{'Name':<25}{'Average':<10}{'Grade':<5}")
    print("-"*40)

    for stud in student:
        print(f"""{stud['id']:<5}
            {stud['name']:<25}
            {stud['avg']:<10}
            {stud['grade']:<5}""")
    print("-"*40)

def search_stud():
    searchid = int(input("Enter student id :"))
    searchnm = input("Enter student name:")
    for stud in student :
        if stud['id'] == searchid and stud['nm']== searchnm :
                print(student[stud])

def update_stud():
    a = input("Enter what you want to update (marks/attendence/assignments) :")
    b = int(input("Enter id :"))
    for i in student:
        if i['id']==b:
            if a=="marks":
                m=int(input("Enter maths marks:"))
                s = int(input("Enter science marks :"))
                e = int(input("Enter english marks :"))
                i['maths']=m
                i['science']=s
                i['english']=e
                avg = (maths + english + science)/3
                assign_grade()

            if a=="attendence":
                at =int(input("Enter attendence :"))
                i['attendence']=at
            if a=="assignments":
                ass =int(input("Enter assignment :"))
                i['assignments']=ass
    print("updated successfully")
        
def assign_grade():
    pass
def delete_student():
    b = int(input("Enter id :"))
    for i in student:
        if i['id']==b:
            q = input("Do you want to delete student info (y/n) :")
            if q=='y':
                student.remove(i)
                print("deleted successfully")
            else:
                print("Deletion cancelled")
        


            