from tkinter import Tk,Label

window = Tk()
window.title("Digital Clock")

window.geometry("600x300")
window.configure(bg='dark green')

label = Label(window, text='Welcome', font=("Arial Black", 78, "bold"), bg='dark green')
label.pack(pady=100)

window.mainloop()