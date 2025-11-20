from flashcard import Flashcard
from util.database import num_of_cards_in_db, get_cards_from_db, change_word_knowledge
from tkinter import ttk

class FlashcardApp:
    def __init__(self, root, num_of_cards: int, deck_sort = "Unknown"):
        self.root = root
        self.num_of_cards = num_of_cards
        self.deck_sort = deck_sort
        self.cards = get_cards_from_db(self.num_of_cards, self.deck_sort)

        self.cards.append(Flashcard("Finished Pack", "Finished Pack", -1))
        self.num_of_cards += 1

        self.current_card_inx = 0

        if num_of_cards > 0:
            self.current_card = self.cards[0]
        else:
            self.current_card = None

        self.flashcard_button = None
        self.know_button = None
        self.unknown_button = None

    def on_know_click(self):
        if self.current_card.knowledge < 10:
            change_word_knowledge(self.current_card.word, 1)
            self.current_card.knowledge += 1
        self.next_flashcard()

    def on_unknown_click(self):
        if self.current_card.knowledge > 0:
            change_word_knowledge(self.current_card.word, -1)
            self.current_card.knowledge -= 1
        self.next_flashcard()

    def on_flashcard_click(self):
        if self.current_card_inx < self.num_of_cards - 1:
            self.flip_card()
        else:
            self.restart_flashcards()

    def setup_ui(self):
        if num_of_cards_in_db() > 0:
            flashcard_text = self.current_card.text_showing()
        else:
            flashcard_text = ""
        self.flashcard_button = ttk.Button(self.root, text=flashcard_text, style="flashcard.TButton", command=self.on_flashcard_click)
        self.flashcard_button.pack(expand=True)

        self.know_button = ttk.Button(self.root, text="✅", command=self.on_know_click)
        self.know_button.pack(expand=True)

        self.unknown_button = ttk.Button(self.root, text="❌", command=self.on_unknown_click)
        self.unknown_button.pack(expand=True)

    def new_deck(self):
        self.cards = get_cards_from_db(self.num_of_cards)
        self.cards.append(Flashcard("Finished Pack","Finished Pack", -1))

    def flip_card(self):
        self.current_card.flip_card()
        self.update_card()

    def next_flashcard(self) -> bool:
        if self.current_card_inx < self.num_of_cards - 1:
            self.current_card_inx += 1
        else:
            self.restart_flashcards()
            return False

        self.update_card()
        return True

    def update_card(self):
        self.current_card = self.cards[self.current_card_inx]
        self.flashcard_button.configure(text=self.current_card.text_showing())

    def restart_flashcards(self):
        self.current_card_inx = 0
        self.update_card()
