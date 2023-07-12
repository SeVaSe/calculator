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

        # конвертация граммов

        if unit1 == '1. Грамм (г)' and unit2 == '2. Килограмм (кг)':
            # функция конвертации граммов в килограммы
            def conv_g_to_kg():
                converted_digit = digit/1000
                return f'{converted_digit} кг'
            conv_g_to_kg()


        elif unit1 == '1. Грамм (г)' and unit2 == '3. Миллиграмм (мг)':
            # функция конвертации граммов в миллиграммы
            def conv_g_to_mg():
                converted_digit = digit * 1000
                return f'{converted_digit} мг'
            conv_g_to_mg()


        elif unit1 == '1. Грамм (г)' and unit2 == '4. Микрограмм (мкг)':
            # функция конвертации граммов в микрограммы
            def conv_g_to_mcg():
                converted_digit = digit * 1000000
                return f'{converted_digit} мкг'
            conv_g_to_mcg()


        elif unit1 == '1. Грамм (г)' and unit2 == '5. Тонна (т)':
            # функция конвертации граммов в тонны
            def conv_g_to_t():
                converted_digit = digit/1000000
                return f'{converted_digit} т'
            conv_g_to_t()


        elif unit1 == '1. Грамм (г)' and unit2 == '6. Фунт (lb)':
            # функция конвертации граммов в фунты
            def conv_g_to_lb():
                converted_digit = digit/453592
                return f'{converted_digit} lb'
            conv_g_to_lb()


        elif unit1 == '1. Грамм (г)' and unit2 == '7. Унция (oz)':
            # функция конвертации граммов в унции
            def conv_g_to_oz():
                converted_digit = digit/28.35
                return f'{converted_digit} oz'
            conv_g_to_oz()


        elif unit1 == '1. Грамм (г)' and unit2 == '8. Карат (ct)':
            # функция конвертации граммов в караты
            def conv_g_to_ct():
                converted_digit = digit/0.2
                return f'{converted_digit} oz'
            conv_g_to_ct()

    # кнопка "Конвертировать"
    btn_convert = Button(weight_window, text='Отправить', command=clicked)
    btn_convert.place(x=60, y=100)


