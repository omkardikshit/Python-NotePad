from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import sys

master = Tk()
master.title("Notepad")
master.geometry("600x500")

text = Text(master, width = 300,height=300,font=("Consolas Bold",20),highlightthickness=0)
text.pack()

menu = Menu(master)
menu2 = Menu(master)
master.config(menu = menu)

def Exit():
   answer = tkinter.messagebox.askquestion("Notepad","Do you Want to Save Changes")
   if answer == 'yes' :
      Save()
   else :
      master.quit()

def Open():
   master.fileName = filedialog.askopenfilename(filetypes = (("Text Documents",".txt"),("All Files","*.*")))
   master.fileName = open(master.fileName)
   txt = master.fileName.read()
   text.insert(END,txt)
   New()

def New():
   ans = messagebox.askquestion(title="Save File", message="Would You Like To Save?")
   if ans is True:
      Save()
      Delete_all()
   else :
      Delete_all()

def Delete_all():
   text.delete(1.0,END)
   
def Save():
   path =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text Documents",".txt"),("All Files","*.*")))
   write = open(path,mode='w')
   write.write(text.get("1.0",END))

def Close():
   Save()
   master.quit()

def Cut():
   master.clipboard_clear()
   text.clipboard_append(string=text.selection_get())
   text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def Copy():
   master.clipboard_clear()
   text.clipboard_append(string=text.selection_get())   

def Paste():
   text.insert(INSERT, master.clipboard_get())

def Delete():
   text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def Select_All():
   text.tag_add(SEL,"1.0",END)
   
subMenu = Menu(menu)
menu.add_cascade(label="File", menu = subMenu)
subMenu.add_command(label="New      Ctrl+N",command=New)
subMenu.add_command(label="Open...      " ,command=Open)
subMenu.add_command(label="Save      Ctrl+S" ,command=Save)
subMenu.add_command(label="Save As...")
subMenu.add_separator()
subMenu.add_command(label="Page Setup...")
subMenu.add_command(label="Print      Ctrl+P")
subMenu.add_separator()
subMenu.add_command(label="Exit" ,command=Exit)

subMenu2 = Menu(menu2)
menu.add_cascade(label="Edit", menu = subMenu2)
subMenu2.add_command(label="Undo      Ctrl+Z")
subMenu2.add_command(label="Redo       Ctrl+Shift+Z")
subMenu2.add_separator()
subMenu2.add_command(label="Cut          Ctrl+X", command=Cut)
subMenu2.add_command(label="Copy       Ctrl+C", command=Copy)
subMenu2.add_command(label="Paste       Ctrl+V", command=Paste)
subMenu2.add_command(label="Delete         Del", command=Delete)
subMenu2.add_command(label="Select All ", command=Select_All)

master.mainloop()

