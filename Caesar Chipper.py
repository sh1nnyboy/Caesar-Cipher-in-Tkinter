from tkinter import*
from tkinter.font import*
from tkinter.messagebox import*
from tkinter import messagebox

class App(Tk):
    def __init__(self):
        self.b = Tk()
        
        self.b.title("Enkripsi Caesar Chipper")
        self.b.configure(background="pink")
        self.helv = Font(family="Helvetica", size=12, weight="bold")
        self.helv2 = Font(family="Helvetica", size=10, weight="bold")
 
        self.b.geometry("350x250")
        self.b.resizable(False,False)

        self.judul= Label(self.b, text="Caesar Chipper Generator", fg="red", font= self.helv )
        self.judul.pack()

        self.inputan = Label(self.b, text="Enkripsi", fg="blue", font= self.helv2)
        self.inputan.place(x=20, y=50)
        self.enkripsix = StringVar()
        self.enkripsi= Entry(self.b, textvariable= self.enkripsix)
        self.enkripsi.place(x=95, y=50)

        self.inputan2 = Label(self.b, text="Loncatan", fg="blue", font = self.helv2)
        self.inputan2.place (x=20, y=80)
        self.loncatanx = IntVar()
        self.loncatan = Spinbox(self.b, from_ =0, to =100, textvariable=self.loncatanx)
        self.loncatan.place(x=95, y=80)

        self.buttontext = StringVar()
        self.button=Button(self.b, textvariable=self.buttontext, command=self.encrypt, width=8)
        self.button.place(x=60, y=120)
        self.buttontext.set("Enkripsi !")

        self.buttontext = StringVar()
        self.button=Button(self.b, textvariable=self.buttontext, command=self.quit, width=8)
        self.button.place(x=145, y=120)
        self.buttontext.set("Exit !")

        self.buttontext = StringVar()
        self.button=Button(self.b, textvariable=self.buttontext, command=self.reset, width=8)
        self.button.place(x=230, y=120)
        self.buttontext.set("Reset !")

        self.labelKet1 = Label(self.b, text ="Hasil Enkripsi : ", fg="red",bg="yellow", font= self.helv2)
        self.labelKet1.place(x=10, y=180)

        self.b.mainloop()

    def quit(self):
        exit()

    def reset(self):
        self.enkripsix.set("")
        self.loncatanx.set("0")
        self.labelKet1.config(text= "Hasil Enkripsi :")

    def encrypt(self):
        result = ""
        for i in range(len(self.enkripsix.get())):
            char=self.enkripsix.get()[i]
            if (char.isupper()):
                result += chr((ord(char) + self.loncatanx.get()-65) % 26 + 65)
            else:
                result += chr((ord(char) + self.loncatanx.get() - 97) % 26 + 97)
        self.labelKet1.config(text= "Hasil Enkripsi : "+ result)
        

        
App()
