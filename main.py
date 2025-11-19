import tkinter as tk
from tkinter import ttk, messagebox
import database
from database import add_card_to_db
from flashcard import start_flashcard
from homescreen import enter_homescreen

if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style()
    root.geometry("1280x720")
    root.title("FlashCards")
    root.config(background="#33363b")

    style.configure("flashcard.TButton", font=("Times New Roman", 20), padding=(40, 200, 40, 200))

    enter_homescreen(root)

    root.mainloop()