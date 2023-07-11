from tkinter import *
# from mass_calc import open_weight_window
# from prog_calc import open_programming_window

root = Tk()
root.title('Calculator')
root.geometry('350x500')


main_menu = Menu()
main_menu.add_cascade(label="Вес"''' command=open_weight_window''')
main_menu.add_cascade(label="Программист" '''command=open_programming_window''')



root.config(menu=main_menu)
root.mainloop()












