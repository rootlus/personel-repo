# Importing Modules

import time
from datetime import datetime
import random
import sys
import os

def clear_terminal(): # Checks what system it is, and clears terminal that way.
    if sys.platform == "win32": os.system("cls") # If system is Windows, runs "cls" command.
    elif sys.platform == "linux": os.system("clear") #If system is Linux, runs the "clear" command.


clear_terminal()

while True:
    print("[?] Enter a pin. Minimum 4 length.")
    input_pin = input(">>> ")
        
    if not input_pin.isdigit(): # Checks if input pin is not digit.
        # If it is, it clears terminal and goes back to loop start.
        clear_terminal()
        continue

    if len(input_pin) < 4: # Checks if input pin is less then 4 char?
        clear_terminal()
        continue

    break # Breaks the loop.


def bruteForce_pin():

    clear_terminal()


    value_pinTried = 0
    value_TotalPinTried = 0
    value_takedRobotTest = 0

    value_chars = "qwertyuopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

    pin_len = len(input_pin) # Takes length of input pin.

    date_now = datetime.now() # Take's datetime.
    start_time = time.time() # Take's time.

    while True:
        test_pin = ""

        for i in range(int(pin_len)): # Makes pin length how length input pin is.
            test_pin += str(random.randint(0,9))
            
        
        if value_pinTried == 100000:
        # If tried pin value is 100000 makes a robot test.
            value_takedRobotTest += 1
            while True:
                value_robotCode = ""
                for a in range(6):
                    value_robotCode += random.choice(value_chars)
                
                clear_terminal()

                print("[!] Robot Test, Enter Code:")
                print(value_robotCode,"\n")
                input_code = input(">>> ")

                if input_code == value_robotCode:
                    value_pinTried = 0
                    clear_terminal()
                    break
                else:
                    clear_terminal()
                    continue


        # Prints terminal to which pin is trying and how much attempt gone. And removes line with \r
        print(f"[*] Trying Pin: {test_pin} - Attempt: {value_TotalPinTried}",end="\r")
        
        if test_pin == input_pin: # Checks if tested pin..
        # If its true, clears terminal and shows the results and ends the script.
            clear_terminal()

            elapsed_time = time.time() - start_time

            print("\n")
            print(f"Pin Found: {test_pin}")
            print(f"\nTaked Time: {elapsed_time}")
            print(f"Total Attempts: {value_TotalPinTried}")
            print(f"Total Robot Test: {value_takedRobotTest}\n")
            break
        else:
        #If its not, adds adds 1 to values.
            value_pinTried += 1

            value_TotalPinTried += 1

bruteForce_pin()
