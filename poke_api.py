import requests

poke_api_URL = 'https://pokeapi.co/'


def main():  
    pokemon = get_pokemon("cinderace")
    print(pokemon) 
    
        
def get_pokemon(search_term):

    poke_Search_URL = f'https://pokeapi.co/api/v2/pokemon/{search_term}'


    header_params = {
        'Accept': 'application/json',
        'entity': 'pokemon',
    }

    print(f'Grabbing info about {search_term}...',  end=' ')
    resp_msg = requests.get(poke_Search_URL, headers=header_params)
    

    if resp_msg.ok:
        print('Success!!')
        body_dict = resp_msg.json()
        poke_list = [ability['ability']['name']for ability in body_dict['abilities']]
        return poke_list

    else:
        print('Failure')
        print(f'{resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error: {resp_msg.text}')
    return None



if __name__ == '__main__':
    main()