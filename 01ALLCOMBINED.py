import winsound
from tkinter import *
# import messagebox class from tkinter
from tkinter import messagebox
from tkinter import ttk # additionally imports Tkinter subpackage for progress bar.
import time
import base64
# Create a GUI window
root = Tk()
# create a global variables
variable1 = StringVar(root)
variable2 = StringVar(root)        
# initialise the variables
variable1.set("lang-code")
variable2.set("lang-code")
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..', 'a':'.-', 'b':'-...',
'c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-','l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-',
'r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--','x':'-..-', 'y':'-.--', 'z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
# Function to clear both text areas
def clearAll() :
	# whole content of text area is deleted
	language1_field.delete(1.0, END)
	language2_field.delete(1.0, END)
# Function to perform conversion from one language to another
def convert() :
	# get a whole input content from text box ignoring \n from the text box content
	message = language1_field.get("1.0", "end")[:-1]
	# get the content from variable1 and 2, check their values
	 #variable1.get() == variable2.get() :
	if variable1.get()==variable2.get():
		# show the error message
		messagebox.showerror("Can't Be same Language")
		return
	if variable1.get() == "Eng" and variable2.get() == "Morse" :
		# function call
		rslt = encrypt(message)
	elif variable1.get() == "Morse" and variable2.get() == "Eng" :
		# function call
		rslt = decrypt(message)
	else :
		#show the error message
		messagebox.showerror("please choose valid language code..")
		return
	# insert content into text area
	# from rslt variable
	language2_field.insert('end -1 chars', rslt)
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	global cipher
	cipher=''
	for letter in message:
		if letter != ' ':
			# Looks up the dictionary and adds the corresponding morse code along with a space to separate morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters and 2 indicates different words
			cipher += ' '
	return cipher
# Function to decrypt the string from morse to english
def decrypt(message):
	# extra space added at the end to access the last morse code
	message += ' '
	decipher,citext='',''
	for letter in message:
		# checks for space
		if (letter != ' '):
			# counter to keep track of space
			i = 0
			# storing morse code of a single character
			citext += letter
		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1
			# if i = 2 that indicates a new word
			if i == 2 :
				# adding space to separate words
				decipher += ' '
			else:
				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT .values()).index(citext)]
				citext = ''
	return decipher
def sound(message):  #declares a function that takes string as parameter
    length = len(message) # stores length of a Morse translated Message.
    my_progress['value'] = 0 # Updates progress bar with 0 value in order to clear it once user decides to play the sound 
    for i in message: # for loop that iterates through Message in order to play a sound
        if i == '.': # if symbol is "."
            my_progress['value'] += 100 / length # Updates progress bar for "100 / length of a message"
            root.update_idletasks() # pushes program to draw progress bar update for every for loop iteration
            winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1) # timeout for listener
        elif i == '-': # else if symbol is "-"
            my_progress['value'] += 100 / length # Updates progress bar for "100 / length of a message"
            root.update_idletasks()
            winsound.Beep(1000, 600)  # Beep at 1000 Hz for 600 ms
            time.sleep(0.1)
        elif i == ' ': # else if symbol is " "
            my_progress['value'] += 100 / length
            root.update_idletasks()
            pass # do nothing continue loop, there is no sound for space symbol
def play_coded_message():
    sound(cipher)
    root.update_idletasks()   
