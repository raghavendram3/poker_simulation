# Blackjack Basic Strategy Simulator

A Python-based blackjack simulation that implements basic strategy and tracks financial performance over multiple games. This tool helps analyze the statistical outcomes of playing blackjack using mathematically optimal decisions.

## Features

- **Basic Strategy Implementation**: Follows optimal blackjack basic strategy for hit/stand/double/split decisions
- **Complete Game Logic**: Handles blackjack detection, dealer rules, and all standard game mechanics
- **Financial Tracking**: Monitors total investment vs. net returns over multiple games
- **Data Visualization**: Generates plots showing investment and return trends
- **Realistic Payouts**: Implements standard casino payouts (1:1 for wins, 3:2 for blackjack)

## Requirements

```
python >= 3.6
matplotlib
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/blackjack-simulator.git
cd blackjack-simulator
```

2. Install required dependencies:
```bash
pip install matplotlib
```

## Usage

### Basic Simulation

Run the simulation with default parameters (300 games, €1 bet per game):

```bash
python blackjack_simulator.py
```

### Customizing the Simulation

Modify these parameters in the script:

```python
num_games = 300      # Number of games to simulate
bet_per_game = 1     # Bet amount per game in euros
```

## How It Works

### Basic Strategy Rules

The simulator implements optimal basic strategy decisions:

- **Hard Totals**: Hit/stand based on player total vs dealer upcard
- **Doubling**: Double on 10-11, and 9 vs dealer 3-6
- **Splitting**: Split Aces and 8s always, split pairs 2,3,6,7 vs dealer 2-6
- **Soft Totals**: Handles Ace-counting automatically

### Game Flow

1. Deal initial two cards to player and dealer
2. Check for natural blackjacks
3. Apply basic strategy decisions (hit/stand/double/split)
4. Complete dealer hand (hit on soft 17)
5. Determine winner and calculate payout

### Financial Tracking

- **Investment**: Cumulative amount bet across all games
- **Net Return**: Total winnings minus total losses
- **Break-even Analysis**: Visual indication of profitability

## Output

The simulation generates a graph showing:

- Blue line: Total investment over time
- Green line: Net return over time  
- Red dashed line: Break-even point (€0)

## Key Functions

### `play_blackjack()`
Simulates a single complete blackjack game using basic strategy.

**Returns:**
- `'win'`: Player wins (1:1 payout)
- `'lose'`: Player loses
- `'blackjack'`: Player blackjack (3:2 payout)
- `'draw'`: Push/tie

### `basic_strategy(player_hand, dealer_card, allow_double=True)`
Determines the optimal play based on basic strategy.

**Parameters:**
- `player_hand`: List of player's cards
- `dealer_card`: Dealer's upcard
- `allow_double`: Whether doubling is allowed

**Returns:** `'hit'`, `'stand'`, `'double'`, or `'split'`

### `simulate_blackjack_with_tracking(num_games, bet_per_game=1)`
Runs multiple games and tracks financial performance.

**Returns:** Tuple of (investments_list, returns_list)

## Statistical Expectations

When using perfect basic strategy:
- House edge: ~0.5% (varies by specific rules)
- Expected long-term result: Slight losses due to house edge
- Short-term variance: Significant fluctuations possible

## Customization Options

### Modifying Rules
You can adjust the simulation by modifying:

- Card values in `card_values` dictionary
- Basic strategy logic in `basic_strategy()` function
- Payout ratios in `simulate_blackjack_with_tracking()`

### Different Betting Strategies
Currently implements flat betting, but can be extended for:
- Progressive betting systems
- Card counting simulations
- Bankroll management strategies

## Example Results

A typical 300-game simulation might show:
- Total investment: €300
- Net return: €285-315 (due to house edge and variance)
- Win rate: ~45-48%
- Blackjack rate: ~4.8%

## Limitations

- Uses infinite deck assumption (no card counting effects)
- Simplified split handling (doesn't track individual split hand results)
- Fixed dealer rules (hits soft 17)
- No surrender option implemented

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request
