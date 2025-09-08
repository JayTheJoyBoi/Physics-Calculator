import tkinter as tk
from random import randint
from time import sleep
import threading
def main(physicsUserFunctions):
    class Application(tk.Frame):
        tk = tk
        screenItems = {}
        lineCount = 0
        def print(self,*args,sep=" ",newline=True):
            string = sep.join(args)
            n = 'print'+str(randint(1,99999999999))
            self.screenItems[n] = tk.Label(self,text=string)
            self.screenItems[n].grid(column=0,row=self.lineCount)
            if newline:
                self.lineCount += 1
        async def input(self,text):
            self.isenter = False
            self.print(text,newline=False)
            na = 'inBox'+str(randint(1,99999999999))
            self.screenItems[na] = tk.Entry(self)
            self.screenItems[na].grid(column=1,row=self.lineCount)
            n = 'inBoxRet'+str(randint(1,99999999999))
            self.screenItems[n] = tk.Button(self,text="Enter",command=self.__setIsEnterForInput)
            self.screenItems[n].grid(column=2,row=self.lineCount)
            sleep(1)
            while not self.isenter:
                pass
            self.lineCount += 1
            return self.screenItems[na].get()
        def __setIsEnterForInput(self):
            self.isenter=True
        def cls(self):
            for widget in self.winfo_children():
                widget.destroy()
            self.screenItems = {}
            self.lineCount = 0
        def __init__(self,master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.menu()
        def menu(self):
            self.pageTitle = tk.Label(self,text="Physics Calculator")
            self.pageTitle.grid(row=0,column=0)
            self.lineCount = 1
            for i in physicsUserFunctions.keys():
                n = 'menu'+str(randint(1,99999999999))
                self.screenItems[n] = tk.Button(self,text=i,command=lambda: self.__getargs(i))
                self.screenItems[n].grid(column=0,row=self.lineCount)
                self.lineCount += 1
        def __getargs(self,i):
            argBoxes = {}
            self.cls()
            self.print(i)
            for n,t in physicsUserFunctions[i]['args'].items():
                self.print(n,newline=False)
                if t == 'entry':
                    argBoxes[n] = tk.Entry(self)
                elif t == 'text':
                    argBoxes[n] = tk.Text(self)
                argBoxes[n].grid(column=0,row=self.lineCount)  
                self.lineCount += 1
            self.screenItems["EntrreySubmitBtn"] = tk.Button(self,text="Submit",command=lambda: threading.Thread(target=self.__handleArgs,args=(i,argBoxes,)).start())
            self.screenItems["EntrreySubmitBtn"].grid(column=0,row=self.lineCount)
            self.lineCount += 1
        async def __handleArgs(self,i,argBoxes):
            args = {}
            for n in physicsUserFunctions[i]['args'].keys():
                args[n] = argBoxes[n].get()
            self.cls()
            await physicsUserFunctions[i]['funct'](self,args)
    root = tk.Tk()
    root.title("Physics Calculator")
    app = Application(master=root)
    app.mainloop()