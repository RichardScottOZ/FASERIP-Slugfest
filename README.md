# FASERIP Slugfest

A combat simulator and character generator for the FASERIP RPG system and other compatible superhero RPGs.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bluetyson/FASERIP-Slugfest/HEAD?urlpath=https%3A%2F%2Fgithub.com%2Fbluetyson%2FFASERIP-Slugfest%2Fblob%2Fmain%2Fnotebooks%2FFASERIP%2520Character%2520Generator.ipynb)

## Quick Start

```python
from DnD_battler import Creature, Encounter

# Load two characters and simulate a battle
cyclops = Creature.load("Cyclops")
corsair = Creature.load("Corsair")
arena = Encounter(cyclops, corsair)

# Run 100 battles and get statistics
print(arena.go_to_war(100))
```

## Installation

### From Source
```bash
git clone https://github.com/bluetyson/FASERIP-Slugfest.git
cd FASERIP-Slugfest/DnD-battler
pip install .
```

### For Development
```bash
pip install -e .
```

### For Notebooks
```bash
pip install -r requirements.txt
```

## Features

- **Combat Simulator**: Simulate battles between FASERIP characters with detailed combat mechanics
- **Character Generator**: Create random characters using Ultimate Powers Book rules
- **Character Database**: Access 3000+ pre-made characters from Ben Riely's Marvel database
- **Statistical Analysis**: Run thousands of battles to determine win probabilities
- **Jupyter Notebooks**: Interactive character generation and analysis tools

## Repository Structure

```
FASERIP-Slugfest/
├── DnD-battler/          # Core simulator package
│   ├── DnD_battler/      # Python package
│   └── setup.py          # Package installer
├── examples/             # Example scripts and battles
├── notebooks/            # Jupyter notebooks for character generation
├── data/                 # Character data, powers, talents, equipment
├── olddata/              # Reference data for character generation
└── Slugfest/             # Additional utilities
```

## Usage Examples

### Simple Battle
```bash
cd examples
python simple_battle.py
```

### Character-Specific Battles
```bash
python runtestFASERIP-Cyclops.py
python runtestFASERIP-Wolverine.py
```

See the [examples/](examples/) directory for more examples including:
- One vs many battles
- Martial artist contests
- Team battles
- Custom character creation

### Online (No Installation Required)
Use Binder to run the character generator and simulator in your browser - no installation needed!

## Technical Details

For detailed technical documentation, see [DnD-battler/README.md](DnD-battler/README.md).

## Discussion & Blog

Project updates and discussions: http://cosmicheroes.space/blog/index.php/tag/faserip-slugfest/

## Character Generator
## Character Generator

The character generator creates random FASERIP characters using Ultimate Powers Book rules.

### Using Notebooks

- **notebooks/FASERIP Character Generator.ipynb** - Main character generator
  - Creates characters in JSON and CSV formats
  - Compatible with the simulator's beastiary format
  - Outputs saved to data/ directory

- **notebooks/FASERIP-Training-Data.ipynb** - Parses Ben Riely's character database
- **notebooks/FASERIP-Martial_Artists.ipynb** - Martial artist analysis

### Character Generator Notes

- Composite and Compound Forms are replaced with Mutants for simplicity
- Metamorphic robot extra forms not currently implemented
- Character data standardized through mapping files (PowersFix.csv, TalentsFix.csv, EquipmentFix.csv)

## Combat Mechanics

### Implemented Powers

The simulator currently supports:
- Body Armour
- Claws (mapped to generic Edged attacks)
- Energy Absorption
- Energy Blast
- Extra Attacks
- Force Blast
- Force Field
- Hyper-Speed (defensive bonus and multiple attacks)
- Phasing
- Power Absorption (as takedown)
- Probability Manipulation
- Regeneration
- Resistances (framework in place)

### Implemented Equipment

Equipment is standardized to generic attack types:
- Blaster Pistols → Shooting
- Boomerangs → Throwing
- Bows → Shooting
- Guns → Shooting
- Swords → Edged

### Combat Notes

- Bullseyes are treated as Stuns for faster combat
- Multi-opponent battles use -4 CS penalty
- See technical documentation for detailed combat mechanics

## Related Projects

### Other FASERIP Tools
- **Java**: [FASERIP Character Generator GUI](http://sourceforge.net/projects/javamcc/files/JMCC%28betav4.5%29.jar/download)
- **JavaScript**: [Jin's FASERIP Char Creator](https://github.com/jinniaflyer450/Jins-FASERIP-Char-Creator)

### Resources
- [FASERIP RPG](https://gurbintrollgames.wordpress.com/faserip/)
- [4CS (Four-Color System)](https://www.drivethrurpg.com/product/50837/Four-Color-System-Core-Rules)
- [Classic Marvel Forever](https://classicmarvelforever.com/)
- [DnD Battler](https://github.com/matteoferla/DnD-battler) (Original inspiration)
- [Ben Riely Marvel Database](https://www.angelfire.com/comics/benriely/index.html)
- [Unofficial Canon Project](https://drive.google.com/drive/folders/1B4FIJ1gUksHQFLqrNYZ439JSkpm8uH4U)
- [FASERIPing Blog](http://cosmicheroes.space/blog/index.php/tag/faserip/)

## Contributing

Contributions are welcome! Whether you want to:
- Add new characters to the beastiary
- Implement additional powers or equipment
- Fix bugs or improve documentation
- Share battle results and statistics

Please feel free to open issues or submit pull requests.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

- Based on [DnD-battler](https://github.com/matteoferla/DnD-battler) by Matteo Ferla
- Character data from [Ben Riely's Marvel Database](https://www.angelfire.com/comics/benriely/index.html)
- FASERIP system by TSR/Marvel Super Heroes RPG