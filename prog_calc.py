from tkinter import *
from tkinter.ttk import Combobox

# функция открывания окна
def open_programming_window():
    prog_window = Toplevel()
    prog_window.title('Конвертер единиц измерения объёма информации')
    prog_window.geometry('500x150')
    prog_window.resizable(height=False, width=False)

    digit_input = Entry(prog_window, width=13, font=('', 20))
    digit_input.place(x=30, y=30)

    result_entry = Entry(prog_window, width=13, font=('', 20))
    result_entry.place(x=245, y=30)

    # виджет Combobox для выбора единицы измерения
    combo_input = Combobox(prog_window, width=29, height=13)
    combo_input['values'] = ('1. Бит (bit)', '2. Байт (byte)', '3. Килобайт (KB)', '4. Мегабайт (MB)', '5. Гигабайт (GB)', '6. Терабайт (TB)', '7. Петабайт (PB)', '8. Эксабайт (EB)')
    combo_input.place(x=30, y=60)

    lbl = Label(prog_window, text='=')
    lbl.place(x=230, y=35)

    combo_output = Combobox(prog_window, width=29, height=13)
    combo_output['values'] = ('1. Бит (bit)', '2. Байт (byte)', '3. Килобайт (KB)', '4. Мегабайт (MB)', '5. Гигабайт (GB)', '6. Терабайт (TB)', '7. Петабайт (PB)', '8. Эксабайт (EB)')
    combo_output.place(x=245, y=60)





