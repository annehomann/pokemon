#!/usr/bin/env python3

# Jaden's solution
# https://github.com/jadencamelot/pokemon/tree/solution

from client import Client

def main():
    exit_flag = False
    c = Client()

    while exit_flag == False:
        command = input("Enter command: ")
        if command == "hello":
            print("hello")
        elif command == "all":
            print(c.pokemon)
        elif command == "exit":
            exit_flag = True
        elif command == "pokemon":
            n_pokemon = len(c.pokemon)
            print(f"There are {n_pokemon} pokemon")
        elif command == "list":
            for i in c.pokemon:
                print(i['name'].title())
        elif command == "search":
            entry = input("Write the name of the pokemon you would like to know about: ")
            for p in c.pokemon:
                if p['name'] == entry:
                    print(p['name'].title())
                    print(p['height'])

            



if __name__ == "__main__":
    main()

# User can search for a pokemon via command interface
# Commands:
# "list" - list names of all pokemon
# "search <pokemon> - search for a pokemon and display info about it"

# Client class fetch data for a given pokemon and return it

