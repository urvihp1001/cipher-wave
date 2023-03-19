import winsound
from tkinter import *
# import messagebox class from tkinter
from tkinter import messagebox
from tkinter import ttk # additionally imports Tkinter subpackage for progress bar.
import time 
import base64
r = Tk()
def clearAll() :
	# whole content of text area is deleted
	pt_field.delete(1.0, END)
	ct_field.delete(1.0, END)
def encode(message):
        sample_string = message
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string
def convert():
    message=pt_field.get("1.0", "end")[:-1]
    
    result=encode(message)
    ct_field.insert('end -1 chars', result)
if __name__ == "__main__" :
	r.configure(background = 'darkslategray')
	r.geometry("720x720")
	r.title("Converter")
	headlabel = Label(r, text = 'Welcome to Base64',fg = 'blue4', bg = "orangered",font=('Times', 27))
	headlabel.grid(row = 11, column = 1)
	label1 = Label(r, text = "PlainText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	
	label3 = Label(r, text = "CipherText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label1.grid(row = 12, column = 0)
	
	label3.grid(row = 16, column = 0)
	pt_field = Text(r, height = 5, width = 25,font = "arial 15")
	
	ct_field = Text(r, height = 5, width = 25,font = "arial 15")
	pt_field.grid(row = 12, column = 1, padx = 10)
	
	ct_field.grid(row = 16, column = 1, padx = 10)
	button1 = Button(r, text = "Convert", bg = "red", fg = "black",command = convert)
	button1.grid(row = 15, column = 1)
	button2 = Button(r, text = "Clear", bg = "red",fg = "black", command = clearAll)
	button2.grid(row = 18, column = 1)	
r.mainloop()
