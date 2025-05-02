import random
import matplotlib.pyplot as plt

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, suit, rank):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._deck = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0)

class PokerHand:
    def __init__(self, deck):
        self._cards = [deck.deal() for _ in range(5)]

    @property
    def cards(self):
        return self._cards

    @property
    def number_matches(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i != j and self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_full_house(self):
        return self.number_matches == 8  # Only true for full house

# Simulation configuration
iterations = 50000  # <-- CHANGE THIS MANUALLY if needed (from 1000 to 50000)
draws = []
probs = []

full_house_count = 0

for i in range(1, iterations + 1):
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)

    if hand.is_full_house:
        full_house_count += 1

    if i % 100 == 0:
        probability = 100 * full_house_count / i
        draws.append(i)
        probs.append(probability)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(draws, probs)
plt.xlabel("Number of Draws")
plt.ylabel("Probability of Full House (%)")
plt.title("Simulated Probability of Drawing a Full House Over Time")
plt.grid(True)
plt.show()

# Final result
print(f"Final Probability after {iterations} draws: {100 * full_house_count / iterations:.4f}%")
