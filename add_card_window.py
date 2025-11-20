import tkinter as tk
from tkinter import ttk

from util.database import add_card_to_db


class AddCardWindow:
    def __init__(self, root):
        self.add_card_window = tk.Toplevel(root)
        self.add_card_window.title("Add Card")
        self.add_card_window.resizable(False, False)
        self.add_card_window.geometry("640x640")

        ttk.Label(self.add_card_window, text="Word : ").pack()
        self.word_entry = ttk.Entry(self.add_card_window)
        self.word_entry.pack()

        ttk.Label(self.add_card_window, text="Definition : ").pack()
        self.definition_entry = ttk.Entry(self.add_card_window)
        self.definition_entry.pack()

        ttk.Button(self.add_card_window, text="Add Card", command=self.add_card).pack()

    def add_card(self):
        word = self.word_entry.get()
        definition = self.definition_entry.get()

        if word == "" or definition == "" or add_card_to_db(word, definition) < 0:
            status_label = ttk.Label(self.add_card_window, text="Word Already Entered", foreground="red")
            status_label.pack()
            self.add_card_window.after(3000, status_label.destroy)
            return

        status_label = ttk.Label(self.add_card_window, text="Word Added!", foreground="green")
        status_label.pack()
        self.add_card_window.after(3000, status_label.destroy)
