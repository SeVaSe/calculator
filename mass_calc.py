from tkinter import *
from tkinter.ttk import Combobox

# функция для открывания окна
def open_weight_window():
    # окно
    weight_window = Toplevel()
    weight_window.title('Конвертатор единиц измерения массы')
    weight_window.geometry('340x500')

    # поле ввода
    digit_input = Entry(weight_window, width=5)
    digit_input.place(x=25, y=30)

    # виджет Combobox для выбора единицы измерения
    combo_input = Combobox(weight_window)
    combo_input['values'] = ('1. Грамм (г)', '2. Килограмм (кг)', '3. Миллиграмм (мг)', '4. Микрограмм (мкг)', '5. Тонна (т)', '6. Фунт (lb)', '7. Унция (oz)')
    combo_input.place(x=60, y=30)

    lbl = Label(weight_window, text='Конвертировать в')
    lbl.place(x=60, y=60)

    combo_output = Combobox(weight_window)
    combo_output['values'] = ('1. Грамм (г)', '2. Килограмм (кг)', '3. Миллиграмм (мг)', '4. Микрограмм (мкг)', '5. Тонна (т)', '6. Фунт (lb)', '7. Унция (oz)')
    combo_output.place(x=60, y=80)

    # функция отправки значений, необходимых для конвертации
    def clicked():
        digit = digit_input.get()
        unit1 = combo_input.get()
        unit2 = combo_output.get()

        if unit1 == '1. Грамм (г)' and unit2 == '2. Килограмм (кг)':
            def conv_g_and_kg():
                converted_digit = digit * 1000
                return f'{converted_digit} кг'
            conv_g_and_kg()

    # кнопка "Конвертировать"
    btn_convert = Button(weight_window, text='Отправить', command=clicked())
    btn_convert.place(x=60, y=100)


