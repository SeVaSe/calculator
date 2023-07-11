from tkinter import *
from mass_calc import open_weight_window
# from prog_calc import open_programming_window

window = Tk()
window.title('Calculator')
window.geometry('340x500')

# функция меню, для перехода в калькуляторы: массы и программиста
def menu_main():
    main_menu = Menu()
    main_menu.add_cascade(label="Вес", command=open_weight_window)
    main_menu.add_cascade(label="Программист" '''command=open_programming_window''')
    window.config(menu=main_menu)


# функция расстановки кнопок
def knopki():
    # строка ввода
    entry = Entry(window, width=19, font=('', 20))
    entry.place(x=25, y=30)

    ### первая строчка кнопок
    # 1
    btn1 = Button(window, bg='black', fg='white', text='1', font=('', 15))
    btn1.place(x=25, y=70, width=70, height=70)

    # 2
    btn2 = Button(window, bg='black', fg='white', text='2', font=('', 15))
    btn2.place(x=98, y=70, width=70, height=70)

    # 3
    btn3 = Button(window, bg='black', fg='white', text='3', font=('', 15))
    btn3.place(x=170, y=70, width=70, height=70)

    # +
    btn4 = Button(window, bg='black', fg='white', text='+', font=('', 15))
    btn4.place(x=242, y=70, width=70, height=70)


    ### вторая строчка кнопок
    # 4
    btn1 = Button(window, bg='black', fg='white', text='4', font=('', 15))
    btn1.place(x=25, y=142, width=70, height=70)

    # 5
    btn2 = Button(window, bg='black', fg='white', text='5', font=('', 15))
    btn2.place(x=98, y=142, width=70, height=70)

    # 6
    btn3 = Button(window, bg='black', fg='white', text='6', font=('', 15))
    btn3.place(x=170, y=142, width=70, height=70)

    # -
    btn4 = Button(window, bg='black', fg='white', text='-', font=('', 15))
    btn4.place(x=242, y=142, width=70, height=70)

knopki()
menu_main()
window.mainloop()












