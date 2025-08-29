#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hangman — full terminal version (RU interface, EN word list).
"""

import random
import string
from dataclasses import dataclass

HANGMANPICS = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========""",
]

WORDS = [
    "family","friend","school","teacher","student","health","doctor","nurse","hospital","travel",
    "ticket","airport","bus","train","station","market","shop","money","wallet","credit",
    "phone","number","message","screen","window","street","house","apartment","kitchen","bedroom",
    "bathroom","garden","water","bottle","coffee","tea","sugar","bread","butter","cheese",
    "egg","chicken","beef","fish","rice","pasta","salad","fruit","banana","apple",
    "orange","grape","lemon","milk","yogurt","cereal","cookie","chocolate","honey","pepper",
    "salt","spice","knife","fork","spoon","plate","glass","cup","table","chair",
    "sofa","carpet","lamp","mirror","clock","watch","calendar","morning","evening","night",
    "summer","winter","spring","autumn","weather","rain","snow","cloud","wind","sunny",
    "music","guitar","piano","movie","theater","camera","photo","video","internet","email",
    "password","account","login","profile","schoolbag","notebook","pencil","pen","eraser","ruler",
    "homework","project","lesson","library","book","story","chapter","paper","printer","office",
    "manager","worker","meeting","report","salary","career","holiday","weekend","party","gift",
    "birthday","wedding","familycar","bicycle","motorbike","driver","license","fuel","battery","charger",
    "energy","electric","gardeners","flower","plant","tree","forest","mountain","river","beach",
    "island","village","city","country","border","passport","visa","hotel","hostel","reservation",
    "clean","dirty","happy","sad","angry","tired","hungry","thirsty","strong","weak"
]

MAX_WRONG = len(HANGMANPICS) - 1

@dataclass
class Stats:
    games: int = 0
    wins: int = 0
    losses: int = 0

def pick_word() -> str:
    return random.choice(WORDS)

def masked_word(secret: str, guessed: set[str]) -> str:
    return " ".join([c if c in guessed else "_" for c in secret])

def print_state(secret: str, guessed: set[str], wrong: int, used_letters: set[str]):
    print(HANGMANPICS[wrong])
    print(f"\nСлово:   {masked_word(secret, guessed)}")
    print(f"Ошибок:  {wrong}/{MAX_WRONG}")
    if used_letters:
        sorted_used = " ".join(sorted(used_letters))
        print(f"Буквы:   {sorted_used}")
    print()

def ask_guess(used_letters: set[str]) -> str:
    while True:
        raw = input("Ваша попытка (буква или всё слово): ").strip().lower()
        if not raw:
            print("Пустой ввод. Попробуйте снова.")
            continue
        if not all(ch in string.ascii_lowercase for ch in raw):
            print("Пожалуйста, используйте только английские буквы (a-z).")
            continue
        if len(raw) == 1 and raw in used_letters:
            print("Эта буква уже была. Другая попытка.")
            continue
        return raw

def play_round(stats: Stats):
    secret = pick_word()
    guessed_letters: set[str] = set()
    used_letters: set[str] = set()
    wrong = 0

    print("\nНовая игра! Я загадал английское слово.")
    print(f"Подсказка: длина слова — {len(secret)}.")

    while True:
        print_state(secret, guessed_letters, wrong, used_letters)

        if all(c in guessed_letters for c in secret):
            print(f"Поздравляю! Вы отгадали слово: {secret.upper()}")
            stats.wins += 1
            stats.games += 1
            break

        if wrong >= MAX_WRONG:
            print(HANGMANPICS[wrong])
            print(f"Проиграли. Слово было: {secret.upper()}")
            stats.losses += 1
            stats.games += 1
            break

        guess = ask_guess(used_letters)
        if len(guess) == 1:
            used_letters.add(guess)
            if guess in secret:
                guessed_letters.add(guess)
                print(f"Верно! Буква '{guess}' есть в слове.")
            else:
                wrong += 1
                print(f"Нет такой буквы. Ошибка {wrong}/{MAX_WRONG}.")
        else:
            if guess == secret:
                guessed_letters.update(set(secret))
                print(f"Точно! Слово — {secret.upper()}")
            else:
                wrong += 1
                print(f"Неверное слово. Ошибка {wrong}/{MAX_WRONG}.")

def main():
    print("=== HANGMAN (Виселица) — полная версия ===")
    stats = Stats()

    while True:
        play_round(stats)
        print(f"\nСтатистика: партий — {stats.games}, побед — {stats.wins}, поражений — {stats.losses}")
        again = input("\nСыграть ещё? (y/n): ").strip().lower()
        if again != "y":
            print("\nСпасибо за игру! До встречи.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВыход по Ctrl+C. Пока!")
