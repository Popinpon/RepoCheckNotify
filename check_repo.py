import requests
import time
import argparse
from urllib.parse import urlparse
import time

from send_notification import notify_changing


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
            notify_changing(existing_url)
            print(existing_url)
            # send notification
            # break

        time.sleep(1)  # Check every hour

if __name__ == "__main__":
    main()