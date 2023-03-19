#OTP
from tkinter import *
r = Tk()
def clearAll() :
	# whole content of text area is deleted
	pt_field.delete(1.0, END)
	k.delete(1.0, END)
	ct_field.delete(1.0, END)
def enc(clear,key):
    clear = clear.lower()
    clear = clear.replace(' ','')
    m = len(key)
    key = [ord(letter)-97 for letter in key]
    cipher_text = ''
    for i in range(len(clear)):
        letter = clear[i]
        k= key[i % m] 
        cipher_text += chr((ord(letter) + int(k) - 97) % 26 + 97)
    return cipher_text
def convert():
    message=pt_field.get("1.0", "end")[:-1]
    key=k.get("1.0", "end")[:-1]
    if len(key)!=len(message):
        messagebox.showerror("message length must match key length!!!")
        return 
    result=enc(message,key)
    ct_field.insert('end -1 chars', result)
if __name__ == "__main__" :
	r.configure(background = 'darkslategray')
	r.geometry("720x720")
	r.title("Converter")
	headlabel = Label(r, text = 'Welcome to OTP Cipher',fg = 'blue4', bg = "orangered",font=('Times', 27))
	headlabel.grid(row = 11, column = 1)
	label1 = Label(r, text = "PlainText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label2 = Label(r, text = "Key",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label3 = Label(r, text = "CipherText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label1.grid(row = 12, column = 0)
	label2.grid(row = 14, column = 0)
	label3.grid(row = 16, column = 0)
	pt_field = Text(r, height = 5, width = 25,font = "arial 15")
	k = Text(r, height = 5, width = 25,font = "arial 9")
	ct_field = Text(r, height = 5, width = 25,font = "arial 15")
	pt_field.grid(row = 12, column = 1, padx = 10)
	k.grid(row=14,column=1,padx=15)
	ct_field.grid(row = 16, column = 1, padx = 10)
	button1 = Button(r, text = "Convert", bg = "red", fg = "black",command = convert)
	button1.grid(row = 15, column = 1)
	button2 = Button(r, text = "Clear", bg = "red",fg = "black", command = clearAll)
	button2.grid(row = 18, column = 1)	
r.mainloop()

