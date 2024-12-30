import random
import os
import sys

def clear_terminal():
    if sys.platform=="linux": os.system("clear")
    elif sys.platform=="win32": os.system("cls")


def mode_easy():
    try:
        gameinfo_triedTime = 0

        while True:
            gameask_onetime = input("One Time?(Y/n): ")

            if gameask_onetime == "Y" or gameask_onetime == "y" or gameask_onetime == "n" or gameask_onetime == "N":
                break
            else:
                continue

        rnd_number = random.randint(0,10)
        clear_terminal()
        print("Ready.")

        while True:
            if gameask_onetime == "Y" or gameask_onetime == "y" and gameinfo_triedTime > 0:
                print("Failed...")
                input()
                game_menu()
            

            ply_guess = int(input("> "))

            if ply_guess == rnd_number:
                print("Succesfull!!")
                input()
                game_menu()
            else:
                gameinfo_triedTime += 1
    except Exception as e:
        with open("error.log","w+") as f:
            f.write(e)
        print("Something went wrong. Saved to error.log")
    except KeyboardInterrupt:
        exit()

def mode_custom():
    while True:
        gameinfo_triedTime = 0
        try:
            user_startNumber = input("Start number: ")
            user_endNumber = input("End number: ")

            x_startNumber = int(user_startNumber)
            x_endNumber = int(user_endNumber)

            rnd_number = random.randint(x_startNumber, x_endNumber)

            while True:
                gameask_onetime = input("One Time?(Y/n): ")

                if gameask_onetime == "Y" or gameask_onetime == "y" or gameask_onetime == "n" or gameask_onetime == "N":
                    break
                else:
                    continue
            
            clear_terminal()
            print("Ready.")

            while True:
                if gameask_onetime == "Y" or gameask_onetime == "y" and gameinfo_triedTime > 0:
                    print("Failed...")
                    input()
                    game_menu()
                

                ply_guess = int(input("> "))

                if ply_guess == rnd_number:
                    print("Succesfull!!")
                    input()
                    game_menu()
                else:
                    gameinfo_triedTime += 1

        except Exception as e:
            with open("error.log","w+") as f:
                f.write(e)
            print("Something went wrong. Saved to error.log")
        except KeyboardInterrupt:
            exit()




def game_menu():
    while True:
        clear_terminal()

        print("""
    - Select Difficulty - 

    1 - Start (0 - 10)
    2 - Custom Mode
    """)

        try:
            user_difficulty = input("> ")
        except KeyboardInterrupt:
            exit()

        if user_difficulty is None or user_difficulty == "":
            continue
        elif user_difficulty=="1":
            mode_easy()
        elif user_difficulty=="2":
            mode_custom()
        else:
            continue

game_menu()