# RepoVTA - Repo Visibility Transition 
Repo VTA is a python script that sends notification when a github repository visibility becomes public.

Have you ever wanted to receive notifications when a repository, pre-revealed like in an arXiv paper, transitions from private or commit-less status to being public? This repository's code sends notification using a notification api like LINE notification the moment a commit is made, especially for 404 not found or empty repositories.

![](404img.png)



## Installation

```bash
git clone https://github.com/Popinpon/RepoCheckNotify.git
pip install python-dotenv
# or (conda user) conda install -c conda-forge python-dotenv 
```


## Preparation
- Get message api token
     This code uses LINE notify api [here](https://notify-bot.line.me)
- Save the token in .env file as followed:

    ```bash
    # .env
    TOKEN=<your token>
    ```
- Save repository urls in repo_list.txt file as followed:
    ```bash
    #repo_list.txt
    https://github.com/<username1>/<repo_name1>
    https://github.com/<username2>/<repo_name2>
    ...
    ```

- If you want to use other notification service like Discord, you can modify [send_message function](https://github.com/Popinpon/RepoCheckNotify/blob/main/send_notification.py?plain=1#L26) in send_notififcation.py

## Usage
```bash

python check_repo.py <repository list file (default repo_list.txt)>
# if you want to execute theis script periodically, use cron or Task scheduler
```
Careful: github api has rate limit.





<!-- ## License

Information about the license for your project. -->
