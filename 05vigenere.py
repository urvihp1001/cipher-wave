# import tkinter module
from tkinter import *

# import other necessary modules
import random

# creating root object
root = Tk()
root.configure(background = 'darkslategray')
# defining size of window
root.geometry("1200x900")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700,background = 'darkslategray',
							relief = SUNKEN)
f1.pack(side = LEFT)



lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'),
		text = "SECRET MESSAGING \n Vigenère cipher",
					bg = "orangered", bd = 10, anchor='w')
					
lblInfo.grid(row = 0, column = 0)


						
lblInfo.grid(row = 1, column = 0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit function
def qExit():
	root.destroy()

# Function to reset the window
def Reset():
	rand.set("")
	Msg.set("")
	key.set("")
	mode.set("")
	Result.set("")


# reference
# labels
lblMsg = Label(f1, font = ('arial', 16, 'bold'),
		text = "MESSAGE", bd = 16, anchor = "w",background = 'orangered',fg="blue4")
		
lblMsg.grid(row = 1, column = 0)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = Msg, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtMsg.grid(row = 1, column = 1)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "KEY", bd = 16, anchor = "w",background = 'orangered',fg="blue4")
			
lblkey.grid(row = 2, column = 0)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = key, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtkey.grid(row = 2, column = 1)

lblmode = Label(f1, font = ('arial', 16, 'bold'),
		text = "MODE(e for encrypt, d for decrypt)",
								bd = 16, anchor = "w",background = 'orangered',fg="blue4")
								
lblmode.grid(row = 4, column = 0)

txtmode = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = mode, bd = 10, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtmode.grid(row = 4, column = 1)

lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "The Result-", bd = 16, anchor = "w",background = 'orangered',fg="blue4")
			
lblService.grid(row = 2, column = 2)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result, bd = 10, insertwidth = 4,
					bg = "powder blue", justify = 'right')
						
txtService.grid(row = 2, column = 3)



# Function to encode
def encode(key, clear):
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

# Function to decode
def decode(key, enc):
  orig_text = []
  m=len(key)
  for i in range(len(enc)): 
    x = (ord(enc[i]) -ord(key[i%m]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

def Ref():
	print("Message= ", (Msg.get()))

	clear = Msg.get()
	k = key.get()
	m = mode.get()

	if (m == 'e'):
		Result.set(encode(k, clear))
	else:
		Result.set(decode(k, clear))

# Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Show Message", bg = "powder blue",
						command = Ref).grid(row = 7, column = 1)

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Reset", bg = "green",
				command = Reset).grid(row = 7, column = 2)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Exit", bg = "red",
				command = qExit).grid(row = 7, column = 3)
root.mainloop()
