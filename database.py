import sqlite3
from typing import Any

from flashcard import Flashcard


def create_database():
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE NOT NULL,
        answer TEXT,
        knowledge INTEGER)''')

def add_card_to_db(word, answer):
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        try:
            c.execute('INSERT INTO cards (word, answer, knowledge) VALUES (?, ?, ?)', (word, answer, 0))
        except sqlite3.IntegrityError:
            return -1
        return c.rowcount

def num_of_cards_in_db() -> int:
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        c.execute("SELECT COUNT(*) FROM cards")
        result = c.fetchone()[0]
        return result

def get_cards_from_db(num_of_cards: int, deck_sort = "unknown") -> list[Flashcard]:
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        if deck_sort == "unknown":
            c.execute('SELECT word, answer, knowledge FROM cards ORDER BY knowledge ASC LIMIT ?', (num_of_cards,))
        elif deck_sort == "known":
            c.execute('SELECT word, answer, knowledge FROM cards ORDER BY knowledge DEC LIMIT ?', (num_of_cards,))
        elif deck_sort == "random":
            c.execute('SELECT word, answer, knowledge FROM cards ORDER BY RANDOM() LIMIT ?', (num_of_cards,))
        else:
            raise ValueError(f"deck_sort must be one of 'unknown', 'known', or 'random'")

        return [Flashcard(raw_card[0], raw_card[1], raw_card[2]) for raw_card in c.fetchall()]



def change_word_knowledge(word: str, amt: int) -> bool:
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        c.execute("UPDATE cards SET knowledge = knowledge + ? WHERE word = ?", (amt, word))


create_database()
