#!/usr/bin/env python3
"""
Simple FASERIP Slugfest Example
================================

This example shows the basic usage of the FASERIP Slugfest simulator.
It loads two characters and simulates battles between them.
"""

from DnD_battler import Creature, Encounter

def main():
    """Run a simple combat simulation between Cyclops and Corsair."""
    
    print("=" * 60)
    print("FASERIP SLUGFEST - Simple Example")
    print("=" * 60)
    print()
    
    # Load two characters from the beastiary
    print("Loading characters from beastiary...")
    cyclops = Creature.load("Cyclops")
    corsair = Creature.load("Corsair")
    
    print(f"  - {cyclops.name}")
    print(f"  - {corsair.name}")
    print()
    
    # Create an encounter
    print("Setting up encounter...")
    arena = Encounter(cyclops, corsair)
    print(f"  Arena: {arena}")
    print()
    
    # Run a single battle
    print("Running a single battle...")
    print("-" * 60)
    result = arena.battle()
    print(result)
    print("-" * 60)
    print()
    
    # Run multiple battles to get statistics
    print("Running 100 battles for statistics...")
    stats = arena.go_to_war(100)
    print(stats)
    print()
    
    print("=" * 60)
    print("Example complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
