from tkinter.ttk import *
from tkinter import *
import winsound
minu = 25
pontos = 0


# menu de estudo
def start() :
    menu5 = Tk()
    menu5.geometry('300x300')
    menu5.config(bg=('#A2EC3B'))
    texto = StringVar(menu5, (f'Tempo para estudar ({minu} min)') )    
    
    men5lab = Label(menu5, textvariable=texto, 
                    font=('Arial',12),
                    relief=SUNKEN)
    men5lab.pack()

    barra = Progressbar(menu5, orient=HORIZONTAL, length=250,)
    barra.pack()

    # menu de espera
    def salaesp() :
        sala = Tk()
        sala.geometry('300x300')
        sala.config(bg=('#A2EC3B'))

        global pontos
        global minu

        if pontos == 4:
            minu = 30
            pontos = 0

        else:
            minu = 5

        texto = StringVar(sala, (f'Tempo para descansar ({minu} min)') )
        men5lab = Label(sala, textvariable=texto, 
                        font=('Arial',12),
                        relief=SUNKEN)
        men5lab.pack()
        barra = Progressbar(sala, 
                            orient=HORIZONTAL, 
                            length=250,)
        barra.pack()

        def tempo() :
            xb=0
            valor = (100/minu)
            while (xb <= minu) :
                barra['value'] += valor
                xb += 1
                men5lab.update_idletasks()
                sala.after(100)
            #winsound.PlaySound('alarm-clock-01.wav', winsound.SND_FILENAME)
            men5butao.destroy()
            salabutcont.pack(side=LEFT)
            salabutpara.pack(side=RIGHT)
        
        def continuar() :
            sala.destroy()
            menu5.deiconify()            
        def parar() :
            sala.destroy()
            menuprin.destroy()
            menu5.destroy()
        men5butao = Button(sala, text='iniciar!',
                    command=tempo,
                    font=('Arial',20),
                    bg=('#856ff8'),)
        men5butao.pack()

        salabutcont = Button(sala, text='Continuar!',
            command=continuar,
            font=('Arial',20),
            bg=('#856ff8'),)
        
        salabutpara = Button(sala, text='Parar!',
            command=parar,
            font=('Arial',20),
            bg=('#856ff8'),)
        
        ########################

    def tempo() :
        men5butao['state'] = 'disabled'
        global pontos 
        global minu
        xb=0
        valor = (100/minu)
        while (xb <= minu) :
            barra['value'] += valor
            xb += 1
            men5lab.update_idletasks()
            menu5.after(200)
        men5butao['state'] = 'active'
        barra['value'] = 0 
        pontos += 1
        #winsound.PlaySound('alarm-clock-01.wav', winsound.SND_FILENAME)
        menu5.withdraw()
        salaesp()



    men5butao = Button(menu5, text='iniciar!',
                command=tempo,
                font=('Arial',20),
                bg=('#856ff8'),)
    men5butao.pack()



    menu5.mainloop()

# css que n é css mas parece
menuprin = Tk()
jon = PhotoImage(file='joji.png')
menuprin.geometry('300x400')
menuprin.title('Pomodoro By John')
menuprin.minsize(300, 400)
menuprin.maxsize(300, 400)
menuprin.config(bg=('#A2EC3B'))

prinlab1 = Label(
    text='=== Bem vindo ===',
    font=('Arial',20),
    padx= 50,
    pady=10,
    bg=('#A2EC3B'),
    )
prinlab1.pack()

prinlab2 = Label(text='Programa para metodo pomodoro!',
    font=('Arial',12),
    bg=('black'),
    padx= 10,
    pady=10,
    relief=SUNKEN,
    image=jon,
    compound='bottom')
prinlab2.pack()



iniciar = Button(text='iniciar!',
                command=start,
                font=('Arial',20),
                bg=('#856ff8'),
                )
iniciar.pack(side= BOTTOM)

menuprin.mainloop()
