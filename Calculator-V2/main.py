import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Calculator")
app.geometry("345x580")

max_chiffres = 9
pile_ecran = []
current_nbr = False
current_operation = False

#Fonction

def update_screen(value=False):
    if value:
        screen.configure(text=value)
    else:
        screen.configure(text="0")

def get_number_from_pile():
    number = ""
    for digit in pile_ecran:
        number += str(digit)
    return number

def press_btn(btn):
    if btn.isdigit() or (btn == "." and "." not in pile_ecran):
        num_btn(btn)
    elif btn in ["+", "-", "*", "÷", "^"]:
        operation_btn(btn)
    update_screen(get_number_from_pile())

def num_btn(btn):
    if len(pile_ecran) >= max_chiffres:
        return pile_ecran
    pile_ecran.append(btn)
    return pile_ecran

def operation_btn(btn):
    global current_nbr, current_operation
    if current_nbr and current_operation:
        #execute
    if not current_nbr:
        current_nbr = float(get_number_from_pile()) if "." in get_number_from_pile() else int(get_number_from_pile())



#----------Ecran-------------#
screen_font = ('Courier', 55, 'bold')
screen= customtkinter.CTkLabel(app, text="0", font=screen_font, fg_color="black")
screen.grid(row=1, column=0, sticky="E", padx=(10, 10), pady=(30, 10), columnspan=4)

#----------Buttons-------------#
buttons_font = ('Arial', 30, 'bold')

pad = customtkinter.CTkLabel(app, text="")
pad.grid(row=2, column=0, sticky="WE", padx=(0, 0), pady=(10, 0), columnspan=5)

#Digits
btn_0 = customtkinter.CTkButton(pad, text="0", width=75, height=75, font=buttons_font, command=lambda : press_btn("0"))
btn_1 = customtkinter.CTkButton(pad, text="1", width=75, height=75, font=buttons_font, command=lambda : press_btn("1"))
btn_2 = customtkinter.CTkButton(pad, text="2", width=75, height=75, font=buttons_font, command=lambda : press_btn("2"))
btn_3 = customtkinter.CTkButton(pad, text="3", width=75, height=75, font=buttons_font, command=lambda : press_btn("3"))
btn_4 = customtkinter.CTkButton(pad, text="4", width=75, height=75, font=buttons_font, command=lambda : press_btn("4"))
btn_5 = customtkinter.CTkButton(pad, text="5", width=75, height=75, font=buttons_font, command=lambda : press_btn("5"))
btn_6 = customtkinter.CTkButton(pad, text="6", width=75, height=75, font=buttons_font, command=lambda : press_btn("6"))
btn_7 = customtkinter.CTkButton(pad, text="7", width=75, height=75, font=buttons_font, command=lambda : press_btn("7"))
btn_8 = customtkinter.CTkButton(pad, text="8", width=75, height=75, font=buttons_font, command=lambda : press_btn("8"))
btn_9 = customtkinter.CTkButton(pad, text="9", width=75, height=75, font=buttons_font, command=lambda : press_btn("9"))

btn_0.grid(row=5, column=2, padx=(5, 5), pady=(5, 0))
btn_1.grid(row=4, column=1, padx=(5, 5), pady=(5, 5))
btn_2.grid(row=4, column=2, padx=(5, 5), pady=(5, 5))
btn_3.grid(row=4, column=3, padx=(5, 5), pady=(5, 5))
btn_4.grid(row=3, column=1, padx=(5, 5), pady=(5, 5))
btn_5.grid(row=3, column=2, padx=(5, 5), pady=(5, 5))
btn_6.grid(row=3, column=3, padx=(5, 5), pady=(5, 5))
btn_7.grid(row=2, column=1, padx=(5, 5), pady=(5, 5))
btn_8.grid(row=2, column=2, padx=(5, 5), pady=(5, 5))
btn_9.grid(row=2, column=3, padx=(5, 5), pady=(5, 5))

#Operations
btn_plus = customtkinter.CTkButton(pad, text="+", width=75, height=75, font=buttons_font, command=lambda : press_btn("+"))
btn_minus = customtkinter.CTkButton(pad, text="-", width=75, height=75, font=buttons_font, command=lambda : press_btn("-"))
btn_factor = customtkinter.CTkButton(pad, text="x", width=75, height=75, font=buttons_font, command=lambda : press_btn("x"))
btn_division = customtkinter.CTkButton(pad, text="÷", width=75, height=75, font=buttons_font, command=lambda : press_btn("÷"))
btn_power = customtkinter.CTkButton(pad, text="^", width=75, height=75, font=buttons_font, command=lambda : press_btn("^"))

btn_plus.grid(row=4, column=4, padx=(5, 0), pady=(5, 0))
btn_minus.grid(row=3, column=4, padx=(5, 0), pady=(5, 0))
btn_factor.grid(row=2, column=4, padx=(5, 0), pady=(5, 0))
btn_division.grid(row=1, column=4, padx=(5, 0), pady=(5, 0))
btn_power.grid(row=5, column=1, padx=(5, 0), pady=(5, 0))

#Other
btn_dot = customtkinter.CTkButton(pad, text=".", width=75, height=75, font=buttons_font, command=lambda : press_btn("."))
btn_parenthesis_left = customtkinter.CTkButton(pad, text="(", width=75, height=75, font=buttons_font, command=lambda : press_btn("("))
btn_parenthesis_right = customtkinter.CTkButton(pad, text=")", width=75, height=75, font=buttons_font, command=lambda : press_btn(")"))
btn_reset = customtkinter.CTkButton(pad, text="CE", width=75, height=75, font=buttons_font, command=lambda : press_btn("CE"))
btn_equal = customtkinter.CTkButton(pad, text="=", height=75, width=75, font=buttons_font, command=lambda : press_btn("="))

btn_dot.grid(row=5, column=3, padx=(5, 5), pady=(5, 0))
btn_parenthesis_left.grid(row=1, column=2, padx=(5, 5), pady=(5, 5))
btn_parenthesis_right.grid(row=1, column=3, padx=(5, 5), pady=(5, 5))
btn_reset.grid(row=1, column=1, padx=(5, 5), pady=(5, 5))
btn_equal.grid(row=5, column=4, padx=(5, 5), pady=(5, 0))

app.mainloop()