import tkinter as tk
from tkinter import ttk
import database
from database import add_card_to_db


def flip_card():
    print("Fuck You")

def add_card_screen():

    def add_card():
        answer = answer_entry.get()
        definition = definition_entry.get()

        if answer == "" or definition == "":
            return

        add_card_to_db(answer, definition)

    add_card_window = tk.Toplevel(root)
    add_card_window.title("Add Card")
    add_card_window.resizable(False, False)
    add_card_window.geometry("640x640")

    tk.Label(add_card_window, text="Answer : ").pack()
    answer_entry = tk.Entry(add_card_window)
    answer_entry.pack()

    tk.Label(add_card_window, text="Definition : ").pack()
    definition_entry = tk.Entry(add_card_window)
    definition_entry.pack()

    tk.Button(add_card_window, text="Add Card", command=add_card).pack()

def leave_home_screen():
    flashcard_start.pack_forget()
    addCard.pack_forget()
    start_flashcard()

root = tk.Tk()
style = ttk.Style()
root.geometry("1280x720")
root.title("FlashCards")
root.config(background="#33363b")

flashcard_start = ttk.Button(root, text="Flash Cards?", command=start_flashcard, style="flashcard.TButton")
style.configure("flashcard.TButton", font=("Times New Roman", 20), padding=(40,200,40,200))
flashcard_start.pack(expand=True)

addCard = ttk.Button(root, text="Add Card?", command=add_card_screen)
addCard.pack(expand=True)

root.mainloop()