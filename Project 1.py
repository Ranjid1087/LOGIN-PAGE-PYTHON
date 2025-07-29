from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector
import sys

win=tkinter.Tk()
sw=win.winfo_screenwidth()
sh=win.winfo_screenheight()
win.configure(width=sw,height=sh,bg='ORANGE')


'''path=Image.open("E://Pictures//image 1.PNG")
res=ImageTk.PhotoImage(path)
imglabel=tkinter.Label(win,image=res)
imglabel.place(x=840,y=160)'''


def login():
    con=mysql.connector.connect(host="localhost",user='root',password='12345',database='project')
    us_name=un_tb.get()
    ps_word=up_tb.get()
    u_name=us_name.strip()
    p_word=ps_word.strip()
    n=len(u_name)
    l=len(p_word)
    if l==0 or n==0:
        messagebox.showwarning("warning","USERNAME OR PASSWORD SHOULD NOT BE EMPTY")
        return
    cur=con.cursor()
    cur.execute("select * from details")
    alldata=cur.fetchall()
    for i in alldata:
        if u_name==i[0]:
            if p_word==i[1]:
                messagebox.showinfo('RESULT','Login Successful')
                clearfun()
                break
            else:
                messagebox.showinfo('Result',"Incorrect Password")
                up_tb.delete(0,'end')
                break
    else:
        messagebox.showerror('Result',"Invalid Username")
        clearfun()
    con.commit()
  
def signup(): 
    con=mysql.connector.connect(host="localhost",user='root',password='12345',database='project')
    us_name=un_tb.get()
    ps_word=up_tb.get()
    u_name=us_name.strip()
    p_word=ps_word.strip()
    n=len(u_name)
    l=len(p_word)
    if l==0 or n==0:
        messagebox.showwarning("warning","USERNAME OR PASSWORD SHOULD NOT BE EMPTY")
        return
    elif not(u_name.isupper()):
        messagebox.showwarning('Warning',"Please Use Only Capital Letters \n in UserName")
        return
    elif not(l>=8 and l<=12):
        messagebox.showwarning('Warning',"Password Must contain 8 to 12 characters")
        return
    else:
        pass

    a,b,c,d=0,0,0,0
    for j in p_word:
        if j>='A' and j<='Z':
            a=1
            continue
        if j>='a' and j<='z':
            b=1
            continue
        if j>='0' and j<='9':
            c=1
            continue
        if not((j>='A' and j<='Z') and (j>='a' and j<='z') and (j>='0' and j<='9')):
            d=1
            continue
    if a==1 and b==1 and c==1 and d==1:
        cur=con.cursor()
        cur.execute("select * from details")
        alldata=cur.fetchall()

        for k in alldata:
            if u_name==k[0] or (u_name==k[0] and p_word==k[1]):
                    messagebox.showwarning('Result',"Same Username and Password\n is already exist")
                    messagebox.showinfo('Suggestion',"Please choose another Username")
                    clearfun()
                    break
        else:
            cur=con.cursor()
            cur.execute("insert into details values('%s','%s')"%(u_name,p_word))
            messagebox.showinfo('Result',"Signup Successful")
        con.commit()
    else:
        messagebox.showwarning('Warning',"weak password,Please use strong password")
        up_tb.delete(0,"end")
def clearfun():
    un_tb.delete(0,'end')
    up_tb.delete(0,"end")
    un_tb.focus()

title=tkinter.Label(win,text="Signup/Login Page",bg='black',font=('Times',60),fg='white')
title.place(x=225,y=0)
un=tkinter.Label(win,text="User Name",bg='orange',font=('Times',15,'bold'))
un.place(x=365,y=200)
un_info=tkinter.Label(win,text="(All charecters must be caps)",bg='orange',font=('arial',8))
un_info.place(x=365,y=223)
un_tb=tkinter.Entry(win)
un_tb.place(x=580,y=210)
up=tkinter.Label(win,text="Password",bg='Orange',font=('Times',15,'bold'))
up.place(x=365,y=300)
up_info=tkinter.Label(win,text="(Use atleast one Caps & Small &\n Number and Special Character)",bg='orange',font=('arial',8))
up_info.place(x=365,y=323)
up_tb=tkinter.Entry(win)
up_tb.place(x=580,y=320)
login_button=tkinter.Button(win,text='Login',bg='Yellow',font=('Times',15),fg='black',command=login)
login_button.place(x=500,y=450)
Signup_button=tkinter.Button(win,text='Signup',bg='indigo',font=('Times',15),fg='white',command=signup)
Signup_button.place(x=560,y=450)
win.mainloop()
    
