class Flashcard:
    def __init__(self, word: str, definition: str, knowledge: int):
        self.word: str = word
        self.definition: str = definition
        self.knowledge: int = knowledge
        self.is_flipped: bool = False

    def flip_card(self):
        self.is_flipped = not self.is_flipped

    def text_showing(self) -> str:
        if self.is_flipped:
            return self.definition
        return self.word