from tkinter import *
from tkinter.ttk import Combobox

# функция для открывания окна
def open_weight_window():
    # окно
    weight_window = Toplevel()
    weight_window.title('Конвертер единиц измерения массы')
    weight_window.geometry('500x150')
    weight_window.resizable(height=False, width=False)

    # поле ввода
    digit_input = Entry(weight_window, width=13, font=('', 20))
    digit_input.place(x=30, y=30)

    result_entry = Entry(weight_window, width=13, font=('', 20))
    result_entry.place(x=245, y=30)

    # виджет Combobox для выбора единицы измерения
    combo_input = Combobox(weight_window, width=29, height=13)
    combo_input['values'] = ('1. Грамм (г)', '2. Килограмм (кг)', '3. Миллиграмм (мг)', '4. Микрограмм (мкг)', '5. Тонна (т)', '6. Фунт (lb)', '7. Унция (oz)', '8. Карат (ct)')
    combo_input.place(x=30, y=60)

    lbl = Label(weight_window, text='=')
    lbl.place(x=230, y=35)

    combo_output = Combobox(weight_window, width=29, height=13)
    combo_output['values'] = ('1. Грамм (г)', '2. Килограмм (кг)', '3. Миллиграмм (мг)', '4. Микрограмм (мкг)', '5. Тонна (т)', '6. Фунт (lb)', '7. Унция (oz)', '8. Карат (ct)')
    combo_output.place(x=245, y=60)

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
                conv_mcg()
            elif unit1 == '5. Тонна (т)':
                conv_t()
            elif unit1 == '6. Фунт (lb)':
                conv_lb()
            elif unit1 == '7. Унция (oz)':
                pass
            elif unit1 == '8. Карат (ct)':
                pass

        # функция конвертации граммов
        def conv_g():
            if unit2 == '2. Килограмм (кг)':
                converted_digit = digit / 1000
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 1000
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000000
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000000
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit / 453592
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit / 28.35
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit / 0.2
                return converted_digit

        # функция конвертации килограммов
        def conv_kg():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit * 1000
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 1000000
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000000000
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit * 2.205
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 35.274
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 5000
                return converted_digit

        # функция конвертации миллиграммов
        def conv_mg():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit / 1000
                return converted_digit

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit / 1000000
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000000000
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit * 0.00000220462
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 0.000035274
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 0.005
                return converted_digit

        # функция конвертации микрограммов
        def conv_mcg():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit / 1000000
                return converted_digit

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit / 1000000000
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit / 1000
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 1000000000000
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit * 0.00000000220462
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 0.000000035274
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 0.000005
                return converted_digit

        # функция конвертации тонн
        def conv_t():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit * 1000000
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 1000000000
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 1000000000000
                return converted_digit

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit * 1000
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit * 2204.62
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 35274
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 5000000
                return converted_digit

            # функция конвертации фунтов
        def conv_lb():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit * 453.6
                return converted_digit

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit * 0.453592
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 453592.37
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 453592370
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit * 0.000453592
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit * 16
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 453.59237
                return converted_digit

        # функция конвертации унций
        def conv_oz():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit * 28.35
                return converted_digit

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit * 35.273
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 28350
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 28349.52
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit * 0.0000283495
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit / 16
                return converted_digit

            elif unit2 == '8. Карат (ct)':
                converted_digit = digit * 141.7475
                return converted_digit

        # функция конвертации каратов
        def conv_ct():
            if unit2 == '1. Грамм (г)':
                converted_digit = digit * 0.2
                return converted_digit

            elif unit2 == '2. Килограмм (кг)':
                converted_digit = digit * 0.0002
                return converted_digit

            elif unit2 == '3. Миллиграмм (мг)':
                converted_digit = digit * 200
                return converted_digit

            elif unit2 == '4. Микрограмм (мкг)':
                converted_digit = digit * 200000
                return converted_digit

            elif unit2 == '5. Тонна (т)':
                converted_digit = digit / 5000
                return converted_digit

            elif unit2 == '6. Фунт (lb)':
                converted_digit = digit / 2268
                return converted_digit

            elif unit2 == '7. Унция (oz)':
                converted_digit = digit / 141.7
                return converted_digit


    # кнопка "Конвертировать"
    btn_convert = Button(weight_window, text='Конвертировать', command=clicked)
    btn_convert.place(x=190, y=100)

