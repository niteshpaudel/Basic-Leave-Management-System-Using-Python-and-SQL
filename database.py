from asyncio.windows_events import NULL
from types import NoneType
import cx_Oracle
import os
clear=lambda:os.system('cls')
con = cx_Oracle.connect('system/system@localhost:1521/xe')
worker = con.cursor()
worker.execute('select * from studentinfo')
rows = worker.fetchall()
worker.execute('select * from hods')
rowss = worker.fetchall()

clear()
print("Welcome to my database\n\n")
print("Login:")
r=0
while r!=1:
    log = input("Press 1 for HOD login\nPress 2 for Student login\nPress 3 for Principal login\n")
    if log == '1':
        clear()
        r=1
        z=0
        while z!=1:
            clear()
            cor=""
            cou = input("Select your course\nPress 1 for Bsc. IT\nPress 2 for BCA\nPress 3 for BBA\nPress 4 for Bcom\nPress 5 for MBA\nPress 6 for Mcom\n")
            if cou=='1':
                cor ="bscit"
                tem ="Bsc IT"
                z=1
            elif cou=='2':
                cor ="bca"
                tem ="BCA"
                z=1
            elif cou=='3':
                cor="bba"
                tem="BBA"
                z=1
            elif cou=='4':
                cor="bcom"
                tem="Bcom"
                z=1
            elif cou=='5':
                cor="mba"
                tem="MBA"
                z=1
            elif cou=='6':
                cor="mcom"
                tem="Mcom"
                z=1
            else:
                clear()
                print("Select valid course")
                z=0
        q=0
        while q!= 1:
            passwr=input("Enter password: ")
            check = 0
            if passwr == "" or passwr ==" ":
                check = 2

            if check == 2:
                clear()
                print("Password cannot be empty")
                print("Login failed!\n\nPlease try again\n\n")

            elif check == 0:
                k=0
                found=0
                for i in rowss:
                    if cor == rowss[k][1] and passwr == rowss[k][2]:
                        found=1
                        names = rowss[k][0]
                        break     
                    k+=1
                if found==1:
                    q=1
                    clear()
                    print("Login Succesful!")
                    print("Welcome",names,"\nCourse: ",tem)
                    e=0
                    while e!=1:
                        choice=input("Press 1 to view unapproved leaves of department\nPress 2 to view all leaves of department\nPress 3 to view leave balance of approved students\nPress 4 to view leave of unapproved students\n")
                        if choice == '1':
                            e=1
                            query = "select * from (select roll_no,name,to_char(leave_date,'dd-mm-yy'),no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where course='{0}' and approved='{1}'".format(cor,"waiting")
                            print(query)
                            worker.execute(query)
                            data = worker.fetchall()
                            print("S.No:\t\tRoll no\t\tName\t\tDate\t\tDays\t\tReason\t\tApprove\t\tRemarks")
                            t=1
                            y=1
                            count=0
                            for i in data:
                                print(t,"\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6],"\t",i[7])
                                t+=1
                                count+=1
                            l=0
                            while l!=1:
                                b=0 
                                while b!=1:
                                    ch = input("Enter the S.no you want to approve or reject\n")
                                    if ch=="":
                                        print("Cannot be empty")
                                        continue
                                    pr = int(ch)
                                    if pr<=0 or pr>count:
                                        b=0
                                        print("Entered serial number does not exist\nTry again")
                                    elif pr>0 or pr<=count:
                                        b=1
                                        ap = input("Press a to approve and r to reject this leave\n")
                                        rem = input("Enter the remarks\n")
                                        rol = data[pr-1][0]
                                        dat = data[pr-1][2]
                                        if ap=='a':
                                            query1="update leaveinfo set approved = 'yes' where roll_no ={0} and leave_date = to_date('{1}','dd-mm-yy')".format(rol,dat)
                                            query2="update leaveinfo set remarks='{0}' where roll_no ={1} and leave_date = to_date('{2}','dd-mm-yy')".format(rem,rol,dat)
                                            worker.execute(query1)
                                            worker.execute(query2)
                                            worker.execute("commit")
                                            while True:
                                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                                if again == '1':
                                                    e=0
                                                    clear()
                                                    break
                                                elif again == '2':
                                                    clear()
                                                    quit()
                                                else:
                                                    print("Wrong input!\nTry again\n")
                                                    continue
                                        elif ap=='r':
                                            query1="update leaveinfo set approved = 'no' where roll_no ={0} and leave_date = to_date('{1}','dd-mm-yy')".format(rol,dat)
                                            query2="update leaveinfo set remarks='{0}' where roll_no ={1} and leave_date = to_date('{2}','dd-mm-yy')".format(rem,rol,dat)
                                            worker.execute(query1)
                                            worker.execute(query2)
                                            worker.execute("commit")
                                            while True:
                                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                                if again == '1':
                                                    e=0
                                                    clear()
                                                    break
                                                elif again == '2':
                                                    clear()
                                                    quit()
                                                else:
                                                    print("Wrong input!\nTry again\n")
                                                    continue
                                        else:
                                            l=0
                                            clear()
                                            print("Wrong input! Try again")
                        elif choice == '2':
                            e=1
                            query = "select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where course='{0}'".format(cor)
                            worker.execute(query)
                            data = worker.fetchall()
                            print("Roll no\t\tName\t\tDate\t\tDays\t\tReason\t\tApprove\t\tRemarks")
                            t=0
                            y=1
                            for i in data:
                                print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
                                t+=1
                            while True:
                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                if again == '1':
                                    e=0
                                    clear()
                                    break
                                elif again == '2':
                                    clear()
                                    quit()
                                else:
                                    clear()
                                    print("Wrong input!\nTry again\n")
                                    continue
                        elif choice == '3':
                            e=1
                            query = "select roll_no,sum(no_of_days),10-sum(no_of_days) from leaveinfo where approved='yes' group by roll_no"
                            worker.execute(query)
                            data = worker.fetchall()
                            print(data)
                            print("Roll no\t\tTotal Days\t\tLeave Balance")
                            for i in data:
                                print(i[0],"\t",i[1],"\t",i[2],)
                            while True:
                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                if again == '1':
                                    e=0
                                    clear()
                                    break
                                elif again == '2':
                                    clear()
                                    quit()
                                else:
                                    clear()
                                    print("Wrong input!\nTry again\n")
                                    continue
                        elif choice == '4':
                            e=1
                            query = "select roll_no,sum(no_of_days),10-sum(no_of_days) from leaveinfo where approved='waiting' group by roll_no"
                            worker.execute(query)
                            data = worker.fetchall()
                            print(data)
                            print("Roll no\t\tTotal Days\t\tLeave Balance")
                            for i in data:
                                print(i[0],"\t",i[1],"\t",i[2],)
                            while True:
                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                if again == '1':
                                    e=0
                                    clear()
                                    break
                                elif again == '2':
                                    clear()
                                    quit()
                                else:
                                    clear()
                                    print("Wrong input!\nTry again\n")
                                    continue
                        else:
                            print("Enter valid choice")
                else:
                        clear()
                        print("Login failed!\n\nPlease try again\n\n")
                        q=0

    elif log == '2':
        r=1
        x=1
        while (x!=0):
            rollno = input("Enter Your Roll Number: ")
            passw=input("Enter password: ")
            check = 0
            if rollno == "" or rollno ==" ":
                check = 1
            elif passw == "" or passw ==" ":
                check = 2
            if (rollno == "" and passw == "") or (rollno ==" " and passw ==" "):
                check = 3
            if check == 1:
                clear()
                print("Roll number cannot be empty")
                print("Login failed!\n\nPlease try again\n\n")
            elif check == 2:
                clear()
                print("Password cannot be empty")
                print("Login failed!\n\nPlease try again\n\n")
            elif check == 3:
                clear()
                print("Roll number and password cannot be empty")
                print("Login failed!\n\nPlease try again\n\n")
            elif check == 0:
                k=0
                found=0
                for i in rows:
                    if rollno == str(rows[k][1]) and passw == rows[k][2]:
                        found=1
                        name = rows[k][0]
                        course = rows[k][3]
                        break
                    
                    k+=1
                if found==1:
                    clear()
                    print("Login Succesful!")
                    print("Welcome",name,"\nRoll no: ",rollno,"\nCourse: ",course)
                    y=0
                    while y!=1:
                        choice = input("Enter Your Choice: \nPress 1 to apply for leave\nPress 2 for viewing leave status\nPress 3 to logout\nPress 4 to edit your leave(s)\n")
                        appr = 'waiting'   
                        ream = 'waiting'
                        if choice == '1':
                            clear()
                            leave_bal="select sum(no_of_days) from leaveinfo where roll_no={0} and approved='yes'".format(rollno)
                            worker.execute(leave_bal)
                            counts=worker.fetchall()
                            worker.execute("commit")
                            count = counts[0][0]
                            if count==None:
                                count=0
                            print("Your leave balance is",10-count)
                            if count>10:
                                print("Sorry you have reached the limit of applying leaves")
                            else:
                                apply = input('Enter starting date of the leave(should be of the format DD-MM-YY):\n')
                                no_of_days = int(input('For how many days: '))
                                reason = input("Your reason for leave: ")
                                string="insert into leaveinfo values({0},to_date('{1}','dd-mm-yy'),{2},'{3}','{4}','{5}')".format(rollno,apply,no_of_days,reason,appr,ream)
                                worker.execute(string)
                                worker.execute("commit")
                                while True:
                                    again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                    if again == '1':
                                        e=0
                                        clear()
                                        break
                                    elif again == '2':
                                        clear()
                                        quit()
                                    else:
                                        clear()
                                        print("Wrong input!\nTry again\n")
                                        continue

                        elif choice == '2':
                            clear()
                            string = "select * from (select roll_no,name,to_char(leave_date,'dd-mm-yy'),no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where roll_no={0}".format(rollno)
                            worker.execute(string)
                            data = worker.fetchall()
                            print("Roll no\t\tName\t\tDate\t\tDays\t\tReason\t\tApprove\t\tRemarks")
                            t=0
                            y=1
                            for i in data:
                                print(i[0],"\t","\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
                                t+=1
                            while True:
                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                if again == '1':
                                    e=0
                                    clear()
                                    break
                                elif again == '2':
                                    clear()
                                    quit()
                                else:
                                    clear()
                                    print("Wrong input!\nTry again\n")
                                    continue
                        elif choice == '3':
                            clear()
                            print("Thankyou",name,"\nRoll no: ",rollno)
                            y=0    
                            x = 0            
                        elif choice == '4':
                            query = "select * from (select roll_no,name,to_char(leave_date,'dd-mm-yy'),no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where roll_no={0} and approved='{1}'".format(rollno,"waiting")
                            worker.execute(query)
                            data = worker.fetchall()
                            print("S.No:\t\tRoll no\t\tName\t\tDate\t\tDays\t\tReason\t\tApprove\t\tRemarks")
                            t=1
                            y=1
                            count=0
                            for i in data:
                                print(t,"\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
                                t+=1
                                count+=1
                            l=0
                            while l!=1:
                                b=0 
                                while b!=1:
                                    ch = input("Enter the S.no of the leave you want to edit\n")
                                    if ch=="":
                                        print("Cannot be empty")
                                        continue
                                    pr = int(ch)
                                    if pr<=0 or pr>count:
                                        b=0
                                        print("Entered serial number does not exist\nTry again")
                                    elif pr>0 or pr<=count:
                                        b=1
                                        ap = input("Press 1 to delete a leave\nPress 2 to edit a leave\n")
                                        rol = data[pr-1][0]
                                        dat = data[pr-1][2]
                                        if ap=='1':
                                            query="delete from leaveinfo where roll_no ={0} and leave_date = to_date('{1}','dd-mm-yy')".format(rol,dat)
                                            worker.execute(query)
                                            worker.execute("commit")
                                            while True:
                                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                                if again == '1':
                                                    e=0
                                                    clear()
                                                    break
                                                elif again == '2':
                                                    clear()
                                                    quit()
                                                else:
                                                    print("Wrong input!\nTry again\n")
                                                    continue
                                        elif ap=='2':
                                            newdate=input("Enter new starting date of leave(should be of the format DD-MM-YY):\n")
                                            newdays=int(input("Enter number of days:\n"))
                                            newreason=input("Enter reason:\n")
                                            query1="update leaveinfo set leave_date = to_date('{0}','dd-mm-yy') where roll_no ={1} and leave_date = to_date('{2}','dd-mm-yy')".format(newdate,rol,dat)
                                            query2="update leaveinfo set no_of_days={0} where roll_no ={1} and leave_date = to_date('{2}','dd-mm-yy')".format(newdays,rol,newdate)
                                            query3="update leaveinfo set reason='{0}' where roll_no ={1} and leave_date = to_date('{2}','dd-mm-yy')".format(newreason,rol,newdate)
                                            worker.execute(query1)
                                            worker.execute(query2)
                                            worker.execute(query3)
                                            worker.execute("commit")
                                            while True:
                                                again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                                                if again == '1':
                                                    e=0
                                                    clear()
                                                    break
                                                elif again == '2':
                                                    clear()
                                                    quit()
                                                else:
                                                    print("Wrong input!\nTry again\n")
                                                    continue
                                        else:
                                            l=0
                                            clear()
                                            print("Wrong input! Try again")
                        else:
                            print("Please enter a valid choice")

                else:
                    clear()
                    print("Login failed!\n\nPlease try again\n\n")
    elif log=='3':
        clear()
        print("Welcome Principal of Islamia College of Science and Commerce\n\n")
        x=0
        while x!=1:
            password = input("Enter password: ")
            if password=='principal@123':
                x=1
                clear()
                print("Login successful!")
                y=0
                while y!=1:
                    cho = input("Press 1 to view all leaves of college\nPress 2 to view leaves by department\n")
                    if cho == '1':
                        y=1
                        query = "select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no))"
                        worker.execute(query)
                        data = worker.fetchall()
                        print("Roll no\t\tName\t\tDate\t\tDays\t\tReason\t\tApprove\t\tRemarks")
                        t=0
                        y=1
                        for i in data:
                            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
                            t+=1
                        while True:
                            again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                            if again == '1':
                                e=0
                                clear()
                                break
                            elif again == '2':
                                clear()
                                quit()
                            else:
                                clear()
                                print("Wrong input!\nTry again\n")
                                continue
                    elif cho == '2':
                        y=1
                        cou = input("Select your course\nPress 1 for Bsc. IT\nPress 2 for BCA\nPress 3 for BBA\nPress 4 for Bcom\nPress 5 for MBA\nPress 6 for Mcom\n")
                        if cou=='1':
                            cor ="bscit"
                        elif cou=='2':
                            cor ="bca"
                        elif cou=='3':
                            cor="bba"
                        elif cou=='4':
                            cor="bcom"
                        elif cou=='5':
                            cor="mba"
                        elif cou=='6':
                            cor="mcom"
                        else:
                            clear()
                            print("Select valid course")
                        query = "select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where course='{0}'".format(cor)
                        worker.execute(query)
                        data = worker.fetchall()
                        print("Roll no\t\tName\t\tDate\t\tDays\t\tReason\t\tApprove\t\tRemarks")
                        t=0
                        y=1
                        for i in data:
                            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
                            t+=1
                        while True:
                            again = input("Thankyou for using this program\nPress 1 to go back\nPress 2 to quit\n")
                            if again == '1':
                                e=0
                                clear()
                                break
                            elif again == '2':
                                clear()
                                quit()
                            else:
                                clear()
                                print("Wrong input!\nTry again\n")
                                continue
                    else:
                        y=0
                        print("Enter valid choice!\n")
            elif password=="" or password==" ":
                clear()
                x=0
                print("Password cannot be empty!\nTry again")
            else:
                clear()
                print("Wrong password!\nTry again")
                x=0

    else:
        r=0
        clear()
        print("Please enter valid choice")