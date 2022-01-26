from tkinter import*
from turtle import width
from PIL import Image,ImageTk
from tkinter import ttk
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Immanent")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====================

        
        #all varaibles===
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()


        #====searchFrame===
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,bg="white",relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #==options==
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("times new roman",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #==title
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=950)

        #==content===
        #==row1==
        lbl_empid=Label(self.root,text="Emp ID",font=("times new roman",15),bg="white").place(x=50,y=200)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=350,y=200)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=750,y=200)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15),bg="white").place(x=150,y=200,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=450,y=200,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="white").place(x=850,y=200,width=180)

        #==row2==
        lbl_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=240)
        lbl_dob=Label(self.root,text="D.O.B",font=("times new roman",15),bg="white").place(x=350,y=240)
        lbl_doj=Label(self.root,text="D.O.J",font=("times new roman",15),bg="white").place(x=750,y=240)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="white").place(x=150,y=240,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="white").place(x=450,y=240,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="white").place(x=850,y=240,width=180)

        

        #==row3==
        lbl_email=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=280)
        lbl_pass=Label(self.root,text="Password",font=("times new roman",15),bg="white").place(x=350,y=280)
        lbl_utype=Label(self.root,text="User Type",font=("times new roman",15),bg="white").place(x=750,y=280)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="white").place(x=150,y=280,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("times new roman",15),bg="white").place(x=450,y=280,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=850,y=280,width=180)
        cmb_utype.current(0)

        #==row4==
        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=320)
        lbl_salary=Label(self.root,text="Salary",font=("times new roman",15),bg="white").place(x=500,y=320)

        self.txt_address=Text(self.root,font=("times new roman",15),bg="white")
        self.txt_address.place(x=150,y=320,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),bg="white").place(x=600,y=320,width=180)

        #==buttons==
        btn_add=Button(self.root,text="Save",font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=355,width=110,height=28)
        btn_update=Button(self.root,text="Update",font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=355,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",font=("times new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=355,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=355,width=110,height=28)


        #==Employee Details==

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
       
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
       
       
        self.EmployeeTable.pack(fill=BOTH,expand=1)

if __name__=="__main_":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()