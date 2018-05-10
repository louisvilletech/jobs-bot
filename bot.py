#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Get reactions API endpoint https://api.slack.com/methods/reactions.get

from slackclient import SlackClient
from poyo import parse_string, PoyoException
import codecs
import os
import json
import glob

path = str(os.path.dirname(os.path.realpath(__file__))) + "/"
with codecs.open(path + 'config.yml', encoding='utf-8') as ymlfile:
    ymlstring = ymlfile.read()

config = parse_string(ymlstring)

sc = SlackClient(config['slack']['oauth_access_token'])

# Get all the available pinned messages in the channel
pins = sc.api_call(
  "pins.list",
  channel=config['slack']['channel']
)

# Add new pinned items. Iterate through all of them so we make
#   sure we get everything available

for item in pins['items']:
  file = path + "messages/" + item['message']['ts'] + ".json"
  with open(file, 'w') as out:
    out.write(json.dumps(item))

# Combine all of our messages into a single convenient file.
# We can't just rely on all the json files we added above
#   since there may be messages that have been archived
#   or are unavailable via the API because of the Slack
#   team's message limits

result = []
json_search = path + "messages/[0-9]*.json"
for f in glob.glob(json_search):
  with open(f, "rb") as infile:
    result.append(json.load(infile))

file = path + "messages/messages.json"
with open(file, "w") as outfile:
  json.dump(result, outfile)
  print(json.dumps(result))