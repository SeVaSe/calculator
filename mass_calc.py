from tkinter import *
from tkinter.ttk import Combobox

# функция для открывания окна
def open_weight_window():
    # окно
    weight_window = Toplevel()
    weight_window.title('Конвертер единиц измерения массы')
    weight_window.geometry('340x500')

    # поле ввода
    digit_input = Entry(weight_window, width=5)
    digit_input.place(x=25, y=30)

    # виджет Combobox для выбора единицы измерения
    combo_input = Combobox(weight_window)
    combo_input['values'] = ('1. Грамм (г)', '2. Килограмм (кг)', '3. Миллиграмм (мг)', '4. Микрограмм (мкг)', '5. Тонна (т)', '6. Фунт (lb)', '7. Унция (oz)', '8. Карат (ct)')
    combo_input.place(x=60, y=30)

    lbl = Label(weight_window, text='Конвертировать в')
    lbl.place(x=60, y=60)

    combo_output = Combobox(weight_window)
    combo_output['values'] = ('1. Грамм (г)', '2. Килограмм (кг)', '3. Миллиграмм (мг)', '4. Микрограмм (мкг)', '5. Тонна (т)', '6. Фунт (lb)', '7. Унция (oz)', '8. Карат (ct)')
    combo_output.place(x=60, y=80)

    # функция отправки значений, необходимых для конвертации
    def clicked():
        digit = int(digit_input.get())
        unit1 = combo_input.get()
        unit2 = combo_output.get()

        #
        def convertation():
            if unit1 == unit2:
                pass
            elif unit1 == '1. Грамм (г)':
                conv_g()
            elif unit1 == '2. Килограмм (кг)':
                conv_kg()
            elif unit1 == '3. Миллиграмм (мг)':
                conv_mg()
            elif unit1 == '4. Микрограмм (мкг)':
                pass
            elif unit1 == '5. Тонна (т)':
                pass
            elif unit1 == '6. Фунт (lb)':
                pass
            elif unit1 == '7. Унция (oz)':
                pass
            elif unit1 == '8. Карат (ct)':
                pass

        # функция конвертации граммов
        def conv_g():
            if unit2 == '2. Килограмм (кг)':
                converted_digit = digit / 1000
                return f'{converted_digit} кг'

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 1000
                return f'{converted_digit} мг'

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000000
                return f'{converted_digit} мкг'

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000000
                return f'{converted_digit} т'

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit / 453592
                return f'{converted_digit} lb'

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit / 28.35
                return f'{converted_digit} oz'

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit / 0.2
                return f'{converted_digit} ct'

        # функция конвертации колиграммов
        def conv_kg():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit * 1000
                return f'{converted_digit} г'

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 1000000
                return f'{converted_digit} мг'

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000000000
                return f'{converted_digit} мкг'

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000
                return f'{converted_digit} т'

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit * 2.205
                return f'{converted_digit} lb'

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 35.274
                return f'{converted_digit} oz'

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 5000
                return f'{converted_digit} ct'

        # функция конвертации миллиграммов
        def conv_mg():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit / 1000
                return f'{converted_digit} г'

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit / 1000000
                return f'{converted_digit} мг'

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000
                return f'{converted_digit} мкг'

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000000000
                return f'{converted_digit} т'

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit * 0.00000220462
                return f'{converted_digit} lb'

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 0.000035274
                return f'{converted_digit} oz'

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 0.005
                return f'{converted_digit} ct'



    # кнопка "Конвертировать"
    btn_convert = Button(weight_window, text='Отправить', command=clicked)
    btn_convert.place(x=60, y=100)

