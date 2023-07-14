from tkinter import *
from mass_calc import open_weight_window
from prog_calc import open_programming_window

window = Tk()
window['bg'] = 'black'
window.title('Calculator')
window.geometry('291x502')
window.resizable(height=False, width=False)


# функция меню, для перехода в калькуляторы: массы и программиста
def menu_main():
    main_menu = Menu(bg="#666666", fg="white")
    main_menu.add_cascade(label="Вес", command=open_weight_window)
    main_menu.add_cascade(label="Программист", command=open_programming_window)
    window.config(menu=main_menu)


# наш textBox
def input_entry(znak, entry):
    if 'abs' not in znak and '√' not in znak: # если нет корня, модуля и процентов, то просто выводим выражение
        entry.insert(END, znak)
    elif 'abs' in znak:  # обрабатываем модуль
        strok = entry.get()
        chislo_abs = strok.split(' ', 1) # делим по пробелу на число и на знак модуля
        abs_osn = f'abs({chislo_abs[0]})' # отбираем число и меняем модуль, на понятное изложение для компьютера
        entry.delete(0, END)
        entry.insert(END, abs_osn)
    elif '√' in znak: # обрабатываем корень
        strok = entry.get()
        sqrt_znak = strok.split(' ', 1) # делим по пробелу на число и на знак корня
        sqrt_osn = f'{sqrt_znak[0]}**0.5' # отбираем число и меняем корень, на понятное изложение для компьютера
        entry.delete(0, END)
        entry.insert(END, sqrt_osn)




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

# вычисления
def answer_send(strok_entry):
    strok = strok_entry.get()


    try:
        if '%' in strok:
            numbers = strok.split(' ')
            num = float(numbers[0])
            percent = float(numbers[1].strip('%'))
            result = (num * percent) / 100
            strok_entry.delete(0, END)
            strok_entry.insert(0, result)
        else:
            strok_entry.delete(0, END)
            strok_entry.insert(0, eval(strok))

    except:
        strok_entry.insert(0, 'Ошибка!')








