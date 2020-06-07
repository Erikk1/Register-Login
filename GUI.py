import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import * 
import tkinter as tk




entry_1 = None;
entry_2 = None;
entry_3 = None;

class ForFrames(tk.Tk):
    
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)  
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (Registerform,Login):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Registerform")

     def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise() 

class Registerform(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller




            # convert registered userinfo to json file
        def regPress():
            usern = entry_1.get()
            passw = entry_2.get()
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            if entry_2.get() == entry_3.get() and not len(entry_1.get()) == 0:
                c.execute("CREATE TABLE IF NOT EXISTS 'entries' (username TEXT, password TEXT)")
                c.execute("INSERT INTO entries(username,password)VALUES(?,?)",(usern,passw))
                MsgBox = tkinter.messagebox.showinfo("Success","Registered, click OK to login")
                if MsgBox == 'ok':
                    controller.show_frame("Login")
            conn.commit()
            
            if entry_2.get() != entry_3.get():
                     tkinter.messagebox.showinfo("Failed","Passwords don't match")
            elif len(entry_1.get()) == 0:
                    tkinter.messagebox.showinfo("Failed","Please enter a username")

     

                
        registerframe1 = Frame(self)
        registerframe1.pack(fill=X)

        registerframe2 = Frame(self)
        registerframe2.pack(fill=X)

        registerframe3 = Frame(self)
        registerframe3.pack(fill=X)

        label_1 = tk.Label(registerframe1, text="Username")
        label_2 = tk.Label(registerframe2, text="Password")
        label_3 = tk.Label(registerframe3, text="Password confirmation")

        label_1.pack(side=LEFT,padx=5,pady=5)
        label_2.pack(side=LEFT,padx=5,pady=5)
        label_3.pack(side=LEFT,padx=5,pady=5)

        entry_1 = Entry(registerframe1, width=50)
        entry_2 = Entry(registerframe2, width=50, show='*')
        entry_3 = Entry(registerframe3, width=50, show='*')

        entry_1.pack(side=RIGHT,padx=100)
        entry_2.pack(side=RIGHT,padx=100)
        entry_3.pack(side=RIGHT,padx=100)
        
       


        #### nupud



        button1 = tk.Button(self, text="Register", command=regPress)
        button2 = tk.Button(self, text="Already have an account? Login",command=lambda: controller.show_frame("Login"))
        button2.pack(side=BOTTOM)
        button1.pack(side=TOP)
    


        

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #database
        def LogPress():
            usern = entry_1.get()
            passw = entry_2.get()
            if usern == '' or passw == '':
                tkinter.messagebox.showinfo("Failed","Please enter username and password")

            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("SELECT * FROM entries WHERE username = ? and password = ?",(usern,passw))
            if c.fetchall():
                tkinter.messagebox.showinfo(title = "Successfully logged in", message = "Welcome!!! ")
            else:
                tkinter.messagebox.showerror(title = "Error", message = "incorrect username or password")

            c.close()   


        registerframe4 = Frame(self)
        registerframe4.pack(fill=X)

        registerframe5 = Frame(self)
        registerframe5.pack(fill=X)

        label_1 = tk.Label(registerframe4, text="Username")
        label_2 = tk.Label(registerframe5, text="Password")

        label_1.pack(side=LEFT,padx=5,pady=5)
        label_2.pack(side=LEFT,padx=5,pady=5)

        entry_1 = Entry(registerframe4, width=50)
        entry_2 = Entry(registerframe5, width=50, show='*')

        entry_1.pack(side=RIGHT,padx=100)
        entry_2.pack(side=RIGHT,padx=100)

        button1 = tk.Button(self, text="Login",command=LogPress)
        button1.pack(side=TOP)
        button2 = tk.Button(self, text="Don't have an account?", command=lambda: controller.show_frame("Registerform"))
        button2.pack(side=BOTTOM)

        
       
            

    def close_window(self):
        self.master.destroy()


if __name__ == "__main__":


    app = ForFrames()
    app.geometry("700x250")
    app.mainloop()
