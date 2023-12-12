import requests
import time
import argparse
from urllib.parse import urlparse
import time
import os

from dotenv import load_dotenv


def init_args():
    parser = argparse.ArgumentParser(description="Check repository status")
    parser.add_argument("--repo_list", type=str, default="repo_list.txt")
    return parser.parse_args()

def check_repository_status(repo_url):

    # Extract the username and repo name
    url_parse = urlparse(repo_url)
    if url_parse.hostname == "github.com":
        url = url_parse.path
        username = url.split("/")[1]
        repo_name = url.split("/")[2]
        print("User:","Repo Name")
        print(username,repo_name)
        
        response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/branches")
        response = response.json()  

        
        if type(response)==dict and ("message" in response.keys()) and (response["message"] == "Not Found"):
            print("404 Not Found")
            return None
        elif len(response)==0 :
            print("Empty repository")
            return None
        
        elif len(response) >0:
            print("Repository was commited")
            return repo_url
        else:
            raise Exception("Unknown response: {}".format(response))
    else: 
        raise Exception("Invalid repository url: {}".format(repo_url))


def send_line_notify(notification_message):
    """
    notifies a message by line 
    """


    load_dotenv(verbose=True)

    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    line_token = os.environ.get("TOKEN")
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def main():
    # read url config
    args = init_args()
    with open(args.repo_list, "r") as f:
        url_list = f.readlines()
   
    for url in url_list :
        if url[0] == "#":
            continue
        existing_url = check_repository_status(url)
        if existing_url is not None :
            send_line_notify(existing_url)
            print(existing_url)
            # send notification
            # break

        time.sleep(1)  # Check every hour

if __name__ == "__main__":
    main()