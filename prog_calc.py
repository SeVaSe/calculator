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
    combo_input['values'] = (
        '1. Бит (bit)', '2. Байт (byte)', '3. Килобайт (KB)', '4. Мегабайт (MB)', '5. Гигабайт (GB)',
        '6. Терабайт (TB)',
        '7. Петабайт (PB)', '8. Эксабайт (EB)')
    combo_input.place(x=30, y=60)

    lbl = Label(prog_window, text='=')
    lbl.place(x=230, y=35)

    combo_output = Combobox(prog_window, width=29, height=13)
    combo_output['values'] = (
        '1. Бит (bit)', '2. Байт (byte)', '3. Килобайт (KB)', '4. Мегабайт (MB)', '5. Гигабайт (GB)',
        '6. Терабайт (TB)',
        '7. Петабайт (PB)', '8. Эксабайт (EB)')
    combo_output.place(x=245, y=60)

    # функция вывода результата конвертации на ENTRY
    def entry_out(conv):
        result_entry.delete(0, END)
        result_entry.insert(0, str(conv))

    # функция вывода уведомления об ошибке
    def entry_error():
        result_entry.delete(0, END)
        result_entry.insert(0, 'Ошибка!')

    def clicked():
        digit = int(digit_input.get())
        unit1 = combo_input.get()
        unit2 = combo_output.get()

        def conversation():
            if unit1 == unit2:
                entry_out(digit)
            elif unit1 == '1. Бит (bit)':
                conv_bit()
            elif unit1 == '2. Байт (byte)':
                conv_byte()
            elif unit1 == '3. Килобайт (KB)':
                conv_kb()
            elif unit1 == '4. Мегабайт (MB)':
                conv_mb()
            elif unit1 == '5. Гигабайт (GB)':
                conv_gb()
            elif unit1 == '6. Терабайт (TB)':
                conv_tb()
            elif unit1 == '7. Петабайт (PB)':
                conv_pb()
            elif unit1 == '8. Эксабайт (EB)':
                conv_eb()

        # функция конвертации битов
        def conv_bit():
            if unit2 == '2. Байт (byte)':
                converted_digit = digit / 8
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = (digit / 8) / 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = ((digit / 8) / 1024) / 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = (((digit / 8) / 1024) / 1024) / 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = ((((digit / 8) / 1024) / 1024) / 1024) / 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = (((((digit / 8) / 1024) / 1024) / 1024) / 1024) / 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 8 / 1024 / 1024 / 1024 / 1024 / 1024 / 1024
                return entry_out(converted_digit)

        # функция конвертации байтов
        def conv_byte():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = digit / 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = digit / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = digit / 1024 / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = digit / 1024 / 1024 / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = digit / 1024 / 1024 / 1024 / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 1024 / 1024 / 1024 / 1024 / 1024 / 1204
                return entry_out(converted_digit)

        # функция конвертации килобайтов
        def conv_kb():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8 * 1024
                return entry_out(converted_digit)

            elif unit2 == '2. Байт (byte)':
                converted_digit = digit * 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = digit / 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = digit / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = digit / 1024 / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = digit / 1024 / 1024 / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 1024 / 1024 / 1024 / 1024 / 1024
                return entry_out(converted_digit)

        # функция конвертации мегабайтов
        def conv_mb():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '2. Байт (byte)':
                converted_digit = digit * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = digit * 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = digit / 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = digit / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = digit / 1024 / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 1024 / 1024 / 1024 / 1024
                return entry_out(converted_digit)

        # функция конвертации гигабайтов
        def conv_gb():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = digit * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = digit * 1024
                return entry_out(converted_digit)

            elif unit2 == '2. Байт (byte)':
                converted_digit = digit * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = digit / 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = digit / 1024 / 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 1024 / 1024 / 1024
                return entry_out(converted_digit)

        # функция конвертации терабайтов
        def conv_tb():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8 * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '2. Байт (byte)':
                converted_digit = digit * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = digit * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = digit * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = digit * 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = digit / 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 1024 / 1024
                return entry_out(converted_digit)

        # функция конвертации петабайтов
        def conv_pb():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8 * 1024 * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '2. Байт (byte)':
                converted_digit = digit * 1024 * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = digit * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = digit * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = digit * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = digit * 1024
                return entry_out(converted_digit)

            elif unit2 == '8. Эксабайт (EB)':
                converted_digit = digit / 1024
                return entry_out(converted_digit)

        # функция конвертации эксабайтов
        def conv_eb():
            if unit2 == '1. Бит (bit)':
                converted_digit = digit * 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '2. Байт (byte)':
                converted_digit = digit * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '3. Килобайт (KB)':
                converted_digit = digit * 1024 * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '4. Мегабайт (MB)':
                converted_digit = digit * 1024 * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '5. Гигабайт (GB)':
                converted_digit = digit * 1024 * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '6. Терабайт (TB)':
                converted_digit = digit * 1024 * 1024
                return entry_out(converted_digit)

            elif unit2 == '7. Петабайт (PB)':
                converted_digit = digit * 1024
                return entry_out(converted_digit)

        conversation()

    # кнопка "Конвертировать"
    btn_convert = Button(prog_window, text='Конвертировать', command=clicked)
    btn_convert.place(x=190, y=100)
