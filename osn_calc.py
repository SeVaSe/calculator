from tkinter import *
from mass_calc import open_weight_window
from prog_calc import open_programming_window

window = Tk()
window.title('Calculator')
window.geometry('340x500')

# функция меню, для перехода в калькуляторы: массы и программиста
def menu_main():
    main_menu = Menu()
    main_menu.add_cascade(label="Вес", command=open_weight_window)
    main_menu.add_cascade(label="Программист", command=open_programming_window)
    window.config(menu=main_menu)


# наш textBox
def input_entry(znak, entry):
    entry.insert(END, znak)

# очистка textBox
def clear_entry(entry):
    entry.delete(0, END)

# удалить 1 знак
def delete_znak(entry):
    current_text = entry.get()

    if current_text:
        new_text = current_text[:-1]
        entry.delete(0, END)
        entry.insert(0, new_text)

def answer_send(strok_entry):
    strok = strok_entry.get()
    print(eval(strok))





# функция расстановки кнопок
def knopki():
    # строка ввода
    entry = Entry(window, width=19, font=('', 20))
    entry.place(x=25, y=30)


    ### первая строчка кнопок
    # возвести в степень
    btn1 = Button(window, bg='black', fg='white', text='x^?', font=('', 15), command= lambda : input_entry('в разработке', entry))
    btn1.place(x=25, y=70, width=70, height=70)

    # стереть все
    btn2 = Button(window, bg='black', fg='white', text='C', font=('', 15), command= lambda : clear_entry(entry))
    btn2.place(x=98, y=70, width=70, height=70)

    # удалить один последний символ
    btn3 = Button(window, bg='black', fg='white', text='del', font=('', 15), command= lambda : delete_znak(entry))
    btn3.place(x=170, y=70, width=70, height=70)

    # +
    btn_plus = Button(window, bg='black', fg='white', text='+', font=('', 20), command= lambda : input_entry('+', entry))
    btn_plus.place(x=242, y=70, width=70, height=70)


    ### вторая строчка кнопок
    # 1
    btn4 = Button(window, bg='black', fg='white', text='1', font=('', 15), command= lambda : input_entry(1, entry))
    btn4.place(x=25, y=142, width=70, height=70)

    # 2
    btn5 = Button(window, bg='black', fg='white', text='2', font=('', 15), command= lambda : input_entry(2, entry))
    btn5.place(x=98, y=142, width=70, height=70)

    # 3
    btn6 = Button(window, bg='black', fg='white', text='3', font=('', 15), command= lambda : input_entry(3, entry))
    btn6.place(x=170, y=142, width=70, height=70)

    # -
    btn_minus = Button(window, bg='black', fg='white', text='-', font=('', 20), command= lambda : input_entry('-', entry))
    btn_minus.place(x=242, y=142, width=70, height=70)


    ### третья строчка кнопок
    # 4
    btn7 = Button(window, bg='black', fg='white', text='4', font=('', 15), command= lambda : input_entry(4, entry))
    btn7.place(x=25, y=214, width=70, height=70)

    # 5
    btn8 = Button(window, bg='black', fg='white', text='5', font=('', 15), command= lambda : input_entry(5, entry))
    btn8.place(x=98, y=214, width=70, height=70)

    # 6
    btn9 = Button(window, bg='black', fg='white', text='6', font=('', 15), command= lambda : input_entry(6, entry))
    btn9.place(x=170, y=214, width=70, height=70)

    # *
    btn_umn = Button(window, bg='black', fg='white', text='x', font=('', 20), command= lambda : input_entry('*', entry))
    btn_umn.place(x=242, y=214, width=70, height=70)


    ### четвертая строчка кнопок
    # 7
    btn7 = Button(window, bg='black', fg='white', text='7', font=('', 15), command= lambda : input_entry(7, entry))
    btn7.place(x=25, y=286, width=70, height=70)

    # 8
    btn8 = Button(window, bg='black', fg='white', text='8', font=('', 15), command= lambda : input_entry(8, entry))
    btn8.place(x=98, y=286, width=70, height=70)

    # 9
    btn9 = Button(window, bg='black', fg='white', text='9', font=('', 20), command= lambda : input_entry(9, entry))
    btn9.place(x=170, y=286, width=70, height=70)

    # ÷
    btn_del = Button(window, bg='black', fg='white', text='÷', font=('', 20), command= lambda : input_entry('÷', entry))
    btn_del.place(x=242, y=286, width=70, height=70)


    ### пятая строчка кнопок
    # %
    btn7 = Button(window, bg='black', fg='white', text='%', font=('', 15), command= lambda : input_entry('%', entry))
    btn7.place(x=25, y=358, width=70, height=70)

    # 0
    btn8 = Button(window, bg='black', fg='white', text='0', font=('', 15), command= lambda : input_entry(0, entry))
    btn8.place(x=98, y=358, width=70, height=70)

    # .
    btn9 = Button(window, bg='black', fg='white', text='.', font=('', 20), command= lambda : input_entry('.', entry))
    btn9.place(x=170, y=358, width=70, height=70)

    # =
    btn_umn = Button(window, bg='red', fg='white', text='=', font=('', 20), command= lambda : answer_send(entry))
    btn_umn.place(x=242, y=358, width=70, height=70)



knopki()
menu_main()
window.mainloop()












