import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import os

# Installing the modules
os.system("pip install bs4")
os.system("pip install requests")

while True:
    try:
        # Random profile
        response = requests.get("https://spacehey.com/random", allow_redirects=True)
        profile_url = response.url

        soup = BeautifulSoup(response.text, 'html.parser')
        time_tags = soup.find_all('time', class_='ago')

        # If there is no time tag skip it
        if not time_tags:
            print("⏱ Cannot found tag. Skipping...")
            continue

        # Selecting the most recent of the tags (taking the first one)
        found = False
        for tag in time_tags:
            timestamp_str = tag.text.strip()
            if timestamp_str.isdigit():
                timestamp = int(timestamp_str)
                now = int(time.time())
                if now - timestamp <= 86400:
                    print(f"✅ Profile found: {profile_url}")
                    webbrowser.open(profile_url)
                    input("Press Enter to continue...")
                    found = True
                    break

        if not found:
            print(f"❌ {profile_url} - Inactive for 24 hours.")

    except Exception as e:
        print("Error:", e)
        continue
