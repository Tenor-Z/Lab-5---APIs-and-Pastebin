#---------------------------------------------------
#This is the script that will call both PasteBin and
#PokeAPI to add a list of a certain Pokemon's abilities
#to pastebin by fishing the info from PokeAPI
#---------------------------------------------------
from pastebin_api import post_new_paste       #To create a new paste with the abilities for a Pokemon, we need the function to add a new paste  (pastebin_api.py)
from poke_api import get_pokemon           #To get the Pokemon ability info, we need the get_pokemon function from poke_api.py
import sys                              #We only need sys for cases where we run into an error and it exits

def main():

    search_term = get_search_term()                #We must get the argument given at the command line and return it so we can use it later
    search_pokemon = get_pokemon(search_term)                #Use the returned Pokemon name to search for abilities
    if search_pokemon:                                                     #If it is a valid Pokemon
        title, body_text = get_paste_data(search_pokemon, search_term)      #Add the Pokemon and the abilities to the new paste as the title and body text
        paste_url = post_new_paste(title, body_text, '1M')           #And post it to Pastebin (By default it expires after 1 minute)
        print(f'URL of new paste: {paste_url}')                 #And display the newly made paste
    return


def get_search_term():
    num_params = len(sys.argv) -1                           #Get the number of parameters entered at the command line
    if num_params > 0:                                     #If arguments are greater than 1 (at least one argument was entered)
        return sys.argv[1]                                  #Return the first argument given so we can search for it
    else:
        print('Error: Missing search term.')                 #Else if the pokemon does not exist, throw an error and cease operation
        sys.exit(1)



def get_paste_data(search_pokemon, search_term):                 #This function nabs the paste data
    search_term.title()                                         #First we must capitalize the pokemon's name
    title = (f'{search_term.title()}\'s Abilities')                 #This will be the title of the new paste
    divider =  '\n- '.join                                  #With the .join statement, we add a newline followed by a hyphen at the beginning
    body_text = '- ' + divider(search_pokemon)                    #The body text will be each ability with the divider in effect
    return title, body_text                                 #And return this to main so it can be posted


if __name__ == '__main__':
    main()