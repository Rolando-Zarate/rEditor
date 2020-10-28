from tkinter import *
from tkinter import filedialog, messagebox
x = "700"
y = "500"
root = Tk()
root.geometry(x+"x"+y)
root.title("rEditor V1.1")
scrollBar = Scrollbar(root)
scrollBar.pack(side = RIGHT, fill = Y)
box = Text(root,yscrollcommand=scrollBar.set,undo = True, height = y, width = y, font = "Arial, 15", bg = "#003582", fg = "#ffffff", insertbackground = "#ffffff")
box.pack()
scrollBar.config(command = box.yview)
currentFile = False
def aboutShow():
    messagebox.showinfo(title="About rEditor", message = "rEditor is a free text editor coded by Rolando Zarate, Version 1.1")
def openFile():
    global currentFile
    openWindow = filedialog.askopenfilename(title="Open a file",initialdir="/", filetypes=(("Text files","*.txt"),("All files","*.*")))
    openFile = open(openWindow, "r")
    readedOpenFile = openFile.read()
    box.delete("1.0", "end")
    box.insert("1.0", readedOpenFile)
    currentFile = openWindow
    openFile.close()
def saveAs():
    global currentFile
    saveAsWindow = filedialog.asksaveasfilename(title = "Save as",initialdir="/", filetypes = (("All Files","*.*"),))
    saveFile = open(saveAsWindow, "w")
    textToSaveAs = box.get("1.0", END)
    saveFile.truncate()
    saveFile.write(textToSaveAs)
    currentFile = saveAsWindow
    saveFile.close()
def newFile():
    global currentFile
    box.delete("1.0", "end")
    currentFile = False
def save():
    global currentFile
    if currentFile == False:
        messagebox.showinfo(title="Not selected file!", message="You have to open a file!")
    else:
         toSave = open(currentFile, "w")
         toSaveText = box.get("1.0", END)
         toSave.truncate()
         toSave.write(toSaveText)
         toSave.close()
menubar = Menu(root)
files = Menu(menubar, tearoff = False)
about = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Files", menu = files)
menubar.add_cascade(label = "About rEditor", menu = about)
files.add_command(label = "New File", command = newFile)
files.add_command(label = "Open file", command = openFile)
files.add_command(label = "Save as", command = saveAs)
files.add_command(label = "Save", command = save)
about.add_command(label = "About", command = aboutShow)
root.config(menu=menubar)
root.mainloop()
