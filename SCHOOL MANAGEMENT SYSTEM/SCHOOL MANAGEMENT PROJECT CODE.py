import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="ADMIN",database="project")



def addstudent():
    n=input("Enter Student Name:")
    c=input("Enter Class Name:")
    r=input("Enter Roll No:")
    a=input("Enter Address:")
    p=input("Enter Phone No:")
    data=(n,c,r,a,p)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data entered succesfully")
    print(">----------------------------")
    main()


def displayclass():
    cl=input("class:")
    data=(cl,)
    sql="select * from student where class=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("CLASS:",i[1])
        print("ROLL:",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print(">-------------------------------")
        main()



def removestudent():
    c=input("Enter Class Name:")
    r=input("Enter Roll Number:")
    data=(c,r)
    sql='delete from student where CLASS =%s and ROLL=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data updated")
    print(">--------------------------------------")
    main()

def addteacher():
    n=input("Enter Teacher:")
    p=input("Enter Post:")
    s=input("Enter Salary:")
    a=input("Enter Address:")
    ph=input("Enter Phone:")
    data=(n,p,s,a,ph)
    sql='insert into teacher values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data entered successfully")
    print(">--------------------------------------")
    main()


def displayteacher():
    sql="select * from teacher"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("name:",i[0])
        print("post:",i[1])
        print("salary:",i[2])
        print("address:",i[3])
        print("phone:",i[4])
        print(">--------------------------------<")
    print(">------------------------------------")
    main()


def removeteacher():
    n=input("Enter Teacher Name:")
    ac=input("Enter Post:")
    data=(n,ac)
    sql='delete from teacher where name=%s and Post=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data updated")
    print(">-------------------------------------")
    main()


def absentclass():
    d=input("Enter Date:")
    cl=input("Enter Class:")
    ab=input("Enter names of the absent students:")
    data=(d,cl,ab)
    sql="insert into cattendance values(%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data updated")
    print(">-------------------------------------")
    main()



def absentteacher():
    d=input("Enter Date:")
    ab=input("Enter Names Of Absent Teacher:")
    data=(d,ab)
    sql="insert into tattendance values(%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data updated")
    print(">-------------------------------------")
    main()


def submitfees():
    n=input("student name:")
    c=input("class name:")
    r=input("roll number:")
    m=input("Date,month and year:")
    f=input("fees to be paid:")
    d=input("pending fees yes or no:")
    data=(n,c,r,m,f,d)
    sql='insert into fees values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entered successfully")
    print(">-------------------------------------")
    main()


def paysalary():
    n=input("Enter Teacher Name:")
    m=input("Enter Month and Year:")
    p=input("Enter amount to be paid:")
    data=(n,m,p)
    sql='insert into salary values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Salary credited to account no:86*******56")
    print(">------------------------------------")
    main()








def main():
    print("""               GEETHAANJALI AISSC SCHOOL
                 1.ADD STUDENT              2.DISPLAY CLASS
                 3.REMOVE STUDENT           4.ADD TEACHER
                 5.DISPLAY TEACHER          6.REMOVE TEACHER
                 7.CLASS ATTENDANCE         8.TEACHER ATTENDANCE
                 9.SUBMIT FEES              10.PAY SALARY

""")
    choice=input("enter task no:")
    print(">----------------------<")
    if (choice == '1'):
        addstudent()
    elif (choice == '2'):
        displayclass()
    elif (choice == '3'):
        removestudent()
    elif (choice == '4'):
        addteacher()
    elif (choice == '5'):
        displayteacher()
    elif (choice == '6'):
        removeteacher()
    elif (choice == '7'):
        absentclass()
    elif (choice == '8'):
        absentteacher()
    elif (choice == '9'):
        submitfees()
    elif (choice == '10'):
        paysalary()
    else:
        print("wrong choice...")
        main()

def pswd():
    p=input("password:")
    if p=="hari":
        main()
    else:
        print("Incorrect password")
        pswd()

pswd()

    
        
