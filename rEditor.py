from tkinter import *
from tkinter import filedialog, messagebox
print("Now running rEditor v1.0, Coded by rolando zarate")
print("This is a beta")
root = Tk()
root.title("rEditor")
root.resizable(False, False)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
box = Text(root,yscrollcommand = scrollbar.set,undo = True, font="Calibri, 15", bg = "#101781", fg="white", insertbackground="#61A2FF",
     selectbackground="blue")
box.pack()
scrollbar.config(command = box.yview)
current = False
def aboutreditor():
    win = messagebox.showinfo(title="About rEditor...", message="rEditor is a free text editor, coded by rolando zarate, Version 1.0")
def openfile():
    global current
    filewin = filedialog.askopenfilename(initialdir="/", title="Open file", filetypes=(("Text Files","*.txt"),("All files","*.*"),("HTML files", "*.html")))
    box.delete("1.0", "end")
    textopen = open(filewin,"r")
    box.insert("1.0", textopen.read())
    current = filewin
    textopen.close()
def savefileas():
    filesave = filedialog.asksaveasfilename(title="Save as", filetypes=(("Text files", "*.txt"),("All files", "*.*"),("HTML files","*.html")))
    textnamesaveas = open(filesave, "w")
    texttosaveas = box.get("1.0", END)
    textnamesaveas.write(texttosaveas)
    textnamesaveas.close()
def newfile():
    global current
    box.delete("1.0", "end")
    current = False
def savefile():
    global current
    if current == False:
        messagebox.showinfo(title="Not selected file!", message="You have to open a file!")
    else:
         textnamesave = open(current, "w")
         texttosave = box.get("1.0", END)
         textnamesave.write(texttosave)
         textnamesave.close()


def gui():
    menubar = Menu(root)
    files = Menu(menubar, tearoff=False)
    about = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Files", menu = files)
    menubar.add_cascade(label="About rEditor...",menu=about )
    files.add_command(label="New File...", command=newfile)
    files.add_command(label="Open File...", command=openfile)
    files.add_command(label="Save as...", command=savefileas)
    files.add_command(label="Save file...", command=savefile)
    about.add_command(label="About", command=lambda:aboutreditor())
    root.configure(menu=menubar)
gui()
root.mainloop()
