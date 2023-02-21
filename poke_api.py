import requests

pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"
#search_url = f'{pokeapi_url}/{pokemon}'

def main():
    pokesearch = get_pokemon("cinderace","abilities")

def get_pokemon(pokemon, search_term, page=1, limit=20):
    search_url = f'{pokeapi_url}/{pokemon}'
    poke = str(pokemon)
    poke.strip()
    poke.lower()

    param = {
        "entity": pokemon,
        "name": pokemon,
        "page": page,
        "limit": limit,
        "term": search_term
    }

    print("Getting info about the Pokemon...", end='')
    resp_msg = requests.post(search_url, data=param)

    if resp_msg.ok:
        print('Success!!')
        print(f'URL of new paste: {resp_msg.text}')
        return resp_msg.text
    elif resp_msg.status_code == 422:
        print("Error!")
        print("Maximum pastes reached for 24 hours.")
    else:
        print("Error")
        print(f"Response code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.content}")
        return None

    return

if __name__ == "__main__":
    main()
