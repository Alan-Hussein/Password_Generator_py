#importing Libraries

from tkinter import *
import random, string
import pyperclip



###initialize window

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root,  font ='arial 15 bold').pack(side = BOTTOM)



###select password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()



#####define function

pass_str = StringVar()

def Generator():
    password = ''
    for x in range(pass_len.get()):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   


###button

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 10)

Entry(root , textvariable = pass_str).pack()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

    '''
pyperclip is a Python module that provides a cross-platform clipboard interface.
It allows you to easily copy and paste text to and from the clipboard in your Python programs,
    '''

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=15)




# loop to run program
root.mainloop()
