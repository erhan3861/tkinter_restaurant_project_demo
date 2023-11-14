from tkinter import *

para = 100



pencere = Tk()
pencere.geometry("1600x700+0+0")
pencere.resizable(0,0)
pencere.title("Ihsan-Ustanin-Mekani")

Tops = Frame(pencere,bg="white", width = 1600, height = 50, relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(pencere, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(pencere, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)



lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="IHSAN-USTANIN-MEKANI",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=("aria", 20, ), fg="steel blue", anchor="w")
lblinfo.grid(row=1,column=0)

text_Input=StringVar()
operator =""

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set("")



btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=("ariel", 20, "bold",), text="1",bg="powder blue", command=lambda: btnclick(1))


































































"""class Yemek():
    def __init__(self, yemek, table):
        self.yemek = yemek
        self.table = table

    def show_info(self):
        print(self.yemek, self.table)"""




"""class Döner(Yemek):
    def __init__(self, yemek, table, döner):
        super().__init__(yemek, table)
        self.döner = döner
        döner = 10
        Döner.show_info()
        btn = Button(döner, text = "Döner = 10tL")



        
class Pide(Yemek):
    def __init__(self, yemek, table, pide):
        super().__init__(yemek,table)
        self.pide = pide
        pide = 13
        Pide.show_info()
        




class Cola(Yemek):
    def __init__(self, yemek, table, cola):
        super().__init__(yemek, table)
        self.cola = cola
        cola = 2
        Cola.show_info()"""





pencere.mainloop()