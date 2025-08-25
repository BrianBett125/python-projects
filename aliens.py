#!/usr/bin/env python3
"""
Alien Encounter Simulator
- Generate procedurally different alien species
- Choose actions (greet, trade, ally, study, fight)
- Outcomes depend on alien temperament and your ship's stats
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple
import random
import sys
import textwrap

random.seed()  # use system randomness

SPECIES_SYLLABLES = [
    "xa","lo","ri","mu","zen","qar","ith","ul","ta","vor","shi","dra","ke","no","ph",
    "ae","ruk","bel","on","ty","gar","eon","vak","zir","qua","umi","sol"
]

DISPOSITIONS = ["curious", "wary", "proud", "hostile", "honorable", "playful", "stoic"]
TECH_LEVELS = ["stone", "industrial", "atomic", "digital", "fusion", "quantum"]
ETHOS = ["collective", "individualist", "mercantile", "ascetic", "warlike", "diplomatic", "scholarly"]

def make_name(syllables=SPECIES_SYLLABLES) -> str:
    parts = random.randint(2, 4)
    name = "".join(random.choice(syllables) for _ in range(parts))
    # sprinkle an apostrophe sometimes
    if random.random() < 0.25:
        idx = random.randint(1, len(name)-2)
        name = name[:idx] + "'" + name[idx:]
    return name.capitalize()

@dataclass
class AlienSpecies:
    name: str
    disposition: str
    tech_level: str
    ethos: str
    patience: int  # how many missteps before they sour
    trust: float   # -1.0 .. 1.0 baseline attitude toward you
    wealth: int    # for trading
    martial: int   # 0..100 how strong they are in combat

    @staticmethod
    def generate() -> "AlienSpecies":
        return AlienSpecies(
            name=make_name(),
            disposition=random.choice(DISPOSITIONS),
            tech_level=random.choice(TECH_LEVELS),
            ethos=random.choice(ETHOS),
            patience=random.randint(1, 4),
            trust=round(random.uniform(-0.3, 0.5), 2),
            wealth=random.randint(20, 120),
            martial=random.randint(10, 95),
        )

@dataclass
class Ship:
    name: str = "ISS Uhuru"
    hull: int = 100
    shields: int = 60
    science: int = 50
    cargo: int = 50
    credits: int = 100

    def damage(self, amount: int) -> None:
        absorbed = min(self.shields, amount)
        self.shields -= absorbed
        leftover = amount - absorbed
        if leftover > 0:
            self.hull = max(0, self.hull - leftover)

    def repair(self, amount: int) -> None:
        self.hull = min(100, self.hull + amount)

@dataclass
class EncounterResult:
    summary: str
    reputation_delta: float
    loot: int = 0
    lost: int = 0
    alliance: bool = False
    game_over: bool = False

ACTIONS = ["greet", "trade", "ally", "study", "fight", "leave"]

def describe_species(a: AlienSpecies) -> str:
    return (f"Species: {a.name}\n"
            f"- Disposition: {a.disposition}\n"
            f"- Ethos: {a.ethos}\n"
            f"- Tech: {a.tech_level}\n"
            f"- Wealth: {a.wealth}\n"
            f"- Martial: {a.martial}\n")

def greeting(ship: Ship, alien: AlienSpecies) -> EncounterResult:
    bump = {"curious": 0.25, "diplomatic": 0.2, "honorable": 0.15}.get(alien.ethos, 0.1)
    msg = f"You hail the {alien.name}. Their response is measured."
    if alien.disposition in ["curious", "playful"]:
        msg = f"You greet the {alien.name}. They respond with visible excitement."
        bump += 0.15
    if alien.disposition == "hostile":
        bump -= 0.2
    return EncounterResult(msg, bump)

def trade(ship: Ship, alien: AlienSpecies) -> EncounterResult:
    price = random.randint(15, 45)
    qty = random.randint(1, min(10, ship.cargo))
    willingness = alien.trust + (0.2 if alien.ethos == "mercantile" else 0) + (0.1 if alien.disposition in ["curious","honorable"] else 0)
    if willingness < -0.1 or alien.wealth < price * qty:
        return EncounterResult(f"The {alien.name} decline to trade.", -0.05)
    # execute trade
    cost = price * qty
    if ship.credits < cost:
        return EncounterResult("You lack the credits to close a deal.", -0.02)
    ship.credits -= cost
    alien.wealth -= cost
    ship.cargo += qty
    gain_rep = min(0.2, 0.05 + qty / 100)
    return EncounterResult(f"Trade successful: bought {qty} units for {cost} cr.", gain_rep, loot=0)

def ally(ship: Ship, alien: AlienSpecies) -> EncounterResult:
    threshold = 0.4
    chance = alien.trust + (0.2 if alien.ethos in ["diplomatic","honorable"] else 0) - (0.2 if alien.disposition == "wary" else 0)
    if chance >= threshold:
        return EncounterResult(f"The {alien.name} pledge mutual aid. Alliance formed!", +0.5, alliance=True)
    else:
        alien.patience -= 1
        msg = f"The {alien.name} hesitate to commit. (Their patience drops to {alien.patience})"
        hostile = alien.patience <= 0
        return EncounterResult(msg, -0.15 if hostile else -0.05, game_over=False)

def study(ship: Ship, alien: AlienSpecies) -> EncounterResult:
    difficulty = random.randint(20, 80)
    roll = ship.science + random.randint(-15, 20)
    if roll >= difficulty:
        ship.science = min(100, ship.science + 5)
        ship.credits += 10
        return EncounterResult("Your study yields insights (+5 science, +10 credits).", +0.1)
    else:
        alien.patience -= 1
        ship.damage(5)
        return EncounterResult("Your scans annoy them—minor warning shots fired (-5 shields).", -0.1)

def fight(ship: Ship, alien: AlienSpecies) -> EncounterResult:
    your_power = ship.shields + ship.hull + random.randint(0, 30)
    their_power = alien.martial + random.randint(0, 30)
    if your_power >= their_power:
        loot = random.randint(10, 60)
        ship.credits += loot
        return EncounterResult(f"You prevail in a skirmish and salvage {loot} credits.", -0.4, loot=loot)
    else:
        dmg = random.randint(20, 60)
        ship.damage(dmg)
        over = ship.hull == 0
        return EncounterResult(f"You are outgunned! Ship takes {dmg} damage.", -0.3, game_over=over)

def do_action(action: str, ship: Ship, alien: AlienSpecies) -> EncounterResult:
    action = action.lower().strip()
    if action == "greet":
        return greeting(ship, alien)
    if action == "trade":
        return trade(ship, alien)
    if action == "ally":
        return ally(ship, alien)
    if action == "study":
        return study(ship, alien)
    if action == "fight":
        return fight(ship, alien)
    if action == "leave":
        return EncounterResult("You break contact and jump to safer space.", 0.0)
    return EncounterResult("Unrecognized action. You hesitate…", -0.01)

def print_ship(ship: Ship) -> None:
    print(f"\nShip: {ship.name} | Hull {ship.hull} | Shields {ship.shields} | Science {ship.science} | Cargo {ship.cargo} | Credits {ship.credits}")

def wrap(s: str) -> str:
    return textwrap.fill(s, width=78)

def main() -> None:
    ship = Ship()
    reputation = 0.0
    encounters = 0
    alliances: List[str] = []

    print("=== Alien Encounter Simulator ===")
    print("Actions: greet | trade | ally | study | fight | leave")
    print("Tip: build trust with greetings/trade before proposing an alliance.\n")

    while ship.hull > 0:
        alien = AlienSpecies.generate()
        encounters += 1
        print("\n" + "=" * 78)
        print(f"Encounter #{encounters}: You drop out of FTL near an unknown vessel.")
        print(describe_species(alien))
        print_ship(ship)

        while True:
            action = input("\nChoose action (greet/trade/ally/study/fight/leave): ").strip().lower()
            result = do_action(action, ship, alien)
            reputation = max(-1.0, min(1.0, reputation + result.reputation_delta))
            print("\n" + wrap(result.summary))
            print(f"Reputation now: {reputation:+.2f}")
            print_ship(ship)

            if result.alliance:
                alliances.append(alien.name)
                break

            if action == "leave" or ship.hull == 0:
                break

            # Hostility trigger if patience exhausted or rep very low
            if alien.patience <= 0 or reputation <= -0.8:
                print(wrap(f"The {alien.name} turn hostile due to strained relations."))
                aftermath = fight(ship, alien)
                reputation = max(-1.0, min(1.0, reputation + aftermath.reputation_delta))
                print(wrap(aftermath.summary))
                print_ship(ship)
                break

        if ship.hull == 0:
            print("\nYour ship is destroyed. Game over.")
            break

        # small between-encounter repair
        ship.repair(5)
        ship.shields = min(80, ship.shields + 5)

        cont = input("\nContinue exploring space? (y/n): ").strip().lower()
        if cont != "y":
            break

    print("\n=== Mission Summary ===")
    print(f"Encounters: {encounters}")
    print(f"Alliances: {', '.join(alliances) if alliances else 'None'}")
    print(f"Final Reputation: {reputation:+.2f}")
    print_ship(ship)
    print("Thanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n\nExiting peacefully. Live long and prosper.")

