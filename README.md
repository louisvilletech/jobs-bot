# Louisville Tech Jobs Bot

This script pulls all pinned messages in a Slack channel and saves them to a database.

# Installation

Requirements

* Python 3.6+

It is recomended that you use pyenv and pipenv to develop your project. Assuming pipenv is installed, simply clone this repo and run `pipenv install` in the project root.

Copy config-template.yml to config.yml and add your Slack app oauth token and the ID for the channel you want to pull messages from.

# Notes

This script is intended to be run as a cron job, but can be run manually. It will save each individual message as it's own json file in the `messages/TS_ID.json` directory along with a combined json file, `messages/messages.json`. Additionally, the script will print the contents of `messages/messages.json` to stdout so you can pipe it wherever you like without modifying the script.