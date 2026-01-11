# Contributing to FASERIP Slugfest

Thank you for your interest in contributing to FASERIP Slugfest! This document provides guidelines and information for contributors.

## Ways to Contribute

### 1. Report Bugs
- Use the GitHub issue tracker
- Include details: what you expected vs. what happened
- Provide steps to reproduce the issue
- Include your Python version and OS

### 2. Add Characters
Characters are defined in CSV format in the beastiary files:
- Main beastiary: `DnD-battler/DnD_battler/beastiaryFASERIP.csv`
- Test characters: `data/benriely.csv`

Character attributes include:
- FASERIP stats (F, A, S, E, R, I, P)
- Health and Karma
- Powers, Equipment, Talents
- Attack and Defense profiles

### 3. Implement Powers and Equipment
Powers are located in:
- `DnD-battler/DnD_battler/creature/`

When implementing new powers:
1. Add power definitions to the Creature class
2. Update combat mechanics if needed
3. Add tests/examples demonstrating the power
4. Update PowersFix.csv for standardization

### 4. Improve Documentation
- Fix typos and clarify instructions
- Add more examples
- Improve code comments
- Update notebooks with better explanations

### 5. Code Contributions

#### Development Setup
```bash
git clone https://github.com/bluetyson/FASERIP-Slugfest.git
cd FASERIP-Slugfest/DnD-battler
pip install -e .
```

#### Code Style
- Python 3.6+ required
- Follow existing code conventions
- Add comments for complex logic
- Update docstrings for new functions

#### Testing
Run existing test files to ensure your changes don't break functionality:
```bash
cd examples
python runtestFASERIP.py
python simple_battle.py
```

### 6. Share Battle Results
Have interesting battle results or statistics? Share them!
- Open an issue with your findings
- Post on the blog: http://cosmicheroes.space/blog/

## Repository Structure

### Core Package (`DnD-battler/DnD_battler/`)
- `creature/` - Character/creature classes and mechanics
- `encounter/` - Combat encounter management
- `dice/` - Dice rolling and FASERIP table mechanics
- `beastiaryFASERIP.csv` - Main character database

### Supporting Directories
- `examples/` - Example scripts and battles
- `notebooks/` - Jupyter notebooks for character generation
- `data/` - Character data, powers, talents, equipment mappings
- `olddata/` - Reference data for character generation

## Character Data Format

The beastiary CSV uses these columns:
- `name`, `identity`, `alignment` - Basic info
- `f`, `a`, `s`, `e`, `r`, `i`, `p` - FASERIP stats (ranks like Ty, Gd, Ex, Rm, In, Am, Mn, Un)
- `h`, `k` - Health and Karma (calculated from stats)
- `powers`, `powers_rank`, `powers_adj`, `powers_adj_rank` - Powers and ranks
- `equipment`, `equipment_rank`, `equipment_adj`, `equipment_adj_rank` - Equipment
- `talents`, `talents_adj` - Talents and skills
- `martial_arts` - Martial arts types (A, B, C, D, E)
- `attack` - Attack type dictionary (Blunt, Edged, Force, Energy, etc.)
- `defense` - Defense capabilities
- `body_armour` - Armor ratings vs Physical/Energy
- `mook` - Flag for multi-opponent battles (0 or 1)

## Standardization Files

Located in `data/`:
- `PowersFix.csv` - Maps power names to standardized versions
- `TalentsFix.csv` - Maps talent names to standardized versions
- `EquipmentFix.csv` - Maps equipment to standardized versions

These help parse the 3000+ characters from Ben Riely's database.

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### PR Guidelines
- Describe what your PR does and why
- Reference any related issues
- Include examples if adding new features
- Keep changes focused and minimal

## Questions?

- Open an issue for questions about contributing
- Check existing issues and PRs first
- Visit the blog for discussion: http://cosmicheroes.space/blog/

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Credits

All contributors will be acknowledged. Thank you for helping make FASERIP Slugfest better!
