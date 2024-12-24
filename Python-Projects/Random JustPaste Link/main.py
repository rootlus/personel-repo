import random
import time
import os
import sys

def module_check_install(mobule_name):
    try:
        import module_name
    except ImportError:
        os.system(f"pip install {mobule_name}")

module_check_install("requests")
module_check_install("beautifulsoup4")

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Import Error, try to run again.")

def clear_terminal():
    if sys.platform=="win32": os.system("cls")
    elif sys.platform=="linux": os.system("clear")

clear_terminal()

chars = "qwertyuopasdfghjklzxcvbnm1234567890"

while True:
    try:
        input_wait_Time = int(input("Time after to many requests error(second): "))
        break
    except:
        clear_terminal()
        continue

clear_terminal()

while True:
    input_want_title = input("Print titles?(Y/n): ")
    if input_want_title == "Y" or input_want_title == "y" or input_want_title == "N" or input_want_title == "n":
        break
    else:
        clear_terminal()
        continue

while True:
    try:
        input_req_timeout = int(input("Time after every requests(second): "))
        break
    except:
        clear_terminal()
        continue

clear_terminal()

while True:
    try:
        random_data = ""

        for i in range(5):
            random_data += random.choice(chars)

        url = f"https://justpaste.it/{random_data}"
        
        rsp = requests.get(url)
        rsp_code = rsp.status_code


        if "Too many requests. Please try again later" in rsp.text:
            time_wait = input_wait_Time
            while True:
                print(f"To many requests. waiting {time_wait} seconds...",end="\r")
                time.sleep(1)
                time_wait-=1
                if time_wait == 0:
                    break


        soup = BeautifulSoup(rsp.text, "html.parser")
        title_tag = soup.find_all(class_="articleFirstTitle")
        
        for title in title_tag:
            if rsp_code == 200 or rsp_code == 202:
                print("")
                print(url)
                if input_want_title == "Y" or input_want_title == "y":
                    print(title.get_text())
        time.sleep(input_req_timeout)
    except KeyboardInterrupt:
        exit()
