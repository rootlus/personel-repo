import random
import json
import sys
import os
import datetime

c_chars = "qwertyuopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
c_numbers = "0123456789"
c_sp_chars = "!^+%&/()=?-_,."

def clear_terminal():
    if sys.platform == "win32": os.system("cls")
    elif sys.platform == "linux": os.system("clear")

def menu():
    clear_terminal()
    print("""                               

1-) Start
2-) Settings
3-) Exit
""")

    while True:
        u_choice = input(">>> ")
    
        match u_choice:
            case "1":
                passgen()
                break
            case "2":
                settings()
                break
            case "3":
                exit()
            case _:
                pass



def settings():
    try:
        clear_terminal()
        global wants_c_numbers, wants_c_sp_chars
        
        while True:
            clear_terminal()
            with open("data/settings.json", "r") as f:
                settings_json = json.load(f)

                wants_c_numbers = settings_json.get("wants_c_numbers")
                wants_c_sp_chars = settings_json.get("wants_c_sp_chars")
                
                print(f"""

            Numbers: {wants_c_numbers}
            Special Chars: {wants_c_sp_chars}

            1-) Change Numbers Settings
            2-) Change Special Chars Settings
            3-) Exit
            """)
                
                u_choice = input(">>> ")

                with open("data/settings.json","r+") as f:
                    settings_json = json.load(f)
                    match u_choice:
                        case "1":
                            settings_json["wants_c_numbers"] = "Yes" if settings_json["wants_c_numbers"] == "No" else "No"
                        case "2":
                            settings_json["wants_c_sp_chars"] = "Yes" if settings_json["wants_c_sp_chars"] == "No" else "No"
                        case "3":
                            menu()
                            break
                        case _:
                            print("Wrong Choice")
                            continue

                    f.seek(0)
                    json.dump(settings_json, f, indent=4)
                    f.truncate()
    except KeyboardInterrupt:
        exit()

            

def passgen():
    try:
        global wants_c_numbers, wants_c_sp_chars
        password = ""

        while True:
            u_pass_lenght = input("Password Lenght: ")

            if u_pass_lenght == "":
                clear_terminal()
                print("Lenght can't be empty!")
            
            with open("data/settings.json", "r") as f:

                settings_json = json.load(f)

                wants_c_numbers = settings_json.get("wants_c_numbers")
                wants_c_sp_chars = settings_json.get("wants_c_sp_chars")

                all_chars = c_chars
                if wants_c_numbers == "Yes":
                    all_chars += c_numbers
                if wants_c_sp_chars == "Yes":
                    all_chars += c_sp_chars

                for i in range(int(u_pass_lenght)):
                    password += random.choice(all_chars)

                print(f"Password Generated: {password}")
                input()
                menu()
    except KeyboardInterrupt:
        exit()
                


menu()

    