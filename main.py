# Karam
import os
import json
import requests

def print_gui():
    print("──────────────────────────────\n",
          "\tArtist Database\n",
          "─────────────────────────────\n",
          "L │ List artists\n",
          "V │ View artist profile\n",
          "E │ Exit application\n",
          "─────────────────────────────")

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

FLAG_EXIT = False

base_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

base_request = requests.get(base_url)
base_data = json.loads(base_request.text)

artists = base_data["artists"]

#Sinan
while not FLAG_EXIT:
    clear()
    print_gui()

    user_input = input("Selection > ").casefold()
    if user_input == 'l':
        print("─────────────────────────────")
        for artist in artists:
            print(artist["name"])

    elif user_input == 'v':
        artist_name = input("Artist name > ")

        base_request = requests.get(base_url)
        base_data    = json.loads(base_request.text)
        artists      = base_data["artists"]

        for artist in artists:
            if artist["name"] == artist_name:
                artist_id = artist["id"]

                # Kalle
                artist_url      = base_url + artist_id
                artist_request  = requests.get(artist_url)
                artist_data     = json.loads(artist_request.text)

                artist_name     = artist_data["artist"]["name"]
                artist_members  = ', '.join(artist_data["artist"]["members"])
                artist_genres   = ', '.join(artist_data["artist"]["genres"])
                artist_years    = artist_data["artist"]["years_active"]

                print("─────────────────────────────")
                print("Artist name: \t", artist_name)
                print("Members:     \t", artist_members)
                print("Genres:      \t", artist_genres)
                print("Years active:\t", *artist_years)

        # Jasmin
        if artist_name not in (artist["name"] for artist in artists):
            print("Artist not found.")

    elif user_input == 'e':
        FLAG_EXIT = True

    else:
        print(f"Invalid operation '{user_input}'")

    print("─────────────────────────────")
    input("Press enter to continue")
