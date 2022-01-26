
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image


root=Tk()
root.title("Registration Form")
root.geometry("400x400")
root.iconbitmap('C:\python\Front End\HY.ico')
def register():
    name=name_info.get()
    Com_Name=company_info.get()
    phone=Phone_info.get()
    email=Email_info.get()
    Address=Address_info.get()

    if name=="":
        messagebox.showerror("Error","Please enter your name")
    elif Com_Name=="":
        messagebox.showerror("Error","Please enter your company name")
    elif phone=="":
        messagebox.showerror("Error","Please enter your phonenumber")
    elif email=="":
        messagebox.showerror("Error","Please enter your email")
    elif Address=="":
        messagebox.showerror("Error","please enter your address")
    else:
        Label(root,text="Registration Successfull",font="20",fg="blue").place(x=135,y=285)
    with open(name+"file.txt","w")as f:
        f.write(name+"\n")
        f.write(Com_Name+"\n")
        f.write(phone+"\n")
        f.write(email+"\n")
        f.write(Address+"\n")
def clear():
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
#label
Label(root,text="Inventory Management System",font="ariel 20 bold",bg="black",fg="white").pack(fill="both")
Label(root,text="Register",font="ariel 20 bold",bd=5,bg="white",fg="black").pack()
Label(root,text='Name',font="20").place(x=40,y=75)
Label(root,text='Com_Name',font="20").place(x=40,y=115)
Label(root,text='Phone NO.',font="20").place(x=40,y=155)
Label(root,text='Email Id',font="20").place(x=40,y=195)
Label(root,text='Address',font="20").place(x=40,y=240)

#entry
name_info=StringVar()
company_info=StringVar()
Phone_info=StringVar()
Email_info=StringVar()
Address_info=StringVar()
e=Entry(root,font="10",bd=5,textvariable=name_info)
e.place(x=140,y=75)
e1=Entry(root,font="10",bd=5,textvariable=company_info)
e1.place(x=140,y=115)
e2=Entry(root,font="10",bd=5,textvariable=Phone_info)
e2.place(x=140,y=155)
e3=Entry(root,font="10",bd=5,textvariable=Email_info)
e3.place(x=140,y=195)
e4=Entry(root,font="10",bd=5,textvariable=Address_info)
e4.place(x=140,y=240)


#Buttom
Button(root,text="Register",font="20",command=register).place(x=172,y=300)
Button(root,text="Clear",font="20",command=clear).place(x=200,y=400)
my_image = ImageTk.PhotoImage(Image.open('C:\python\Front End\IMSS.png'))
my_label = Label(image= my_image)
my_label.pack()
mainloop()