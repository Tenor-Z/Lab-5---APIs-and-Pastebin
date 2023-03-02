import requests             #We need requests to make... well.. requests to the pastebin api


post_url = "https://pastebin.com/api/api_post.php"             #Here is the PHP website that is responsible for posting generated posts
dev_key = "70185b642e40e7c757c6e47cdf9b1df4"

def main():
    post_new_paste('Some text to paste or something','Lol')     #If no data is entered, it will default to this placeholder text

def post_new_paste(title, body_text, expiration = '10M', islisted = True):
    """Creates a new PasteBin file

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long the paste will last. Default is set to '10M'.
        islisted (bool, optional): Whether the paste is listed or not (default is True)

    Returns:
        str: URL of the paste if successful. Nothing if failed
    """
    parameters = {'api_dev_key': dev_key,
                  'api_option': 'paste',
                  'api_paste_code': body_text,
                  'api_paste_name': title,
                  'api_paste_expire_date': expiration,
                  'api_paste_private': 0 if islisted else 1
    }

    print("Posting new paste to PasteBin...", end='')
    resp_msg = requests.post(post_url, data=parameters)

    if resp_msg.ok:
        print('Success!!')
        #print(f'URL of new paste: {resp_msg.text}')
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