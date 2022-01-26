from cProfile import label
from cgitb import text
from email.mime import image
from tkinter import*
from PIL import Image,ImageTk#pip install pillow
from employee import employeeClass
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
        lbl_menuLogo=Label(leftMenu)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu=Label(leftMenu,text="Menu",font=("times new roman",20),bg="#010c48").pack(side=TOP,fill=X)
        btn_employee=Button(leftMenu,text="Employee",command=self.employee,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(leftMenu,text="supplier",compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(leftMenu,text="Category",compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(leftMenu,text="Product",compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(leftMenu,text="Sales",compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(leftMenu,text="Exit",compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
           
        #content
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
 
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=300,y=300,height=150,width=300)

        self.lbl_products=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_products.place(x=650,y=300,height=150,width=300)
#====================================================================#

    def employee(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=employeeClass(self.new_win)



if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()     