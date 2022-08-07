import tkinter as tk
import sqlite3
  
root=tk.Tk()
root.geometry("600x200")

try:
    conn =  sqlite3.connect('test.db')
except Exception as e:
    print("Error in connecting",str(e))

c = conn.cursor()
  
name_var=tk.StringVar()
reg_var=tk.StringVar()
disp_output = ""
 
def submit():
 
    name=name_var.get()
    regnum=reg_var.get()
     
    print("The name is : " + name)
    print("The reg num is : " + regnum)

    c.execute("insert into student values ('"+name+"', "+regnum +")")
    conn.commit()
    print("Data inserted!")
    display()
    name_var.set("")
    reg_var.set("")

def display():
    disp_output=""
    for line in c.execute("select * from student"):
        disp_output+=str(line)
        disp_output+="\n"
    display_label = tk.Label(root,text= disp_output)
    display_label.grid(row=2,column=2)

def close():
    conn.close()
    root.destroy()    


name_label = tk.Label(root, text = 'Name', font=('calibre',15, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',15,'normal'))
  

reg_label = tk.Label(root, text = 'Reg No.', font = ('calibre',15,'bold'))
reg_entry=tk.Entry(root, textvariable = reg_var, font = ('calibre',15,'normal'))

sub_btn = tk.Button(root,text = 'Submit', command = submit)
close_btn = tk.Button(root,text='Close',command = close)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
reg_label.grid(row=1,column=0)
reg_entry.grid(row=1,column=1)
sub_btn.grid(row=0,column=2)
close_btn.grid(row=1,column=2)

display()

root.mainloop()
