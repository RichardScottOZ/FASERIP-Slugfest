# Data Files

This directory contains data files used by the FASERIP Slugfest simulator and character generator.

## Character Data

- **benriely.csv** - Large dataset of ~3000 characters parsed from Ben Riely's Marvel character website
- **creature.csv** - Character data in alternative format
- **AmazingMartialArtistI.csv** - Martial artist character examples
- **Martial-Arts-All.csv** - Complete martial arts character dataset
- **Mostly-Human-Martial-Arts-All.csv** - Human martial artist subset
- **Random_Characters.csv** - Generated random characters
- **Random_Characters2.csv** - Additional generated random characters

## Powers, Talents, and Equipment

- **PowersFix.csv** / **PowersFix.txt** - Standardized power mappings for character parsing
- **TalentsFix.csv** - Standardized talent mappings
- **EquipmentFix.csv** - Standardized equipment mappings
- **dfPower_List.csv** - Power reference list
- **dfTalent_List.csv** - Talent reference list
- **dfContact_List.csv** - Contact reference list
- **dfUPB.csv** - Ultimate Powers Book reference data

## Serialized Data

- **superheroapi.pkl** - Pickled data from superhero API

## Usage

These files are referenced by the simulator and character generator notebooks. To use custom character data, follow the format in `benriely.csv` or the beastiary files in the `DnD-battler/DnD_battler/` directory.
