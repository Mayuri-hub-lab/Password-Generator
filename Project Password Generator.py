
################################################ PROJECT 2 : PASSWORD GENERATOR ####################################


#import all library

from tkinter import *
import pyperclip
import random
import string
root=Tk()
root.geometry("400*400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
pass_str=stringvar()
pass_len=intvar()
pass_len.set(0)


s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

def generate():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


def copytoclipboard():
    random_password=pass_str.get()
    pyperclip.copy(random_password)

#labels
label(root,text="Enter Password length").pack(paddy=3)
Entry(root,textvariable=pass_len).pack(paddy=3)
Button(root,text="Generate Password" , command=generate).pack()
Entry(root,textvariable=pass_str).pack(paddy=3)
Button(root,text="Copy to Clipboard",command= copytoclipboard).pack()

root.mainloop()
