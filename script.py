import requests
import sys
from poke_api import get_pokemon
from pastebin_api import post_new_paste

def main():
    search_term = get_search_term()
    thepokemon = get_pokemon(search_term, search_term)
    if thepokemon:
        title, body_text = get_paste_content(thepokemon, search_term)
        paste_url = post_new_paste(title, body_text)
        print(f"URL of new paste: {paste_url}")

def get_search_term():

    num_params = len(sys.argv) - 1
    if num_params > 0:
        search_term = sys.argv[1]
        return search_term
    else:
        print("Error: Missing search term")
        sys.exit(1)

def get_paste_content(pokemon, search_term):
    poke = pokemon.title()
    title = f"{poke}'s Abilities"
    
    divider = ','
    body_text = str(pokemon)
    for ability in pokemon:
        body_text += ability
        body_text += divider

    return title, body_text

if __name__ == "__main__":
    main()
