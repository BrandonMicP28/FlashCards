import tkinter as tk
from tkinter import ttk

from homescreen import HomescreenApp

if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style()
    root.geometry("1280x720")
    root.title("FlashCards")
    root.config(background="#33363b")

    style.configure("flashcard.TButton", font=("Times New Roman", 20), padding=(40, 200, 40, 200))

    home = HomescreenApp(root)
    home.setup_ui()

    root.mainloop()