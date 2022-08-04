from tkinter import *
import random, time
import pygame
pygame.init()

def brosok():
    x = random.choice(['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'])
    return x

def img():
    global b1, b2, s
    for i in range(13):
        b1 = PhotoImage(file=(brosok()))
        b2 = PhotoImage(file=(brosok()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.11)
        s = pygame.mixer.Sound("14.wav")
        s.play()

#Создание окна приложения:
root = Tk ()
root.geometry('1228x478')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height = False, width = False)
#Создание иконки в заголовке окна:
root.iconphoto(True, PhotoImage(file=('icon.png')))
#Создание кнопок:
but1 = Button(root, text = 'Бросает кости 1-ый игрок', width=21, height=1, font='Times 10', command=img).pack()
but2 = Button(root,text='Бросает кости 2-ой игрок', width=21, height=1, font='Times 10', command=img ).pack()
#Создание фона:
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()  
#Создание меток для отображения изображений "костей"      
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.57, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.57, anchor=CENTER)
b1 = PhotoImage(file=(brosok()))
b2 = PhotoImage(file=(brosok()))
lab1['image'] = b1
lab2['image'] = b2
#Добавление фоновой музыки:
pygame.mixer.music.load('12.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(1)

root.mainloop()
