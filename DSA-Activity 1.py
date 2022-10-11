from math import pi
from tkinter import *


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Circle")
        self.geometry("400x200")

        self.__my_canvas = Canvas(self, width=400, height=200)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        # Texts in the display--------------------------------------------
        self.__my_canvas.create_text(200, 20, text='Circle Area Calculator', fill='black',
                                     justify="center", font=('Times New Roman', 15))
        self.__my_canvas.create_text(200, 45, text='----Input Radius/Diameter----', fill='black',
                                     justify="center", font=('Times New Roman', 13))
        self.__my_canvas.create_text(100, 90, text='Radius', fill='black',
                                     justify="center", font=('Times New Roman', 15))
        self.__my_canvas.create_text(300, 90, text='Diameter', fill='black',
                                     justify="center", font=('Times New Roman', 15))

        # Getting the area of circle depending on the given--------------------------------------------
        def equal():
            radius = display_radius.get()
            diameter = display_diameter.get()
            display_area.delete(0, END)

            if radius and diameter != "":
                display_area.insert(0, "Multiple Inputs Found")

            elif radius != "":
                try:
                    area_r = pi * (int(radius) ** 2)
                except:
                    if radius == "":
                        area_r = ""
                    else:
                        area_r = "Syntax Error"
                display_area.insert(0, area_r)

            else:
                try:
                    area_d = (pi * (int(diameter) ** 2)) / 4
                except:
                    if diameter == "":
                        area_d = ""
                    else:
                        area_d = "Syntax Error"
                display_area.insert(0, area_d)

        # Entry fields for computation--------------------------------------------
        display_radius = Entry(self, font=("Times New Roman", 12), background="#6A94B5", foreground="#D3FFF3",
                               insertwidth=1, width=20, justify="center")
        display_diameter = Entry(self, font=("Times New Roman", 12), background="#6A94B5", foreground="#D3FFF3",
                                 insertwidth=1, width=20, justify="center")

        display_area = Entry(self, font=("Times New Roman", 12), background="#6A94B5", foreground="#D3FFF3",
                             insertwidth=1, width=20, justify="center")

        # Placing the entry fields in the canvas--------------------------------------------
        self.__my_canvas.create_window(100, 110, anchor="center", window=display_radius)
        self.__my_canvas.create_window(300, 110, anchor="center", window=display_diameter)
        self.__my_canvas.create_window(200, 180, anchor="center", window=display_area)

        # Button for solving the area of the circle--------------------------------------------
        btn_solve = Button(self, text="Solve", width=8, font=("Times New Roman", 12), command=equal)
        self.__my_canvas.create_window(200, 145, anchor="center", window=btn_solve)

Window().mainloop()
