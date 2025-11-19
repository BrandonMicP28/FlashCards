import database
from database import num_of_cards_in_db, get_cards_from_db
from tkinter import ttk

def flip_card():
    global is_flipped
    is_flipped = not is_flipped

    if is_flipped:
        flashcard.configure(text=f"{cards[current_card + 1]}")
    else:
        flashcard.configure(text=f"{cards[current_card]}")

def start_flashcard(root, num_of_cards: int = min(num_of_cards_in_db(), 100), type = "random"):

    global cards
    global flashcard

    cards = get_cards_from_db(num_of_cards)

    flashcard = ttk.Button(root, text = f"{cards[current_card]}", style = "flashcard.TButton", command = flip_card)
    flashcard.pack(expand=True)

cards: tuple = None
current_card: int = 0
is_flipped: bool = False
flashcard: ttk.Button = None