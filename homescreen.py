from tkinter import ttk

from database import add_card_to_db
from flashcard import start_flashcard
import tkinter as tk

flashcard_start = None
addCard = None
root = None

def enter_homescreen(main_root):
    global flashcard_start
    global root
    global addCard
    root = main_root

    flashcard_start = ttk.Button(root, text="Flash Cards?", command=leave_home_screen, style="flashcard.TButton")
    flashcard_start.pack(expand=True)

    addCard = ttk.Button(root, text="Add Card?", command=add_card_screen)
    addCard.pack(expand=True)

def add_card_screen():

    def add_card():
        answer = answer_entry.get()
        definition = definition_entry.get()

        if answer == "" or definition == "" or add_card_to_db(answer, definition) < 0:
            status_label = ttk.Label(add_card_window, text = "Word Already Entered", foreground="red")
            status_label.pack()
            add_card_window.after(3000, status_label.destroy)
            return

        status_label = ttk.Label(add_card_window, text = "Word Added!", foreground="green")
        status_label.pack()
        add_card_window.after(3000, status_label.destroy)

    add_card_window = tk.Toplevel(root)
    add_card_window.title("Add Card")
    add_card_window.resizable(False, False)
    add_card_window.geometry("640x640")

    ttk.Label(add_card_window, text="Answer : ").pack()
    answer_entry = ttk.Entry(add_card_window)
    answer_entry.pack()

    ttk.Label(add_card_window, text="Definition : ").pack()
    definition_entry = ttk.Entry(add_card_window)
    definition_entry.pack()

    ttk.Button(add_card_window, text="Add Card", command=add_card).pack()

def leave_home_screen():
    flashcard_start.pack_forget()
    addCard.pack_forget()
    flashcard_app = FlashcardApp(root)
    flashcard_app.setup_ui()