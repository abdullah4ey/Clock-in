
from tkinter import*
from tkintertable import TableCanvas, TableModel
import tkinter.messagebox
import sqlite3
import datetime
import time
import csv
#---------------------TABLE 1
conn =sqlite3.connect("Employees ID.db")
c= conn.cursor()
#---------------------TABLE 2
conns =sqlite3.connect("Signed in employees.db")
co= conns.cursor()
#---------------------TABLE 3
connss =sqlite3.connect("Details of Employees.db")
coo= connss.cursor()
#---------------------Table4
connnss =sqlite3.connect("table viewer.db")
cooo= connnss.cursor()
#-----------------------Creating Table 1
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Users(usernames TEXT,passwords TEXT)")

#------------------------Creating Table 2
def create_table1():
    co.execute("CREATE TABLE IF NOT EXISTS User(usernames TEXT,passwords TEXT)")
#------------------------Creating Table 3
def create_table2():
    coo.execute("CREATE TABLE IF NOT EXISTS Signed_in(usernames TEXT,sign_in REAL,sign_out REAL)")

#------------------------Creating Table 4
def create_table3():
    cooo.execute("CREATE TABLE IF NOT EXISTS View(usernames TEXT,sign_in REAL,sign_out REAL)")
#Calling all the tables
def creating_tables():
    create_table()
    create_table1()
    create_table2()
    create_table3()
creating_tables()




#Deleting data from database3
def delete_all_Signed_in_database():
    sql = 'DELETE FROM Signed_in'
    coo = connss.cursor()
    coo.execute(sql)




#This function checks username and password against entries of database 1 and 2. if username and password is not found in database2 and the same username and password
#is found in database1, then it records real time under sign in coloumn on the database 3 and 4 alnog their username.
def signing_in():
    user1=str(labelentry1.get())
    password1=str(labelentry2.get())
    sign="-"
    time= datetime.datetime.now()
    date_time=time.strftime('%I:%M,%p, %A')
    co.execute("SELECT * FROM User WHERE(usernames,passwords)=(?,?)",(user1,password1));
    dat= co.fetchall()
    c.execute("SELECT* FROM Users WHERE(usernames,passwords)=(?,?)",(user1,password1));
    data= c.fetchall()
    if data ==[]:
        tkinter.messagebox.showinfo("Warning!!","Your username or password is incorrect!!!")
    elif data == dat:
        tkinter.messagebox.showinfo("Welcome","you are already logged in")
    else:
        labelentry1.delete(0,END)
        labelentry2.delete(0,END)
        co.execute("INSERT INTO User(usernames,passwords) VALUES (?, ?)",(user1, password1))
        conns.commit() 
        coo.execute("INSERT INTO Signed_in(usernames,sign_in,sign_out) VALUES (?,?,?)",(user1, date_time,sign))
        connss.commit()
        cooo.execute("INSERT INTO View(usernames,sign_in,sign_out) VALUES (?,?,?)",(user1, date_time,sign))
        connnss.commit()
        tkinter.messagebox.showinfo("Welcome","you are successfully logged in!!!")
            
#This function checks username and password against entries of database 2. if username and password is found in database2, then it records real time
#under sign out coloumn on the database 3 and 4 along their username.

def sign_out():
    user_name=str(labelentry1.get())
    password=str(labelentry2.get())
    sign="-"
    time= datetime.datetime.now()
    date_time=time.strftime('%I:%M,%p, %A')
    co.execute("SELECT * FROM User WHERE (usernames,passwords)=(?,?)",(user_name,password));
    dat= co.fetchall()
    if dat==[]:
        tkinter.messagebox.showinfo("Warning!!","Your username or password is incorrect!!!")
        return
    else:
        labelentry1.delete(0,END)
        labelentry2.delete(0,END)
        tkinter.messagebox.showinfo("Welcome","you are successfully signed out!!!")
        
        coo.execute("UPDATE Signed_in SET (sign_out)=(?) WHERE (usernames,sign_out)=(?,?)",(date_time, user_name,sign))
        connss.commit()
        cooo.execute("UPDATE View SET (sign_out)=(?) WHERE (usernames,sign_out)=(?,?)",(date_time, user_name,sign))
        connnss.commit()
        co.execute("DELETE FROM User WHERE (usernames,passwords)=(?,?)",(user_name,password))
        conns.commit()




