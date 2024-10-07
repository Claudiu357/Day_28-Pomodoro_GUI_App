from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

canva = Canvas(width=200, height=224)
apple_img = PhotoImage(file="tomato.png")
canva.create_image(103, 112, image=apple_img)
canva.create_text(103, 130, text="00:00", fill="white", font=("Courier", 20, "bold"))

canva.pack()

window.mainloop()