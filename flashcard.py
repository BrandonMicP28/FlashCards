import database
from database import num_of_cards_in_db


def start_flashcard(cards = num_of_cards_in_db(), type = "random"):
    for i in range(cards):
        print(database.get_card_from_db(i))