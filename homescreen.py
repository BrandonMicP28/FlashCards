from tkinter import ttk

from add_card_window import AddCardWindow
from util.database import num_of_cards_in_db
from flashcard_app import FlashcardApp

class HomescreenApp:
    def __init__(self, root):
        self.root = root
        self.flashcard_start_button = None
        self.add_card_button = None
        self.deck_sort_set = None

    def setup_ui(self):
        self.flashcard_start_button = ttk.Button(self.root, text="Flash Cards?", command=self.on_flashcard_start_click, style="flashcard.TButton")
        self.flashcard_start_button.pack(expand=True)

        self.add_card_button = ttk.Button(self.root, text="Add Card?", command=self.on_add_card_click)
        self.add_card_button.pack(expand=True)

        deck_sort_options = ["Unknown", "Known", "Random"]
        self.deck_sort_set = ttk.Combobox(self.root, values = deck_sort_options, state="readonly")
        self.deck_sort_set.current(0)
        self.deck_sort_set.pack(expand=True)

    def on_add_card_click(self):
        AddCardWindow(self.root)

    def on_flashcard_start_click(self):
        selected_sort = self.deck_sort_set.get()

        self.flashcard_start_button.pack_forget()
        self.add_card_button.pack_forget()
        self.deck_sort_set.pack_forget()

        flashcard_app = FlashcardApp(self.root, num_of_cards_in_db(), deck_sort=selected_sort)

        flashcard_app.setup_ui()