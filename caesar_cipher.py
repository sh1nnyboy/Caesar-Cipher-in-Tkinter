from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import showerror
from tkinter import messagebox

class CaesarCipherApp(Tk):
    def __init__(self):
        self.root = Tk()
        
        self.root.title("Caesar Cipher Encryption")
        self.root.configure(background="pink")
        self.title_font = Font(family="Helvetica", size=12, weight="bold")
        self.label_font = Font(family="Helvetica", size=10, weight="bold")
 
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        self.title_label = Label(self.root, text="Caesar Cipher Generator", fg="red", font=self.title_font)
        self.title_label.pack()

        self.input_label = Label(self.root, text="Plain Text", fg="blue", font=self.label_font)
        self.input_label.place(x=20, y=50)
        self.text_var = StringVar()
        self.text_entry = Entry(self.root, textvariable=self.text_var)
        self.text_entry.place(x=95, y=50)

        self.shift_label = Label(self.root, text="Shift Value", fg="blue", font=self.label_font)
        self.shift_label.place(x=20, y=80)
        self.shift_var = IntVar()
        self.shift_entry = Spinbox(self.root, from_=0, to=25, textvariable=self.shift_var)
        self.shift_entry.place(x=95, y=80)

        self.encrypt_button = Button(self.root, text="Encrypt!", command=self.encrypt, width=8)
        self.encrypt_button.place(x=60, y=120)

        self.exit_button = Button(self.root, text="Exit", command=self.quit, width=8)
        self.exit_button.place(x=145, y=120)

        self.reset_button = Button(self.root, text="Reset", command=self.reset, width=8)
        self.reset_button.place(x=230, y=120)

        self.result_label = Label(self.root, text="Encryption Result: ", fg="red", bg="yellow", font=self.label_font)
        self.result_label.place(x=10, y=180)

        self.root.mainloop()

    def quit(self):
        exit()

    def reset(self):
        self.text_var.set("")
        self.shift_var.set(0)
        self.result_label.config(text="Encryption Result: ")

    def encrypt(self):
        input_text = self.text_var.get()
        shift_value = self.shift_var.get()
        
        if input_text == "":
            showerror("Error", "Please enter a text to encrypt!")
            return
        elif shift_value == 0:
            showerror("Error", "Please enter a shift value greater than 0!")
            return
            
        result = ""
        for char in input_text:
            if char.isupper():
                result += chr((ord(char) + shift_value - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift_value - 97) % 26 + 97)
            else:
                # Preserve spaces and special characters
                result += char
                
        self.result_label.config(text="Encryption Result: " + result)
        
if __name__ == "__main__":
    CaesarCipherApp()
