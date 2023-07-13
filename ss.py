from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import Entry
from PIL import Image, ImageTk

def on_resize(event):
    image = bgimg.resize((event.width, event.height), Image.ANTIALIAS)
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)


root = Tk()
root.title("Supermart Database")
root.geometry('1350x750+0+0')
bgimg = Image.open('157.jpg') 
l = Label(root)
l.place(x=0, y=0, relwidth=1, relheight=1) 
l.bind('<Configure>', on_resize)



def admin():
    global top
    top=Tk()
    top.title('Supermart Employee Database')
    top.geometry("850x950")
    top.configure(bg='powder blue')

    conn=sqlite3.connect('test2.db')
    c = conn.cursor()
    '''
    c.execute("""CREATE TABLE Employee(
        first_name text,
        last_name text,
        Gender text,
        Position text,
        address text,
        City text,
        State text,
        Salary int
        )""")
    '''
    def update():
        conn=sqlite3.connect('test2.db')
        c = conn.cursor()

        record_id=delete_box.get()

        c.execute("""UPDATE Employee SET
            first_name=:first,
            last_name=:last,
            Gender=:Gender,
            Position=:Position,
            address=:address,
            City=:City,
            State=:State,
            Salary=:Salary

            WHERE oid=:oid""",
            {'first':f_name_editor.get(),
             'last':l_name_editor.get(),
             'Gender':Gender_editor.get(),
             'Position':Position_editor.get(),
             'address':address_editor.get(),
             'City':City_editor.get(),
             'State':State_editor.get(),
             'Salary':Salary_editor.get(),
             'oid':record_id
                
            })

        conn.commit()

        conn.close()
        
        editor.destroy()


    def edit():
        global editor
        editor = Tk()
        editor.title("Update a Record")
        editor.geometry('900x700')
        editor.configure(bg='#f5d284')
        conn=sqlite3.connect('test2.db')
        c = conn.cursor()
        record_id=delete_box.get()
        c.execute("SELECT * FROM Employee WHERE oid="+ record_id)
        records=c.fetchall()

        global f_name_editor
        global l_name_editor
        global Gender_editor
        global Position_editor
        global address_editor
        global City_editor
        global State_editor
        global Salary_editor
        
        
        f_name_editor = Entry(editor,width=40)
        f_name_editor.place(x=460,y=10)
        l_name_editor = Entry(editor,width=40)
        l_name_editor.place(x=460,y=60)
        Gender_editor=Entry(editor,width=40)
        Gender_editor.place(x=460,y=110) 
        Position_editor = Entry(editor,width=40)
        Position_editor.place(x=460,y=160)
        address_editor = Entry(editor,width=40)
        address_editor.place(x=460,y=210)
        City_editor = Entry(editor,width=40)
        City_editor.place(x=460,y=260)
        State_editor = Entry(editor,width=40)
        State_editor.place(x=460,y=310)
        Salary_editor = Entry(editor,width=40)
        Salary_editor.place(x=460,y=360)


        f_name_label = Label(editor,text="First name", borderwidth=1,width=40, relief="groove",font='Times')
        f_name_label.place(x=3,y=10)
        l_name_label = Label(editor,text="Last name", borderwidth=1,width=40, relief="groove",font='Times')
        l_name_label.place(x=3,y=60)
        f_name_label = Label(editor,text="Gender", borderwidth=1,width=40, relief="groove",font='Times')
        f_name_label.place(x=3,y=110)
        f_name_label = Label(editor,text="Position", borderwidth=1,width=40, relief="groove",font='Times')
        f_name_label.place(x=3,y=160)
        address_label = Label(editor,text="Address", borderwidth=1,width=40, relief="groove",font='Times')
        address_label.place(x=3,y=210)
        City_label = Label(editor,text="City", borderwidth=1,width=40, relief="groove",font='Times')
        City_label.place(x=3,y=260)
        State_label = Label(editor,text="State", borderwidth=1,width=40, relief="groove",font='Times')
        State_label.place(x=3,y=310)
        Salary_label = Label(editor,text="Salary", borderwidth=1,width=40, relief="groove",font='Times')
        Salary_label.place(x=3,y=360)
        
        Save_btn = Button(editor,text="Save Record",command=update,width=70,font='Times')
        Save_btn.place(x=30,y=410)

        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            Gender_editor.insert(0, record[2])
            Position_editor.insert(0, record[3])
            address_editor.insert(0, record[4])
            City_editor.insert(0, record[5])
            State_editor.insert(0, record[6])
            Salary_editor.insert(0, record[7])

        
    def delete():
        conn=sqlite3.connect('test2.db')
        c = conn.cursor()

        c.execute("DELETE from Employee WHERE oid="+delete_box.get())

        delete_box.delete(0, END)

        
        conn.commit()


        conn.close()

    def submit():
        conn=sqlite3.connect('test2.db')
        c = conn.cursor()
        c.execute("INSERT INTO Employee VALUES (:f_name, :l_name,:Gender,:Position, :address, :City, :State, :Salary)",
                {

                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'Gender':Gender.get(),
                    'Position':Position.get(),
                    'address':address.get(),
                    'City':City.get(),
                    'State':State.get(),
                    'Salary':Salary.get()
                })         
     

        conn.commit()


        conn.close()
    
        #clear the textboxes
        f_name.delete(0,END)
        l_name.delete(0,END)
        Gender.delete(0,END)
        Position.delete(0,END)
        address.delete(0,END)
        City.delete(0,END)
        State.delete(0,END)
        Salary.delete(0,END)


        
    def query():
        dif=Tk()
        conn=sqlite3.connect('test2.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM Employee")
        records=c.fetchall()
        #print(records)
        listbox = Listbox(dif,bd = 10, fg = "black", font = "Times", cursor = "target")
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(dif)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        
        print_records=''
        for record in records:
                print_records=str(record[0])+" "+str(record[1])+" "+"\t"+str(record[8]) + "\n"
                listbox.insert(END,print_records)
        
        
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        '''
        query_label= Label(top,text=print_records,font='Times 15')
        query_label.place(x=300, y=710)

        '''
        conn.commit()


        conn.close()



    f_name = Entry(top,width=50,relief="solid")
    f_name.place(x=460,y=10)
    l_name = Entry(top,width=50, relief="solid")
    l_name.place(x=460,y=60)
    my_str_var = StringVar()
    Gender=ttk.Combobox(top, textvariable = my_str_var,width=50,state="readonly",
    values=["MALE", "FEMALE", "OTHER"])
    Gender.place(x=460,y=110)
    my_str_var1 = StringVar()
    Position = ttk.Combobox(top, textvariable= my_str_var1,width=50,state="readonly",
    values=["Manager","Floor Manager","Senior Employee","Junior Employee","Administration"])
    Position.place(x=460,y=160)
    address = Entry(top,width=50, relief="solid")
    address.place(x=460,y=210)
    City = Entry(top,width=50, relief="solid")
    City.place(x=460,y=260)
    State = Entry(top,width=50, relief="solid")
    State.place(x=460,y=310)
    Salary = Entry(top,width=50, relief="solid")
    Salary.place(x=460,y=360)

    delete_box = Entry(top,width=40, relief="solid")
    delete_box.place(x=460,y=510)

    f_name_label = Label(top,text="First name", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    f_name_label.place(x=10,y=10)
    l_name_label = Label(top,text="Last name", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    l_name_label.place(x=10,y=60)
    Gender_label = Label(top,text="Gender", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Gender_label.place(x=10,y=110)
    Position_label = Label(top,text="Position", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Position_label.place(x=10,y=160)
    address_label = Label(top,text="Address", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    address_label.place(x=10,y=210)
    City_label = Label(top,text="City", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    City_label.place(x=10,y=260)
    State_label = Label(top,text="State", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    State_label.place(x=10,y=310)
    Salary_label = Label(top,text="Salary", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Salary_label.place(x=10,y=360)
    
    delete_label = Label(top,text="Select ID ", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    delete_label.place(x=10,y=510)
    

    submit_btn = Button(top,text="Add to DataBase",command=submit,width=70,bg='white',font='Times')
    submit_btn.place(x=30,y=410)

    query_btn = Button(top,text="Show Records",command=query,width=70,bg='white',font='Times')
    query_btn.place(x=30,y=460)

    delete_btn = Button(top,text="Delete ID",command=delete,width=70,bg='white',font='Times')
    delete_btn.place(x=30,y=560)

    edit_btn = Button(top,text="Edit Records",command=edit,width=70,bg='white',font='Times')
    edit_btn.place(x=30,y=610)

    
    conn.commit()

    conn.close()
    top.mainloop()


def Inventory():
    mid=Tk()
    mid.title("Inventory Database")
    mid.geometry("850x900")
    mid.configure(bg='#b8bc86')

    conn = sqlite3.connect('test3.db')
    c=conn.cursor()
    '''
    c.execute("""CREATE TABLE inventory(
            ID int,
            name text,
            Supplier text,
            Expdate text,
            Quantity int,
            Itemtype text,
            ItemCost int
            )""")
    '''

    def update():
        conn=sqlite3.connect('test3.db')
        c = conn.cursor()

        record_id=delete_box.get()

        c.execute("""UPDATE Inventory SET
            ID=:ID,
            name=:name,
            Supplier=:Supplier,
            Expdate=:Expdate,
            Quantity=:Quantity,
            Itemtype=:Itemtype,
            ItemCost=:ItemCost
            
            WHERE ID=:record_id""",
            {'name':name_editor.get(),
             'Supplier':Supplier_editor.get(),
             'Expdate':Expdate_editor.get(),
             'Quantity':Quantity_editor.get(),
             'Itemtype':Itemtype_editor.get(),
             'ItemCost':ItemCost_editor.get(),
             'ID':ID_editor.get()
             
                
            })

    

            
    def edit():
        global editor
        editor = Tk()
        editor.title("Update a Record")
        editor.geometry('800x600')
        editor.configure(bg='#f5d284')
        conn=sqlite3.connect('test3.db')
        c = conn.cursor()
        record_id=delete_box.get()
        c.execute("SELECT * FROM Inventory WHERE ID="+ record_id)
        records=c.fetchall()

        global ID_editor
        global name_editor
        global Supplier_editor
        global Expdate_editor
        global Quantity_editor
        global Itemtype_editor
        global Itemcost_editor

        ID_editor = Entry(editor,width=50, relief="solid")
        ID_editor.place(x=460,y=10)
        name_editor = Entry(editor,width=50, relief="solid")
        name_editor.place(x=460,y=60)
        Supplier_editor = Entry(editor,width=50, relief="solid")
        Supplier_editor.place(x=460,y=110)
        Expdate_editor= Entry(editor,width=50, relief="solid")
        Expdate_editor.place(x=460,y=160)
        Quantity_editor = Entry(editor,width=50, relief="solid")
        Quantity_editor.place(x=460,y=210)
        Itemtype_editor= Entry(editor,width=50, relief="solid")
        Itemtype_editor.place(x=460,y=260)
        ItemCost_editor= Entry(editor,width=50, relief="solid")
        ItemCost_editor.place(x=460,y=310)

        
        ID_label = Label(editor,text="ID", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        ID_label.place(x=10,y=10)
        name_label = Label(editor,text=" Name", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        name_label.place(x=10,y=60)
        Supplier_label = Label(editor,text="Supplier", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Supplier_label.place(x=10,y=110)
        Expdate_label = Label(editor,text="Expdate", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Expdate_label.place(x=10,y=160)
        Quantity_label = Label(editor,text="Quantity", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Quantity_label.place(x=10,y=210)
        Itemtype_label = Label(editor,text="Item type", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Itemtype_label.place(x=10,y=260)
        ItemCost_label = Label(editor,text="Item cost", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        ItemCost_label.place(x=10,y=310)

        Save_btn = Button(editor,text="Save Record",command=update,width=70,font='Times')
        Save_btn.place(x=30,y=360)

        for record in records:
            ID_editor.insert(0, record[0])
            name_editor.insert(0, record[1])
            Supplier_editor.insert(0, record[2])
            Expdate_editor.insert(0, record[3])
            Quantity_editor.insert(0, record[4])
            Itemtype_editor.insert(0, record[5])
            ItemCost_editor.insert(0, record[6])
            
            
            
           
    def delete():
        conn=sqlite3.connect('test3.db')
        c = conn.cursor()
        c.execute("DELETE from Inventory WHERE ID="+delete_box.get())
        
        '''
        c.execute("UPDATE Inventory SET Quantity=Quantity-deletequan WHERE ID="+delete_box.get())
        '''
        delete_box.delete(0,END)

        
        conn.commit()


        conn.close()

        
    


    def submit():
        conn=sqlite3.connect('test3.db')
        c= conn.cursor()
        c.execute("INSERT INTO Inventory VALUES (:ID, :name,:Supplier,:Expdate,:Quantity,:Itemtype,:ItemCost)",
                {

                    'ID':ID.get(),
                    'name':name.get(),
                    'Supplier':Supplier.get(),
                    'Expdate':Expdate.get(),
                    'Quantity':Quantity.get(),
                    'Itemtype':Itemtype.get(),
                    'ItemCost':ItemCost.get(),
                    
                    
                })         
     

        conn.commit()


        conn.close()
    
        #clear the textboxes
        ID.delete(0,END)
        name.delete(0,END)
        Supplier.delete(0,END)
        Expdate.delete(0,END)
        '''
        Quantity.delete(0,END)
        '''
        Itemtype.delete(0,END)
        ItemCost.delete(0,END)


    def query():
        bcd=Tk()
        conn=sqlite3.connect('test3.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Inventory")
        records=c.fetchall()
        #print(records)
        listbox = Listbox(bcd,bd = 10, fg = "black", font = "Times", cursor = "target")
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(bcd)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        
        print_records=''
        for record in records:
            print_records=str(record[1])+" "+"\t"+str(record[0]) + "\n"
            listbox.insert(END,print_records)
            

        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        '''
        query_label= Label(mid,text=print_records,font='Times 15')
        query_label.place(x=300, y=710)
        '''
        conn.commit()


        conn.close()
    



    ID = Entry(mid,width=50, relief="solid")
    ID.place(x=460,y=10)
    name = Entry(mid,width=50, relief="solid")
    name.place(x=460,y=60)
    Supplier = Entry(mid,width=50, relief="solid")
    Supplier.place(x=460,y=110)
    Expdate= Entry(mid,width=50, relief="solid")
    Expdate.place(x=460,y=160)
    '''
    Quantity = Entry(mid,width=50, relief="solid")
    Quantity.place(x=400,y=210)
    '''
    Quantity = Scale(mid,from_=0,to_=200,length=250,resolution=1,orient=HORIZONTAL)
    Quantity.place(x=460,y=210)
    my_str_var=StringVar()
    Itemtype= ttk.Combobox(mid, textvariable = my_str_var,width=50,state="readonly",
    values=["Snacks", "Essentials", "Beverages","Hygiene","Meat","Stationary","Grocery"])
    Itemtype.place(x=460,y=260)
    ItemCost= Entry(mid,width=50, relief="solid")
    ItemCost.place(x=460,y=310)
    

    delete_box = Entry(mid,width=40, relief="solid")
    delete_box.place(x=460,y=460)

    ID_label = Label(mid,text="ID", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    ID_label.place(x=10,y=10)
    name_label = Label(mid,text=" Name", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    name_label.place(x=10,y=60)
    Supplier_label = Label(mid,text="Supplier", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Supplier_label.place(x=10,y=110)
    Expdate_label = Label(mid,text="Expdate", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Expdate_label.place(x=10,y=160)
    Quantity_label = Label(mid,text="Quantity", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Quantity_label.place(x=10,y=210)
    Itemtype_label = Label(mid,text="Item type", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Itemtype_label.place(x=10,y=260)
    ItemCost_label = Label(mid,text="Item Cost", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    ItemCost_label.place(x=10,y=310)
    
    delete_label = Label(mid,text="Select ID ", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    delete_label.place(x=10,y=460)
    

    submit_btn = Button(mid,text="Add to DataBase",command=submit,width=70,bg='white',font='Times')
    submit_btn.place(x=30,y=360)

    query_btn = Button(mid,text="Show Records",command=query,width=70,bg='white',font='Times')
    query_btn.place(x=30,y=410)


    edit_btn = Button(mid,text="Edit Records",command=edit,width=70,bg='white',font='Times')
    edit_btn.place(x=30,y=510)

    conn.commit()

    conn.close()


    mid.mainloop()

def Customer():
    global down
    down=Tk()
    down.title("Customer Database")
    down.geometry("850x900")
    down.configure(bg='#CBC3E3')

    conn = sqlite3.connect('test4.db')
    c=conn.cursor()

    
    '''
    c.execute("""CREATE TABLE Customer(
            name text,
            Address text,
            City text,
            State text,
            Gender text,
            Experience int,
            PhoneNo int,
            Email text
            )""")

    '''

    
    def update():
        conn=sqlite3.connect('test4.db')
        c = conn.cursor()

        record_id=delete_box.get()

        c.execute("""UPDATE Customer SET
            name=:name,
            Address=:Address,
            City=:City,
            State=:State,
            Gender=:Gender,
            Experience=:Experience,
            PhoneNo=:PhoneNo,
            Email=:Email

            WHERE oid=:oid""",
            {'name':name_editor.get(),
             'Address':Address_editor.get(),
             'City':City_editor.get(),
             'State':State_editor.get(),
             'Gender':Gender_editor.get(),
             'Experience':Experience_editor.get(),
             'PhoneNo':PhoneNo_editor.get(),
             'Email':Email_editor.get(),
             'oid':record_id
                
            })

        conn.commit()


        conn.close()
        
        editor.destroy()

    

    

    def edit():
        global editor
        editor = Tk()
        editor.title("Update a Record")
        editor.geometry('800x600')
        editor.configure(bg='#f5d284')
        conn=sqlite3.connect('test4.db')
        c = conn.cursor()
        record_id=delete_box.get()
        c.execute("SELECT * FROM Customer WHERE oid="+ record_id)
        records=c.fetchall()

        global name_editor
        global Address_editor
        global City_editor
        global State_editor
        global Gender_editor
        global Experience_editor
        global PhoneNo_editor
        global Email_editor

        name_editor = Entry(editor,width=50, relief="solid")
        name_editor.place(x=460,y=10)
        Address_editor = Entry(editor,width=50, relief="solid")
        Address_editor.place(x=460,y=60)
        City_editor = Entry(editor,width=50, relief="solid")
        City_editor.place(x=460,y=110)
        State_editor = Entry(editor,width=50, relief="solid")
        State_editor.place(x=460,y=160)
        Gender_editor=Entry(editor,width=50, relief="solid")
        Gender_editor.place(x=460,y=210)
        Experience_editor = Entry(editor,width=50, relief="solid")
        Experience_editor.place(x=460,y=260)
        PhoneNo_editor = Entry(editor,width=50, relief="solid")
        PhoneNo_editor.place(x=460,y=310)
        Email_editor= Entry(editor,width=50, relief="solid")
        Email_editor.place(x=460,y=360)
        

        name_label = Label(editor,text="Name", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        name_label.place(x=10,y=10)
        Address_label = Label(editor,text="Address", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Address_label.place(x=10,y=60)
        City_label = Label(editor,text="City", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        City_label.place(x=10,y=110)
        State_label = Label(editor,text="State", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        State_label.place(x=10,y=160)
        Gender_label = Label(editor,text="Gender", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Gender_label.place(x=10,y=210)
        Experience_label = Label(editor,text="Experience", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Experience_label.place(x=10,y=260)
        PhoneNo_label = Label(editor,text="PhoneNo", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        PhoneNo_label.place(x=10,y=310)
        Email_label = Label(editor,text="Email", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
        Email_label.place(x=10,y=360)

        Save_btn = Button(editor,text="Save Record",command=update,width=70,font='Times')
        Save_btn.place(x=30,y=410)

        for record in records:
            name_editor.insert(0, record[0])
            Address_editor.insert(0, record[1])
            City_editor.insert(0, record[2])
            State_editor.insert(0, record[3])
            Gender_editor.insert(0, record[4])
            Experience_editor.insert(0, record[5])
            PhoneNo_editor.insert(0, record[6])
            Email_editor.insert(0, record[7])

        

    

    def delete():
        conn=sqlite3.connect('test4.db')
        c = conn.cursor()

        c.execute("DELETE from Customer WHERE oid="+delete_box.get())

        delete_box.delete(0, END)

        
        conn.commit()


        conn.close()


    def submit():
        conn=sqlite3.connect('test4.db')
        c = conn.cursor()
        c.execute("INSERT INTO Customer VALUES (:name,:Address,:City,:Gender, :State,:Experience,:PhoneNo,:Email)",
                {

                    'name':name.get(),
                    'Address':Address.get(),
                    'City':City.get(),
                    'State':State.get(),
                    'Gender':Gender.get(),
                    'Experience':Experience.get(),
                    'PhoneNo':PhoneNo.get(),
                    'Email':Email.get(),
                    
                })         
     

        conn.commit()


        conn.close()
    
        #clear the textboxes
        name.delete(0,END)
        Address.delete(0,END)
        City.delete(0,END)
        State.delete(0,END)
        Gender.delete(0,END)
        Experience.delete(0,END)
        PhoneNo.delete(0,END)
        Email.delete(0,END)


        
    def query():
        abc=Tk()
        conn=sqlite3.connect('test4.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM Customer")
        records=c.fetchall()
        #print(records)
        listbox = Listbox(abc,bd = 10, fg = "black", font = "Times", cursor = "target")
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(abc)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        
        print_records=''
        for record in records:
            print_records=str(record[0])+"\t"+str(record[8]) + "\n"
            listbox.insert(END,print_records)
            

        listbox.config(yscrollcommand = scrollbar.set)
          
        scrollbar.config(command = listbox.yview)
        '''
        query_label= Label(down,text=print_records,font='Times 15')
        query_label.place(x=300, y=710)
        '''
        conn.commit()


        conn.close()

    name = Entry(down,width=50, relief="solid")
    name.place(x=460,y=10)
    Address = Entry(down,width=50, relief="solid")
    Address.place(x=460,y=60)
    City = Entry(down,width=50, relief="solid")
    City.place(x=460,y=110)
    State = Entry(down,width=50, relief="solid")
    State.place(x=460,y=160)
    my_str_var = StringVar()
    Gender=ttk.Combobox(down, textvariable = my_str_var,width=50,state="readonly",
    values=["MALE", "FEMALE", "OTHER"])
    Gender.place(x=460,y=210)
    my_str_var1 = StringVar()
    Experience = ttk.Combobox(down, textvariable = my_str_var1,width=50,state="readonly",
    values=["EXCELLENT :):)","GOOD :)", "AVERAGE :|", "BAD :(","WORST *_*"])
    Experience.place(x=460,y=260)
    PhoneNo = Entry(down,width=50, relief="solid")
    PhoneNo.place(x=460,y=310)
    Email= Entry(down,width=50, relief="solid")
    Email.place(x=460,y=360)

    delete_box = Entry(down,width=40, relief="solid")
    delete_box.place(x=460,y=510)

    
    name_label = Label(down,text="Name", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    name_label.place(x=10,y=10)
    Address_label = Label(down,text="Address", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Address_label.place(x=10,y=60)
    City_label = Label(down,text="City", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    City_label.place(x=10,y=110)
    State_label = Label(down,text="State", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    State_label.place(x=10,y=160)
    Gender_label = Label(down,text="Gender", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Gender_label.place(x=10,y=210)
    Experience_label = Label(down,text="Experience", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Experience_label.place(x=10,y=260)
    PhoneNo_label = Label(down,text="PhoneNo", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    PhoneNo_label.place(x=10,y=310)
    Email_label = Label(down,text="Email", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    Email_label.place(x=10,y=360)
    
    delete_label = Label(down,text="Select ID ", borderwidth=1,width=40,bg='white', relief="solid",font='Times')
    delete_label.place(x=10,y=510)
    
    submit_btn = Button(down,text="Add to DataBase",command=submit,width=70,bg='white',font='Times')
    submit_btn.place(x=30,y=410)
    
    query_btn = Button(down,text="Show Records",command=query,width=70,bg='white',font='Times')
    query_btn.place(x=30,y=460)
    
    delete_btn = Button(down,text="Delete ID",command=delete,width=70,bg='white',font='Times')
    delete_btn.place(x=30,y=560)
    
    edit_btn = Button(down,text="Edit Records",command=edit,width=70,bg='white',font='Times')
    edit_btn.place(x=30,y=610)
    
    conn.commit()
    conn.close()
    down.mainloop()



def viewRecords():
    global top
    view=Tk()
    view.title('Display RECORDS')
    view.geometry("1350x750+0+0")
    view.configure(bg='#CBC3E3')

    def viewCustomer():
        view1 = Tk()
        view1.title("View a Record")
        view1.geometry('1100x1100')
        conn=sqlite3.connect('test4.db')
        c = conn.cursor()
        r_set=conn.execute("SELECT * FROM Customer")
        i=0
        for Customer in r_set:
            for j in range(len(Customer)):
                e=Entry(view1,width=30,fg='blue')
                e.grid(row=i, column=j)
                e.insert(END,Customer[j])
            i=i+1

        conn.commit()


        conn.close()

    def viewInventory():
        view2 = Tk()
        view2.title("View a Record")
        view2.geometry('1100x1100')
        conn=sqlite3.connect('test3.db')
        c = conn.cursor()
        r_set=conn.execute("SELECT * FROM Inventory")
        i=0
        for Inventory in r_set:
            for j in range(len(Inventory)):
                e=Entry(view2,width=30,fg='blue')
                e.grid(row=i, column=j)
                e.insert(END,Inventory[j])
            i=i+1

        conn.commit()


        conn.close()

    def viewEmployee():
        view3 = Tk()
        view3.title("View a Record")
        view3.geometry('1100x1100')
        conn=sqlite3.connect('test2.db')
        c = conn.cursor()
        r_set=conn.execute("SELECT * FROM Employee")
        i=0
        for Employee in r_set:
            for j in range(len(Employee)):
                e=Entry(view3,width=30,fg='blue')
                e.grid(row=i, column=j)
                e.insert(END,Employee[j])
            i=i+1

        conn.commit()


        conn.close()

    
        
    btnn = Button(view, text="VIEW CUSTOMER RECORDS", command=viewCustomer, width=60, height=2, font='Impact', bg='powder blue',
             activebackground='white')

    btnn.place(x=450, y=300)

    btnn = Button(view, text="VIEW INVENTORY RECORDS", command=viewInventory, width=60, height=2, font='Impact', bg='powder blue',
             activebackground='white')

    btnn.place(x=450, y=400)

    btnn = Button(view, text="VIEW EMPLOYEE RECORDS", command=viewEmployee, width=60, height=2, font='Impact', bg='powder blue',
             activebackground='white')

    btnn.place(x=450, y=500)
    
        

      


btn = Button(root, text="ADMIN", command=admin, width=60, height=2, font='Impact', bg='powder blue',
             activebackground='white')

btn.place(x=450, y=200)

bnt1 = Button(root, text='INVENTORY', command=Inventory, width=60, height=2, font='Impact', bg='powder blue',
              activebackground='white')

bnt1.place(x=450, y=300)

bnt2 = Button(root, text='CUSTOMER', command=Customer, width=60, height=2, font='Impact', bg='powder blue',
              activebackground='white')

bnt2.place(x=450, y=400)

bnt3= Button(root, text='VIEW RECORDS', command=viewRecords, width=60, height=2, font='Impact', bg='powder blue',
              activebackground='white')

bnt3.place(x=450, y=500)



mainloop()
