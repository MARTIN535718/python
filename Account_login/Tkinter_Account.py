from tkinter import *

def bejelentkezes():
    user = user_bemenet.get()
    passw = password_bemenet.get()
    with open('bankaccount.txt', 'r', encoding='UTF=8') as forras:
        for adat in forras:
            adat = adat.strip()
            adat = adat.split()
            if adat[0] == user:
                if adat[1] == passw:
                    ertesit['state'] = NORMAL
                    ertesit.delete(1.0, END)
                    ertesit.insert(END, 'Sikeres bejelentkezés')
                    ertesit['state'] = DISABLED
                    return
                    
            else:
                ertesit['state'] = NORMAL
                ertesit.delete(1.0, END)
                ertesit.insert(END, 'Helytelen jelszó/user')
                ertesit['state'] = DISABLED
                

def bezar():
    win.destroy()
    reg = Tk()
    reg.title('Regisztrálás')
    reg.geometry('800x500')
    regis_ertesit = Text(reg, width=20, height=1, state=DISABLED, font='Helvetica 10 bold').grid(row=0, column=0)

    Label(reg, text='New Username', font='Helvetica 12 bold').grid(row=1, column=1)

    uj_user_bemenet = Entry(reg, font='Helvetica 12 bold')
    uj_user_bemenet.grid(row=1, column=0)


    Label(reg, text='New Password', font='Helvetica 12 bold').grid(row=2, column=1)

    uj_pass_bemenet = Entry(reg, font='Helvetica 12 bold')
    uj_pass_bemenet.grid(row=2, column=0)

    Button(reg, text="Regisztrálás", command=regiszt, font="Helvetica 12 bold").grid(row=3, column=0)
    
    regiszt()
    
    return
    
    reg.mainloop()

def regiszt():
        
        
    user = uj_user_bemenet.get()
    passw = uj_pass_bemenet.get()
    with open('bankaccount.txt', 'w', encoding='utf=8') as adat:
        print(user, passw, file=adat)
    
    
        

#Ablak létrehoz
win = Tk()
win.title('Bank Account')
win.geometry('800x500')



#Értesírés kiírása
ertesit = Text(win, height=1, width=20, state=DISABLED,font='Helvetica 12 bold')
ertesit.grid(row=0, column=0)



#User rész
Label(win, text='Username', font='Helvetica 18 bold').grid(row=1, column=1)



user_bemenet = Entry(win, font='Helvetica 16 bold')
user_bemenet.grid(row=1, column=0)


#kitolto
Label(win, text='', font='Helvetica 12 bold').grid(row=2, column=0)


#Password rész
Label(win, text='Password', font='Helvetica 18 bold').grid(row=3, column=1)

password_bemenet = Entry(win, font='Helvetica 16 bold')
password_bemenet.grid(row=3, column=0)

Button(win, text="Bejelentkezés", command=bejelentkezes, font="Helvetica 12 bold").grid(row=4, column=0)



#regisztrálás
Button(win, text='Regisztrálás', command=bezar, font='Helvetica 12 bold').grid(row=5, column=0)


win.mainloop()