#Creates admin window which has two button, two entries and two labels and each button have a different function assigned to them.

def Administrator():
    global labelentri1
    global labelentri2
    global window
    window=Tk()
    window.geometry('375x420+700+110')
    window.title('Sign in system')
    window.resizable(width=False, height=False)
    lablinfo1=Label(window,font=('Calibri (Body)',25,'bold'),text="WELCOME",fg='black',bd=10)
    lablinfo1.pack(side=TOP)
    labl1info2=Label(window,font=('Calibri (Body)',12),text="Admin",fg='black',bd=10)
    labl1info2.pack(side=TOP)
    f2 =Frame(window, width =375, height= 300,relief=SUNKEN)
    f2.pack(side=LEFT)
    labl4=Label(f2,font=('Calibri (Body)',12),text="User Name:",fg='black',bd=10)
    labl4.grid(row=0,column=0, padx=10, pady=10, sticky="w")
    labl5=Label(f2,font=('Calibri (Body)',12),text="Password:",fg='black',bd=10)
    labl5.grid(row=1,column=0, padx=10, pady=10, sticky="w")
    labelentri1 = Entry(f2)
    labelentri1.grid(row=0,column=3, padx=10, pady=10, sticky="w")
    labelentri2 = Entry(f2)
    labelentri2.grid(row=1,column=3, padx=10, pady=10, sticky="w")
    btn2 =Button(f2, text="Sign in",font=('Calibri (Body)',12),fg='black',bd=10,command=verifying)
    btn2.grid(row=3,column=3, padx=10, pady=10, sticky="w")
    btn2 =Button(f2,font=('Calibri (Body)',12),text="Back",fg='black',bd=10,command=Back)
    btn2.grid(row=3,column=6, padx=10, pady=10, sticky="w")
    window.mainloop()

    
#Creates another window for admin if correct username and password is entered on admin window.
#It then allow admin to make changes to CSV and close the whole program by calling 'Close' function

def verifying():
        global master1
        user__name=labelentri1.get()
        pass__word=labelentri2.get()
        if user__name=="abdullah" and pass__word=="90":
            master1=Tk()
            master1.geometry('375x420+500+110')
            master1.resizable(width=False, height=False)
            master1.title('Sign in system')
            lablinfo=Label(master1,font=('Calibri (Body)',20,'bold'),text="welcome",fg='black',bd=10)
            lablinfo.pack(side=TOP)
            f3 =Frame(master1, width =375, height= 300,relief=SUNKEN)
            f3.pack(side=LEFT)
            btn7 =Button(f3, text="Back",font=('Calibri (Body)',12),fg='black',bd=10,command=Back1)
            btn7.grid(row=3,column=3, padx=10, pady=10, sticky="w")
            btn8 =Button(f3, text="Clear CSV",font=('Calibri (Body)',12),fg='black',bd=10,command=delete_all_Signed_in_database)
            btn8.grid(row=1,column=10, padx=10, pady=10, sticky="w")
            btn9 =Button(f3,font=('Calibri (Body)',12),text="Close",fg='black',bd=10,command=Close)
            btn9.grid(row=3,column=20, padx=10, pady=10, sticky="w")
            master1.mainloop()  
        else:
            tkinter.messagebox.showinfo("Error","your User name or password is wrong")

#Deletes the admin login window.            
def Back():
    window.destroy()

#Deletes admin and admin login window.   
def Back1():
    master1.destroy()
    window.destroy()

#Clear database and close the whole program
def Close():
     cooo.execute('DELETE From View')
     tkinter.messagebox.showinfo("Successful",'the program will be closed')
     c.close()
     co.close()
     coo.close()
     cooo.close()
     conn.close()
     conns.close()
     connss.close()
     connnss.close()
     window.destroy()
     master1.destroy()
     windows.destroy()
    


