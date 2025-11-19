import sqlite3

def create_database():
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT UNIQUE NOT NULL,
        answer TEXT,
        knowledge INTEGER)''')

def add_card_to_db(question, answer):
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        try:
            c.execute('INSERT INTO cards (question, answer, knowledge) VALUES (?, ?, ?)', (question, answer, 0))
        except sqlite3.IntegrityError:
            return -1
        return c.rowcount

def num_of_cards_in_db() -> int:
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        c.execute("SELECT COUNT(*) FROM cards")
        result = c.fetchone()[0]
        return result

def get_cards_from_db(num_of_cards: int, is_sorted = True) -> tuple:
    with sqlite3.connect('database.db') as connection:
        c = connection.cursor()
        if is_sorted:
            c.execute('SELECT question, answer FROM cards ORDER BY knowledge ASC LIMIT ?', (num_of_cards,))
        return c.fetchall()


create_database()
