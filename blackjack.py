import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def printing_name(self):
        print(self.suit + " " + self.rank)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def remove_card(self):
        popped_card = self.deck.pop()
        return popped_card


class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_cart(self, card):
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        return self.value

    def aced_value(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def remove_hand(self):
        self.hand = []
        self.value = 0
        self.aces = 0



class Chips:
    def __init__(self):
        self.balance = 1000
        self.bet = 0

    def win_bet(self):
        self.balance += self.bet

    def lose_bet(self):
        self.balance -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.balance:
                print("Sorry, your bet can't exceed", chips.balance)
                continue
            else:
                break


def hit(deck, hand):
    hand.add_cart(deck.remove_card())
    hand.aced_value()


def hit_or_stand(deck, hand):
    while hand.value < 22:
        a = input("Hit or stand?")
        if a[0].lower() == "h":
            hit(deck, hand)
            show_some(player, dealer)
            continue
        elif a[0].lower() == "s":
            print("Player stands. Dealers Turn")
            break
        else:
            print("Try again.")
            continue


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.hand[1])
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    print("Value of hand " + str(player.value))


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.hand, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    print("Player's Hand =", player.value)
    print("Value of hand" + str(player.value))


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")




deck = Deck()
deck.shuffle()
player = Hand()
dealer = Hand()
player_chips = Chips()

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    take_bet(player_chips)
    player.add_cart(deck.remove_card())
    dealer.add_cart(deck.remove_card())
    player.add_cart(deck.remove_card())
    dealer.add_cart(deck.remove_card())
    show_some(player, dealer)
    while playing:
        hit_or_stand(deck, player)
        show_some(player, dealer)
        if player.value > 21:
            show_all(player, dealer)
            player_busts(player, dealer, player_chips)
            playing = False
        elif player.value < 22:
            while dealer.value < 17:
                hit(deck, dealer)
            if dealer.value > 21:
                show_all(player, dealer)
                dealer_busts(player, dealer, player_chips)
                playing = False
            elif dealer.value > player.value:
                show_all(player, dealer)
                dealer_wins(player, dealer, player_chips)
                playing = False
            elif player.value > dealer.value:
                show_all(player, dealer)
                player_wins(player, dealer, player_chips)
                playing = False
            elif player.value == dealer.value:
                show_all(player, dealer)
                push(player, dealer)
                playing = False
    print("\nPlayer's winnings stand at", player_chips.balance)
    new_game = input("Do you want another try? enter yes or no")
    if new_game[0].lower() == 'y':
        playing = True
        player.remove_hand()
        dealer.remove_hand()
        continue
    else:
        print("Thanks for playing!")
    break
