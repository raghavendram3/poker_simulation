import random
import matplotlib.pyplot as plt

# Card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
               '7': 7, '8': 8, '9': 9, '10': 10, 
               'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def create_deck():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def calculate_hand(hand):
    value = sum(card_values[card] for card in hand)
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand(hand) == 21

def basic_strategy(player_hand, dealer_card, allow_double=True):
    player_total = calculate_hand(player_hand)
    dealer_value = card_values[dealer_card]

    if allow_double and len(player_hand) == 2:
        if player_total == 10 or player_total == 11:
            return 'double'
        if player_total == 9 and dealer_value in range(3, 7):
            return 'double'
    if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
        if player_hand[0] in ['A', '8']:
            return 'split'
        if player_hand[0] in ['2', '3', '6', '7'] and dealer_value in range(2, 7):
            return 'split'
        if player_hand[0] in ['4', '5', '10']:
            return 'stand'
    if player_total >= 17:
        return 'stand'
    elif 13 <= player_total <= 16:
        return 'stand' if 2 <= dealer_value <= 6 else 'hit'
    elif player_total == 12:
        return 'stand' if 4 <= dealer_value <= 6 else 'hit'
    else:
        return 'hit'

def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    if is_blackjack(player_hand):
        return 'blackjack'
    elif is_blackjack(dealer_hand):
        return 'lose'

    decision = basic_strategy(player_hand, dealer_hand[0])
    if decision == 'double':
        player_hand.append(deck.pop())
        if calculate_hand(player_hand) > 21:
            return 'lose'
    elif decision == 'split':
        split_hand1 = [player_hand[0], deck.pop()]
        split_hand2 = [player_hand[1], deck.pop()]
        result1 = play_individual_hand(split_hand1, dealer_hand[0], deck)
        result2 = play_individual_hand(split_hand2, dealer_hand[0], deck)
        return result1 if result1 == result2 else 'mixed'
    else:
        while decision == 'hit':
            player_hand.append(deck.pop())
            if calculate_hand(player_hand) > 21:
                return 'lose'
            decision = basic_strategy(player_hand, dealer_hand[0])

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if dealer_total > 21 or player_total > dealer_total:
        return 'win'
    elif player_total < dealer_total:
        return 'lose'
    else:
        return 'draw'

def play_individual_hand(player_hand, dealer_card, deck):
    while basic_strategy(player_hand, dealer_card) == 'hit':
        player_hand.append(deck.pop())
        if calculate_hand(player_hand) > 21:
            return 'lose'
    return 'stand'

# Simulate and track investments and returns
def simulate_blackjack_with_tracking(num_games, bet_per_game=1):
    net_return = 0
    total_investment = 0
    investments = []
    returns = []

    for _ in range(num_games):
        result = play_blackjack()
        total_investment += bet_per_game  # Add the bet for this game
        if result == 'win':
            net_return += bet_per_game * 2  # 2:1 payout for regular win
        elif result == 'blackjack':
            net_return += bet_per_game * 2.5  # 3:2 payout for blackjack
        elif result == 'lose':
            net_return -= bet_per_game  # Lose the bet amount

        investments.append(total_investment)
        returns.append(net_return)

    return investments, returns

# Parameters for simulation
num_games = 300
bet_per_game = 1

# Run simulation and plot results
investments, returns = simulate_blackjack_with_tracking(num_games, bet_per_game)

plt.figure(figsize=(12, 6))
plt.plot(range(1, num_games + 1), investments, label="Total Investment (€)", color="blue", alpha=0.7)
plt.plot(range(1, num_games + 1), returns, label="Net Return (€)", color="green", alpha=0.7)
plt.axhline(0, color="red", linestyle="--", linewidth=1, label="Break-Even Line")
plt.title(f"Blackjack Simulation: Total Investment vs Net Return ({num_games} Games)")
plt.xlabel("Game Number")
plt.ylabel("Euros (€)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
