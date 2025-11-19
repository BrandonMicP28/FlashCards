import database
from database import num_of_cards_in_db, get_cards_from_db
from tkinter import ttk

class FlashcardApp:
    def __init__(self, root, num_of_cards: int = min(num_of_cards_in_db(), 100), type = "random"):
        self.root = root
        self.num_of_cards = num_of_cards
        self.type = type
        self.cards = get_cards_from_db(self.num_of_cards)
        self.is_flipped = False
        self.current_card = 0

        self.flashcard_button = None
        self.know_button = None
        self.unknown_button = None

    def setup_ui(self):
        if num_of_cards_in_db() > 0:
            flashcard_text = self.cards[self.current_card][0]
        else:
            flashcard_text = ""
        self.flashcard_button = ttk.Button(self.root, text=flashcard_text, style="flashcard.TButton", command=self.flip_card)
        self.flashcard_button.pack(expand=True)

        self.know_button = ttk.Button(self.root, text="✅", command=self.next_flashcard)
        self.know_button.pack(expand=True)

        self.unknown_button = ttk.Button(self.root, text="❌", command=self.next_flashcard)
        self.unknown_button.pack(expand=True)

    def new_deck(self):
        self.cards = get_cards_from_db(self.num_of_cards)


    def flip_card(self):
        self.is_flipped = not self.is_flipped
        self.flashcard_button.configure(text=f"{self.cards[self.current_card][1 if self.is_flipped else 0]}")

    def next_flashcard(self) -> bool:
        if self.current_card < self.num_of_cards - 1:
            self.current_card += 1
        else:
            return False

        self.is_flipped = False

        self.flashcard_button.configure(text=f"{self.cards[self.current_card][1 if self.is_flipped else 0]}")
        return True
