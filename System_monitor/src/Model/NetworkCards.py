class NetworkCards:

    def __init__(self):

        self.cards = []

    @property
    def get_cards(self):
        return self.cards

    @get_cards.setter
    def set_cards(self, cards):
        self.cards = cards