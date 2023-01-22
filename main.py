import os
import random
from ascii import logo, game_over
from os import system, name


def higher_lower():
    game_not_end = True
    while game_not_end:
        def new_game():
            print(logo)
            input("\nPress Enter to start...")
            instagram_followers = [
                ["Danielle Collins", 172000],
                ["FC Bayern", 36300000],
                ["Robert Lewandowski", 32400000],
                ["Iga Swiatek", 1000000],
                ["Donald Tusk", 290000],
                ["Barack Obama", 35700000],
                ["Britney Spears", 41600000],
                ["Cristiano Ronaldo", 538000000],
                ["Leo Messi", 423000000],
                ["Killian Mbappe", 95700000],
                ["Olaf Scholz", 1900000],
                ["Sting", 1300000],
                ["Pele", 16000000],
                ["Mr. Beast", 22700000],
                ["Mr. Bean", 8800000],
                ["Ariana Grande", 352000000],
                ["Rihanna", 139000000],
                ["Michael Jackson", 7500000],
                ["Bruno Mars", 27000000],
                ["Michael Schumacher", 1200000]
            ]
            # Shuffle list to get a different order of elements at every execution
            random.shuffle(instagram_followers)

            score_game = 0
            for celebrity in range(0, len(instagram_followers) - 1):
                os.system('cls')
                print(f"Compare A: {instagram_followers[celebrity][0]}\nAgainst\nB: {instagram_followers[celebrity+1][0]}\n")
                answer = input("Answer: ").lower()
                correct_answer = ""
                if instagram_followers[celebrity][1] > instagram_followers[celebrity+1][1]:
                    correct_answer = "a"
                else:
                    correct_answer = "b"
                if answer == correct_answer:
                    score_game += 1
                    print("That's correct!\n")
                else:
                    print("\nThat's not correct!")
                    return score_game
            return score_game

        score = new_game()
        print(f"Your Score: {score}")
        print(f"{game_over}\n")
        if input("Do you want to play again? Y/N: ").lower() == "n":
            game_not_end = False
        else:
            os.system('cls')


higher_lower()

