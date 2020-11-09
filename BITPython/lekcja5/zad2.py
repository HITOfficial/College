# Zadanie 2
# Celem ćwiczenia jest napisanie prostego systemu do gry w blackjacka. Jeśli gra nie jest tobie znana, poniżej znajduje się skrócony opis zasad.

# Blackjack to popularna kasynowa gra karciana, w której celem gracza jest pokonanie krupiera poprzez uzyskanie sumy 21 punktów w kartach, nie przekraczając jednak 21. Punktacja kart jest następująca:
# Karty od dwójki do dziesiątki mają wartość równą numerowi karty.
# Walet, Dama i Król mają wartość równą 10 punktów.
# As ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.
# Na początku gry gracz i krupier dostają po dwie karty. Obydwie karty gracza są odkryte, natomiast tylko jedna karta krupiera jest pokazana graczowi. Gracz teraz może podjąć decyzje o swoim następnym ruchu. Gracz ma następujące możliwości:
# Dobrać kartę (hit).
# Nie dobierać kart (stand).
# Jeżeli gracz po dobraniu kart ma więcej niż 21 punktów, przegrywa zakład i krupier zabiera jego żetony. Jeżeli natomiast gracz ma 21 punktów lub mniej, krupier odkrywa swoją zakrytą kartę i w zależności od liczby jego punktów może dobrać więcej kart. Krupier musi grać według następujących przepisów: wziąć kartę, jeżeli ma 16 punktów lub mniej i nie brać więcej kart, gdy ma 17 punktów lub więcej (niezależnie, ile punktów ma gracz). Wygrywa ten, który ma sumę punktów bliższą lub równą 21. 
# W ramach ćwiczenia należy zaimplementować kilka klas: Dealer, Player, Card, służące do przeprowadzenia gry, oraz Parser, który będzie z linii poleceń czytał decyzje gracza. Zastanów się, gdzie będzie użyta asocjacja, agregacja, kompozycja? Dodatkowo można stworzyć klasę AIPlayer, która będzie grać w blackjacka licząc karty.

import sys
import random

class Parser:
    def __init__(self, table):
        self.table = table

    def parser_input(self, decision):
        if decision == 'hit':
            self.table.hit()
        elif decision == 'stand':
            pass
        elif decision == 'leave':
            sys.exit()
        self.table.play()
        else:
            self.parse_input(input('> '))

    def print_situation(self):
            print(self.table)


class Table:
    def __init__(self, players, dealter):
        self.players = players
        self.dealer = dealer
        for _ in range(2):
            self.player.give_card(self.dealer.draw_card())
            self.dealer.give_card(self.dealer.draw_card())

    def __str__(self):
        pass

    def play(self):
        pass

    def hit(self, play):
        card = self.dealer.draw_card()
        self.player.give_card(card)

    def stand(self, play):
        pass

    def end_game(self):
        dealer_cards_value = self.dealer.hand[0].value + self.dealer.hand[1].value

        while dealer_cards_value < 17:
            card = self.dealer.draw_card()
            self.dealer.draw_card(card)
            dealer_cards_value += card.value

        player_score = 21 - self.player.get_hand_value()
        dealer_score = 21 - self.player.get_hand_value()

        if player_score < 0 and dealer_score < 0:
            print('Player wins') if player_score > dealer_score else ('Dealers wins')
        if player_score > 0 and dealer_score < 0:
            print('Dealer wins') if player_score > dealer_score else ('Player wins')
        if player_score < 0 and dealer_score > 0:
            print('Player wins')


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = []

    def __str__(self):
        return f'{self.name} has cards: {str(self.hand)}'

    def give_card(self, card):
        self.hand.append(card)
        self.hand_value += card.value
        self.hand_value.append(card.value)
        
    def get_hand_value(self):
        value = sum(self.hand_value)
        if value > 21 and 11 in self.hand_value:
            for i in range(self.hand_value.count(11)):
                value -= 10
                if value <= 21:
                    break

        return value


class Dealer(Player):
    def __inint__(self, name="Dealer"):
        super(Dealer, self).__init__(name)
        self.deck = Deck()

    def draw_card(self):
        return self.deck.take()


class Card:
    def __init__(self, value, color, figure):
        self.value = value
        self.color = color
        self.figure = figure

    
    def __str__(self):
        return f'{self.figure}, {self.color}'


class Deck:
    def __inint__(self):
        self.cards = []
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11} 

        for color in['pik', 'kier', 'karo', 'trefl']:
            for figure in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(0, color, figure))

        random.shuffle(self.cards)
    
    def take(self):
        return self.cards.pop(0) if self.cards else None

    def reshuffle(self):
        self.__init__()


if __name__ == "__main__":
    parser = Parser()
    player = Player()
    table = Table()
    parser = Parser()

    while True:
        parser.print_situation()
        decision = input('> ')
        parser.parse_input(decisiton)

