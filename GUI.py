from tkinter import * 
import tkinter as tk
from commands import regPress

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

        #self.master = master
        #self.root.title("Register form")

        #self.geometry("250x150")

        #self.bottomFrame = Frame(parent)
        #self.bottomFrame.pack(side=BOTTOM)
        # self.topFrame = Frame(parent)
        #self.topFrame.pack(side=TOP)
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
        entry_2 = Entry(registerframe2, width=50)
        entry_3 = Entry(registerframe3, width=50)

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

        registerframe4 = Frame(self)
        registerframe4.pack(fill=X)

        registerframe5 = Frame(self)
        registerframe5.pack(fill=X)

        label_1 = tk.Label(registerframe4, text="Username")
        label_2 = tk.Label(registerframe5, text="Password")

        label_1.pack(side=LEFT,padx=5,pady=5)
        label_2.pack(side=LEFT,padx=5,pady=5)

        entry_1 = Entry(registerframe4, width=50)
        entry_2 = Entry(registerframe5, width=50)

        entry_1.pack(side=RIGHT,padx=100)
        entry_2.pack(side=RIGHT,padx=100)

    
        


        button1 = Button(self, text="Login")
        button1.pack(side=TOP)
        button2 = Button(self, text="Don't have an account?", command=lambda: controller.show_frame("Registerform"))
        button2.pack(side=BOTTOM)

    def close_window(self):
        self.master.destroy()


if __name__ == "__main__":


    app = ForFrames()
    app.geometry("700x250")
    app.mainloop()
