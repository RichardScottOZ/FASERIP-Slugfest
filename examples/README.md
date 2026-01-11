# Examples

This directory contains example scripts demonstrating how to use the FASERIP Slugfest simulator.

## Quick Start Example

**simple_battle.py** - The simplest way to get started:
```bash
cd examples
python simple_battle.py
```

This script demonstrates:
- Loading characters from the beastiary
- Creating an encounter
- Running a single battle
- Running multiple battles for statistics

## Character-Specific Examples

These scripts demonstrate battles between specific Marvel characters:

- **runtestFASERIP-Cyclops.py** - Cyclops vs Corsair
- **runtestFASERIP-Wolverine.py** - Wolverine battles
- **runtestFASERIP-Storm.py** - Storm battles
- **runtestFASERIP-Rogue.py** - Rogue battles
- **runtestFASERIP-JeanGrey.py** - Jean Grey battles
- **runtestFASERIP-Beast.py** - Beast battles
- **runtestFASERIP-Bishop.py** - Bishop battles
- **runtestFASERIP-Nightcrawler.py** - Nightcrawler battles
- **runtestFASERIP-Shadowcat.py** - Shadowcat battles
- **runtestFASERIP-Hawkeye.py** - Hawkeye battles
- **runtestFASERIP-Domino.py** - Domino battles (includes probability manipulation)
- **runtestFASERIP-Hulk.py** - Hulk battles

## Martial Artist Examples

- **runtestFASERIP-MartialArtistI.py** - Amazing Martial Artist vs Boxer
- **runtestFASERIP-MostlyHumanMartialArtist.py** - Human martial artist examples

## Multi-Opponent Examples

- **runtestFASERIP-addmob.py** - Demonstrates one character fighting multiple opponents
- **runtestFASERIP-Rat.py** - Herbert the Lawyer vs Rat Pack

## Advanced Examples

- **runtestFASERIP.py** - Comprehensive test with multiple combat scenarios
- **runtestFASERIP-character.py** - Character creation and customization
- **test.py** - Various test scenarios
- **experiments.py** - Experimental features

## Usage Pattern

All examples follow a similar pattern:

```python
from DnD_battler import Creature, Encounter

# Load or create characters
hero = Creature.load("Character Name")
villain = Creature.load("Villain Name")

# Create encounter
battle = Encounter(hero, villain)

# Run simulation
print(battle.go_to_war(1000))  # Run 1000 battles
```

## Customizing Examples

You can modify these examples to:
- Test different character matchups
- Adjust the number of simulation runs
- Create custom characters
- Test team battles

See the main README.md for more information on character creation and simulation options.