# Driver code
if __name__ == "__main__" :
	# Set the background colour of GUI window
	root.configure(background = 'darkslategray')
	# Set the configuration of GUI window (WidthxHeight)
	root.geometry("720x720")
	# set the name of tkinter GUI window
	root.title("Translator")
	# Create Welcome to Morse Code Translator label
	headlabel = Label(root, text = 'Welcome to Morse Code Translator',fg = 'blue4', bg = "orangered", font=('Times', 27))
	# Create a "One Language " label
	label1 = Label(root, text = "One Language ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	# Create a "From Language " label
	label2 = Label(root, text = "From Language",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	# Create a "To Language " label
	label3 = Label(root, text = "To Language ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	# Create a "Converted Language " label
	label4 = Label(root, text = "Converted Language ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	# grid method is used for placing the widgets at respective positions in table like structure .
	headlabel.grid(row = 0, column = 1)
	label1.grid(row = 1, column = 0)
	label2.grid(row = 2, column = 0)
	label3.grid(row = 3, column = 0)
	label4.grid(row = 5, column = 0)
	# Create a text area box for filling or typing the information.
	language1_field = Text(root, height = 5, width = 25,font = "arial 15")
	language2_field = Text(root, height = 5, width = 25,font = "arial 15")
	# padx keyword argument used to set padding along x-axis .
	language1_field.grid(row = 1, column = 1, padx = 10)
	language2_field.grid(row = 5, column = 1, padx = 10)
	# list of language codes
	languageCode_list = ["Eng", "Morse"]
	# create a drop down menu using OptionMenu function which takes window name, variable and choices as an argument. use * before the name of the list, to unpack the values
	FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
	ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)
	FromLanguage_option.grid(row = 2, column = 1, padx = 10)
	ToLanguage_option.grid(row = 3, column = 1, padx = 10)
	# Create a Convert Button and attached
	# with convert function
	button1 = Button(root, text = "Convert", bg = "red", fg = "black",command = convert)
	button1.grid(row = 6, column = 1)
	# Create a Clear Button and attached with clearAll function
	button2 = Button(root, text = "Clear", bg = "red",fg = "black", command = clearAll)
	button2.grid(row = 9, column = 1)
	my_progress = ttk.Progressbar(root, orient=HORIZONTAL,length=300, mode="determinate")
	my_progress.grid(row=20,column=1)#creates progress bar
	playsound = Button(root, text="Play it", command=play_coded_message).grid(row=8,column=1) # creates a button, place it on main window, with a text "Play it", once clicked - it runs play_coded_message function.
	# Start the GUI
	root.mainloop()
r = Tk()
def clearAll() :
	# whole content of text area is deleted
	pt_field.delete(1.0, END)
	k.delete(1.0, END)
	ct_field.delete(1.0, END)
def encrypt(message,k):
        global result
        result=''
        for i in message:
            char = i
            # Encrypt uppercase characters
            if (char.isupper()):
                    result += chr((ord(char) + int(k)-65) % 26 + 65)
            # Encrypt lowercase characters
            elif (char.islower()):
                    result += chr((ord(char) + int(k) - 97) % 26 + 97)
            else:
                    result+=char
        return result
def convert():
    message=pt_field.get("1.0", "end")[:-1]
    key=k.get("1.0", "end")[:-1]
    result=encrypt(message,key)
    ct_field.insert('end -1 chars', result)
if __name__ == "__main__" :
	r.configure(background = 'darkslategray')
	r.geometry("720x720")
	r.title("Converter")
	headlabel = Label(r, text = 'Welcome to Caesar Cipher',fg = 'blue4', bg = "orangered",font=('Times', 27))
	headlabel.grid(row = 11, column = 1)
	label1 = Label(r, text = "PlainText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label2 = Label(r, text = "Key",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label3 = Label(r, text = "CipherText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label1.grid(row = 12, column = 0)
	label2.grid(row = 14, column = 0)
	label3.grid(row = 16, column = 0)
	pt_field = Text(r, height = 5, width = 25,font = "arial 15")
	k = Text(r, height = 2, width = 25,font = "arial 9")
	ct_field = Text(r, height = 5, width = 25,font = "arial 15")
	pt_field.grid(row = 12, column = 1, padx = 10)
	k.grid(row=14,column=1,padx=15)
	ct_field.grid(row = 16, column = 1, padx = 10)
	button1 = Button(r, text = "Convert", bg = "red", fg = "black",command = convert)
	button1.grid(row = 15, column = 1)
	button2 = Button(r, text = "Clear", bg = "red",fg = "black", command = clearAll)
	button2.grid(row = 18, column = 1)	
r.mainloop()
#OTP
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



lblInfo = Label(Tops, font = ('arial', 50, 'bold'),
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
	label2 = Label(r, text = "Key",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label3 = Label(r, text = "CipherText ",fg = 'blue4', bg = 'orangered',font=('Times', 15))
	label1.grid(row = 12, column = 0)
	label2.grid(row = 14, column = 0)
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
