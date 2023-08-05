from time import strftime
from tkinter import Label, Tk

# ======= Configuring window =========
window = Tk()
window.title("savio")
window.geometry("400x160")
window.configure(bg="black")  # =======Background of the clock=====
window.resizable(True, True)  # =====setting a fixed window size =======

clock_label = Label(
    window, bg="Black", fg="White", font=("Arial", 50, "bold"), relief="solid"
)
clock_label.place(x=40, y=40)


def update_label():

    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()