#Creates a registration window with 10 label, 8 entries and 2 buttons and each button is assigned a different function.
def register():
    global labelentry3
    global labelentry4
    global labelentry5
    global labelentry6
    global labelentry7
    global labelentry8
    global labelentry9
    global labelentry10
    global windoows
    windoows=Tk()
    windoows.geometry('750x500+500+110')
    windoows.resizable(width=False, height=False)
    windoows.title('Sign in system')
    lablinfo3=Label(windoows,font=('Calibri (Body)',20,'bold'),text="Sign up",fg='black',bd=10)
    lablinfo3.pack(side=TOP)
    labl1info4=Label(windoows,font=('Calibri (Body)',12),text="With Best of the Best",fg='black',bd=10)
    labl1info4.pack(side=TOP)
    f3 =Frame(windoows, width =600, height= 400,relief=SUNKEN)
    f3.pack(side=LEFT)
    labl6=Label(f3,font=('Calibri (Body)',12),text="First Name:",fg='black',bd=10)
    labl6.grid(row=0,column=0, padx=10, pady=10, sticky="w")
    labl7=Label(f3,font=('Calibri (Body)',12),text="Last Name:",fg='black',bd=10)
    labl7.grid(row=1,column=0, padx=10, pady=10, sticky="w")
    labelentry3 = Entry(f3)
    labelentry3.grid(row=0,column=3, padx=10, pady=10, sticky="w")
    labelentry4 = Entry(f3)
    labelentry4.grid(row=1,column=3, padx=10, pady=10, sticky="w")
    labl8=Label(f3,font=('Calibri (Body)',12),text="User Name:",fg='black',bd=10)
    labl8.grid(row=2,column=0, padx=10, pady=10, sticky="w")
    labl9=Label(f3,font=('Calibri (Body)',12),text="Password:",fg='black',bd=10)
    labl9.grid(row=3,column=0, padx=10, pady=10, sticky="w")
    labelentry5 = Entry(f3)
    labelentry5.grid(row=2,column=3, padx=10, pady=10, sticky="w")
    labelentry6 = Entry(f3)
    labelentry6.grid(row=3,column=3, padx=10, pady=10, sticky="w")
    labl11=Label(f3,font=('Calibri (Body)',12),text="Contact no:",fg='black',bd=10)
    labl11.grid(row=0,column=9, padx=10, pady=10, sticky="w")
    labl12=Label(f3,font=('Calibri (Body)',12),text="E-mail:",fg='black',bd=10)
    labl12.grid(row=1,column=9, padx=10, pady=10, sticky="w")
    labelentry7 = Entry(f3)
    labelentry7.grid(row=0,column=12, padx=10, pady=10, sticky="w")
    labelentry8 = Entry(f3)
    labelentry8.grid(row=1,column=12, padx=10, pady=10, sticky="w")
    labl13=Label(f3,font=('Calibri (Body)',12),text="Address:",fg='black',bd=10)
    labl13.grid(row=2,column=9, padx=10, pady=10, sticky="w")
    labl14=Label(f3,font=('Calibri (Body)',12),text="Confirm password:",fg='black',bd=10)
    labl14.grid(row=3,column=9, padx=10, pady=10, sticky="w")
    labelentry9 = Entry(f3)
    labelentry9.grid(row=2,column=12, padx=10, pady=10, sticky="w")
    labelentry10 = Entry(f3)
    labelentry10.grid(row=3,column=12, padx=10, pady=10, sticky="w")
    btn5 =Button(f3, text="Back",font=('Calibri (Body)',12),fg='black',bd=10,command=Back_for_reg)
    btn5.grid(row=5,column=2, padx=10, pady=10, sticky="w")
    btn6 =Button(f3,font=('Calibri (Body)',12),text="Register",fg='black',bd=10,command=becoming_user)
    btn6.grid(row=5,column=12, padx=10, pady=10, sticky="w")
    windoows.mainloop()


#It check if all the data entered by the teacher meets the requirement, if it does then it enters their username and password in database1 and make them user.
#It also creates a notepad with all the correct information.
def becoming_user():
    first_name=labelentry3.get()
    last_name=labelentry4.get()
    usr_name=labelentry5.get()
    paswrd=labelentry6.get()
    contact_no=labelentry7.get()
    Email_address=labelentry8.get()
    Address=labelentry9.get()
    x=labelentry10.get()
    c.execute('SELECT * FROM Users WHERE(usernames)=(?)',(usr_name,));
    dat= c.fetchall()
    if dat!=[]:
        tkinter.messagebox.showinfo("Error","Username already exists")
        return
    elif first_name=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif last_name=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif usr_name=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif paswrd=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif contact_no=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif Email_address=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif Address=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif x=="":
        tkinter.messagebox.showinfo("Error","please fill all the requirements")
        return
    elif x!=paswrd:
        tkinter.messagebox.showinfo("Error","your passwords are not matching")
        return
    else:
        windoows.destroy()
        c.execute("INSERT INTO Users(usernames,passwords) VALUES (?, ?)",(usr_name, paswrd,))
        conn.commit()
        file=open(usr_name+".txt","w")
        file.write(str("First Name :                     | "+first_name+'\n'))
        file.write(str("Last Name :                      | "+last_name+'\n'))
        file.write(str( "User Name:                      | "+usr_name+'\n'))
        file.write(str("the password:                    | "+paswrd+'\n'))
        file.write(str("Contact Number of the user:      | "+contact_no+'\n'))
        file.write(str("E-mail Address:                  | "+Email_address+'\n'))
        file.write(str("Address:                         | "+Address+'\n'))
        file.write(str("confirm password:                | "+x+'\n'))
        file.close()
        tkinter.messagebox.showinfo("Welcome","you are member now!!!")

