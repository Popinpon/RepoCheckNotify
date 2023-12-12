# Exisiting repository checker

Have you ever wanted to receive notifications when a repository, pre-revealed like in an arXiv paper, transitions from private or commit-less status to being public? This repository's code sends a LINE notification the moment a commit is made, especially for 404 not found or empty repositories.


## Installation

```bash
git clone https://github.com/Popinpon/RepoCheckNotify.git
pip install python-dotenv
# or (conda user) conda install -c conda-forge python-dotenv 
```
you need cron or scheduler like Task scheduler(Win) to run this script periodically.

## Usage
- Get message api token
     This code uses LINE notify api [here](https://notify-bot.line.me)
- Save the token in .env file as followed:
- If you want to use other notification service, you can modify the code in send_notififcation.py

```bash
https://github.com/<username1>/<repo_name1>
https://github.com/<username2>/<repo_name2>
...
```

```bash

check_repo.py <repo_config_file(default repo_list.txt)>

```

The config file as followed:




<!-- ## License

Information about the license for your project. -->
