from tkinter import*
from PIL import Image,ImageTk
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Immanent")
        self.root.config(bg="white")

        #title
        
        title=Label(self.root,text="Inventory Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

       #btn_logout
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor=("hand2")).place(x=1150,y=10,height=50,width=150)

       #clock
        self.lbl_clock=Label(self.root,text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

       #left menu
        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=102,width=209,height=565)


root=Tk()
obj=IMS(root)
root.mainloop()        