#This function deletes the registeration window when back button is clicked on registration window.
def Back_for_reg():
    windoows.destroy()
    

#This function creates the table which represent visual representation of teachers entries on database 4.
#It creates a window first then creates a table on it using frame.
def access_file1():
    cooo.execute("select * from View")
    dataf = {}
    master = Tk()
    master.geometry('600x450+500+110')
    master.title('Sign in system')
    tframe = Frame(master)
    tframe.pack()
    data= cooo.fetchall()
    row = 0
    for column in data:
        row = row + 1
        for y in column:
            dataf.update({column: {'Username': column[0], 'Signed in Time': column[1], 'Signed out Time':column[2]}})
    table = TableCanvas(tframe,data=dataf)
    table.show()    
#This function creates a CSV file by copying all the entries of database 3
def access_file(): 
    coo.execute("select * from Signed_in")
    data= coo.fetchall()
    with open ('signed_in.csv','w',newline='') as f_handle:
        writer=csv.writer(f_handle)
        header=['Usernames','Sign in time','Sign out time']
        writer.writerow(header)
        for row in data:
            writer.writerow(row)            
#This function performs no action.
def disable_event():
    pass  
#This is main window with 2 enitries, 4 labels, 2 buttons and a logo
#It also has a submenu and each submenu has different function assigned to it.
windows=Tk()
windows.geometry('375x420+500+110')
windows.resizable(width=False, height=False)
windows.title('Sign in system')
windows.protocol("WM_DELETE_WINDOW", disable_event)
mainMenu=Menu(windows)
windows.configure(menu=mainMenu)
subMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Extra", menu= subMenu)
subMenu.add_command(label= "Registration",command=register)
subMenu.add_command(label= "Access Details",command=access_file1)
subMenu.add_command(label= "Admin",command=Administrator)
windows.title('Sign in system')
photo =PhotoImage(file='London-Academy.png')
labl=Label(windows, image=photo)
labl.pack(side=TOP)
lablinfo=Label(windows,font=('Calibri (Body)',20,'bold'),text="Sign in",fg='black',bd=10)
lablinfo.pack(side=TOP)
labl1info=Label(windows,font=('Calibri (Body)',12),text="Using your employee's ID",fg='black',bd=10)
labl1info.pack(side=TOP)
f1 =Frame(windows, width =375, height= 300,relief=SUNKEN)
f1.pack(side=LEFT)
labl1=Label(f1,font=('Calibri (Body)',12),text="User Name:",fg='black',bd=10)
labl1.grid(row=0,column=0, padx=10, pady=10, sticky="w")
labl12=Label(f1,font=('Calibri (Body)',12),text="Password:",fg='black',bd=10)
labl12.grid(row=1,column=0, padx=10, pady=10, sticky="w")
labelentry1 = Entry(f1)
labelentry1.grid(row=0,column=3, padx=10, pady=10, sticky="w")
labelentry2 = Entry(f1)
labelentry2.grid(row=1,column=3, padx=10, pady=10, sticky="w")
btn =Button(f1, text="Sign in",font=('Calibri (Body)',12),fg='black',bd=10,command=signing_in)
btn.grid(row=3,column=3, padx=10, pady=10, sticky="w")
btn1 =Button(f1,font=('Calibri (Body)',12),text="Sign out",fg='black',bd=10,command=sign_out)
btn1.grid(row=3,column=6, padx=10, pady=10, sticky="w")
windows.mainloop()






