from tkinter import *
from random import *
from tkinter import messagebox
win = Tk()
win.geometry("600x600")
zone = Canvas(win, width=550, height=550, bg='white')
zone.pack()
Play = True
ready = 0
sea = {}
timer = 0
#---------------------------------------------------------
def on_closing():
    global Play
    if messagebox.askokcancel("Виход з гри", "Хочете вийти з гри?"):
        Play = False
        win.destroy()

win.protocol("WM_DELETE_WINDOW", on_closing)
#-----------------------------------------------------------
#-----------------------------------------------------------
def bigSea():
    global sea
    first_line = randint(0,50)
    point_a = -350+first_line
    point_b = -300+first_line
    line = 0
    first_step = 0
    second_step = 50
    
    for i in range(50):
        wave_line = {}       
        for m in range(50):
            my_circle = "circle" + str(m)
            point_a += 50
            point_b += 50
            wave_line[my_circle] = zone.create_arc(point_a, first_step, point_b, second_step,start=180, extent=180, 
                                                    style=ARC, outline='darkblue', width=1)
        wave = "wave" + str(i)  
        sea [wave] = wave_line 
        line += randint(-10,10)
        first_step += 50
        second_step += 50
        point_a = -50 + line
        point_b = 0 + line  
#---------------------------------------------------------
def move_sea ():
    global sea
    for i in range(50):
        wave = "wave"+str(i)
        step = randint(-100, 100)
        for m in range(50):
            circle = "circle"+str(m)
            zone.move(sea[wave][circle], step,0)
    zone.delete("all")
    bigSea()
#---------------------------------------------------------
while Play == True:    
    if ready < 1 : bigSea(); ready +=1
    win.after(100,move_sea())
    win.update()
    ready = 1
#---------------------------------------------------------
win.mainloop()