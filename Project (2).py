from tkinter import *
from tkinter import messagebox
from datetime import date

root=Tk()
root.title("graphical user interface")
root.geometry("1080x720")

def age():
    today = date.today()
    c = year.get()
    d = month.get()
    e = day.get()
    date_of_birth1=int(c)
    date_of_birth2=int(d)
    date_of_birth3=int(e) 
    if (date_of_birth2 > 13):
        messagebox.showwarning("Invalid Input","Month must be in 1-12")
    else:
        pass

    if (date_of_birth3>31):
        messagebox.showwarning("Invalid Input","Write valid Day")
    else:
        pass

    age = today.year - date_of_birth1 - ((today.month, today.day) < (date_of_birth2,date_of_birth3))
    f = int(age)
    if f<0:
        messagebox.showwarning("Invalid Input","Cannot Possible")

    else:
        age_label = Label(root,text=f)
        age_label.grid(row=7,column=1) 
        
def user_birthday():
    today = date.today()
    c = year.get()
    d = month.get()
    e = day.get()
    date_of_birth1=int(c)
    date_of_birth2=int(d)
    date_of_birth3=int(e)
    # if (date_of_birth2 > 13):
    #     messagebox.showwarning("Invalid Input","Month must be in 1-12")
    # else:
    #     pass

    # if (date_of_birth3>31):
    #     messagebox.showwarning("Invalid Input","Write valid Day")
    # else:
    #     pass

    date_of_birth = date(date_of_birth1,date_of_birth2,date_of_birth3)
    birthday = date(today.year, date_of_birth.month, date_of_birth.day)
    days_until_birthday = (birthday-today).days

    if days_until_birthday > 0:
        days_until_birthday_label = Label(root,text=f"There are {days_until_birthday} days left for your birthday!")
        days_until_birthday_label.grid(row=8,column=1) 

    elif days_until_birthday == 0:
        days_until_birthday_label = Label(root,text="Happy Birthday!")
        days_until_birthday_label.grid(row=8,column=1) 
    else:
        days_until_birthday_label = Label(root,text="You'll have to wait next year until your birthday")
        days_until_birthday_label.grid(row=8,column=1) 

def popup1():
        try:
            if len(f_name.get()) == 0:
                messagebox.showwarning("Invalid Input","Write first name")
            elif len(l_name.get()) == 0:
                messagebox.showwarning("Invalid Input","Write last name")
            elif len(year.get()) == 0:
                messagebox.showwarning("Invalid Input","Write year")
            elif len(month.get()) == 0:
                messagebox.showwarning("Invalid Input","Write month")
            elif len(day.get()) == 0:
                messagebox.showwarning("Invalid Input","Write day")
            else:
                submit()

        except:
            submit()

def submit():
    age()
    user_birthday()

f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
global a
global b
global c
global d
global e
a=f_name.get()
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
b=l_name.get()
year = Entry(root,width=30)
year.grid(row=3,column=1,padx=20)
c=year.get()
month = Entry(root,width=30)
month.grid(row=4,column=1,padx=20) 
d=month.get()
day = Entry(root,width=30)
day.grid(row=5,column=1,padx=20)
e=day.get()

f_name_label = Label(root,text="First Name:")
f_name_label.grid(row=0,column=0,pady=(10,0)) 
l_name_label = Label(root,text="Last Name:")
l_name_label.grid(row=1,column=0) 
dob_label = Label(root,text="Date of Birth")
dob_label.grid(row=2,column=1) 

birth_year_label = Label(root,text="Year:")
birth_year_label.grid(row=3,column=0) 
birth_month_label = Label(root,text="Month:")
birth_month_label.grid(row=4,column=0) 
birth_date_label = Label(root,text="Date:")
birth_date_label.grid(row=5,column=0) 
age_label = Label(root,text="Your age is:")
age_label.grid(row=7,column=0) 
days_until_birthday_label = Label(root,text="Days until birthday:")
days_until_birthday_label.grid(row=8,column=0) 

submit_button=Button(root,text="Submit",command=popup1)
submit_button.grid(row=6,column=1,padx=10,pady=10,ipadx=108 )
root.mainloop()