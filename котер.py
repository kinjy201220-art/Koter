
import tkinter as tk
from tkinter import ttk

timer_runing = True




# noinspection PyTypeChecker
def glader():
    textcat.config(text='Мур-Мур')
    vlad()
    root.after(5000, text)


# noinspection PyTypeChecker
def fooderr():
    textcat.config(text='Мяу-мяу-мяу')
    root.after(5000, text)
    havich()



root = tk.Tk()
root.geometry('500x600')
root.title('*** котер ***')
root.resizable(False, False)
shalle_var = tk.IntVar(value=200)
vish = tk.IntVar(value=200)

shalle_var.set(200)
vish.set(200)
tylse = ttk.Style()
tylse.theme_use('clam')
tylse.configure("TLabel", background='brown', troughcolor='white')


textcat = tk.Label(root, text="...")
textcat.pack(pady=25, fill="none")

glade = tk.Button(root, text="🐾 гладить 🐾", command=glader, width=20, height=5)
glade.pack(side='bottom', ipadx=0)

buttontr = 50

imgr = tk.PhotoImage(file='bbt.png')
img_cat = tk.Label(root, image=imgr)
img_cat.pack(pady=buttontr, fill="none")

fooder = tk.Button(root, text="🍖 кормить 🍖", command=fooderr, width=20, height=5)
fooder.pack(side='bottom', ipadx=20)
eat = 0


# noinspection PyTypeChecker
def ing():
    global eat
    eat = (eat + 1)
    root.after(5000, ing)


# noinspection PyTypeChecker
def decrise_hugr():
    global timer_runing
    if not timer_runing:
        return


    current = shalle_var.get()
    if current > 0:
        shalle_var.set(current -5)

    else:
        textcat.config(text='Я голоден, мяу-мяу')
        gold_eat()
    root.after(3000, decrise_hugr)

def text():
    textcat.config(text='...')



# noinspection PyTypeChecker
def havich():
    current = shalle_var.get()
    if current < 200:
        shalle_var.set(current + 10)
    else:
        shalle_var.set(current + 0)


# noinspection PyTypeChecker
def nastr():

    current = vish.get()
    if current > 0:
        vish.set(current -1)
        root.after(2000, nastr)

    else:
        textcat.confing(text='Мне грусно, мяу-мяу')

def vlad():
    current = vish.get()

    if current < 200:
        vish.set(current + 10)
    else:
        vish.set(current + 0)

def gold_eat():
    current = shalle_var.get()
    secter = vish.get()

    if current == 0:
        vish.set(secter -50)


# noinspection PyTypeChecker
def timers():
    root.after(15000, oth)

def oth():
    textcat.config(text=eat)


# noinspection PyTypeChecker
def sleep():
    textcat.config(text='я пожалуй действительно посплю...')
    root.after(5000, text)



shak = ttk.Progressbar(root, orient='vertical', length=200, mode='determinate', variable=shalle_var, maximum=200)
shak.place(x=470, y=200)

nast = ttk.Progressbar(root, orient='vertical', length=200, mode='determinate', variable=vish, maximum=200)
nast.place(x=20, y=200)

yug = tk.Label(root, text="0")
yug.place(x=4, y=10)

def jf():
    sleep()
    adm_command1()

sleepr = tk.Button(root, text='спать', command=jf)
sleepr.place(x=450, y=550)


# noinspection PyTypeChecker
def polych():
    inver = prim.get()
    textcat.config(text=f'мяу-{inver}-мяу')
    root.after(5000, text)

prim = tk.Entry(root, width=20)
prim.place(x=10, y=500)



prime = tk.Button(root, text='скажи', command=polych)
prime.place(x=25, y=520)
give100 = 'give100'

def adm_command1():
    inver = prim.get()
    if inver == give100:
        current = shalle_var.get()
        sector = vish.get()
        shalle_var.set(current + 100)
        vish.set(sector + 100)


ing()
nastr()
decrise_hugr()

root.mainloop()