# функция расстановки кнопок
def knopki():
    # строка ввода
    entry = Entry(window, width=19, font=('', 20), bg="black", fg="white")
    entry.place(x=2, y=30)


    ### первая строчка кнопок
    # возвести в степень
    btn1 = Button(window, bg='#333333', fg='#3366FF', text='x^?', font=('', 15, 'bold'), command= lambda : input_entry('**', entry))
    btn1.place(x=2, y=70, width=70, height=70)

    # стереть все
    btn2 = Button(window, bg='#333333', fg='#3366FF', text='C', font=('', 15, 'bold'), command= lambda : clear_entry(entry))
    btn2.place(x=75, y=70, width=70, height=70)

    # удалить один последний символ
    btn3 = Button(window, bg='#333333', fg='#3366FF', text='del', font=('', 15, 'bold'), command= lambda : delete_znak(entry))
    btn3.place(x=147, y=70, width=70, height=70)

    # +
    btn_plus = Button(window, bg='#333333', fg='#3366FF', text='+', font=('', 20, 'bold'), command= lambda : input_entry('+', entry))
    btn_plus.place(x=219, y=70, width=70, height=70)


    ### вторая строчка кнопок
    # 1
    btn4 = Button(window, bg='#333333', fg='white', text='1', font=('', 15, 'bold'), command= lambda : input_entry('1', entry))
    btn4.place(x=2, y=142, width=70, height=70)

    # 2
    btn5 = Button(window, bg='#333333', fg='white', text='2', font=('', 15, 'bold'), command= lambda : input_entry('2', entry))
    btn5.place(x=75, y=142, width=70, height=70)

    # 3
    btn6 = Button(window, bg='#333333', fg='white', text='3', font=('', 15, 'bold'), command= lambda : input_entry('3', entry))
    btn6.place(x=147, y=142, width=70, height=70)

    # -
    btn_minus = Button(window, bg='#333333', fg='#3366FF', text='-', font=('', 20, 'bold'), command= lambda : input_entry('-', entry))
    btn_minus.place(x=219, y=142, width=70, height=70)


    ### третья строчка кнопок
    # 4
    btn7 = Button(window, bg='#333333', fg='white', text='4', font=('', 15, 'bold'), command= lambda : input_entry('4', entry))
    btn7.place(x=2, y=214, width=70, height=70)

    # 5
    btn8 = Button(window, bg='#333333', fg='white', text='5', font=('', 15, 'bold'), command= lambda : input_entry('5', entry))
    btn8.place(x=75, y=214, width=70, height=70)

    # 6
    btn9 = Button(window, bg='#333333', fg='white', text='6', font=('', 15, 'bold'), command= lambda : input_entry('6', entry))
    btn9.place(x=147, y=214, width=70, height=70)

    # *
    btn_umn = Button(window, bg='#333333', fg='#3366FF', text='x', font=('', 20, 'bold'), command= lambda : input_entry('*', entry))
    btn_umn.place(x=219, y=214, width=70, height=70)


    ### четвертая строчка кнопок
    # 7
    btn7 = Button(window, bg='#333333', fg='white', text='7', font=('', 15, 'bold'), command= lambda : input_entry('7', entry))
    btn7.place(x=2, y=286, width=70, height=70)

    # 8
    btn8 = Button(window, bg='#333333', fg='white', text='8', font=('', 15, 'bold'), command= lambda : input_entry('8', entry))
    btn8.place(x=75, y=286, width=70, height=70)

    # 9
    btn9 = Button(window, bg='#333333', fg='white', text='9', font=('', 15, 'bold'), command= lambda : input_entry('9', entry))
    btn9.place(x=147, y=286, width=70, height=70)

    # ÷
    btn_del = Button(window, bg='#333333', fg='#3366FF', text='÷', font=('', 20, 'bold'), command= lambda : input_entry('/', entry))
    btn_del.place(x=219, y=286, width=70, height=70)


    ### пятая строчка кнопок
    # (
    btn8 = Button(window, bg='#333333', fg='white', text='(', font=('', 15, 'bold'), command=lambda: input_entry('(', entry))
    btn8.place(x=2, y=358, width=70, height=70)

    # 0
    btn8 = Button(window, bg='#333333', fg='white', text='0', font=('', 15, 'bold'), command= lambda : input_entry('0', entry))
    btn8.place(x=75, y=358, width=70, height=70)

    # )
    btn8 = Button(window, bg='#333333', fg='white', text=')', font=('', 15, 'bold'), command=lambda: input_entry(')', entry))
    btn8.place(x=147, y=358, width=70, height=70)

    # %
    btn8 = Button(window, bg='#333333', fg='#3366FF', text='%', font=('', 15, 'bold'), command=lambda: input_entry(' %', entry))
    btn8.place(x=219, y=358, width=70, height=70)


    ### шестая строчка кнопок
    # |x|
    btn_persent = Button(window, bg='#333333', fg='#3366FF', text='|x|', font=('', 15, 'bold'), command=lambda: input_entry(' abs', entry))
    btn_persent.place(x=75, y=430, width=70, height=70)

    # sqrt
    btn_sqrt = Button(window, bg='#333333', fg='#3366FF', text='√', font=('', 20, 'bold'), command=lambda: input_entry(' √', entry))
    btn_sqrt.place(x=2, y=430, width=70, height=70)

    # .
    btn9 = Button(window, bg='#333333', fg='#3366FF', text='.', font=('', 20, 'bold'), command= lambda : input_entry('.', entry))
    btn9.place(x=147, y=430, width=70, height=70)

    # =
    btn_umn = Button(window, bg='#0066FF', fg='white', text='=', font=('', 20, 'bold'), command= lambda : answer_send(entry))
    btn_umn.place(x=219, y=430, width=70, height=70)



knopki()
menu_main()
window.mainloop()












