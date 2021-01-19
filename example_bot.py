import discord
import os
import requests # allows for HTTP request to get data from the API, zenquotes API
import json # API returns JSON, this module makes it easier to work with the returned JSON
from dotenv import load_dotenv, find_dotenv
from pathlib import Path 

load_dotenv(find_dotenv())
env_path = Path('.')/'.env'
load_dotenv(dotenv_path = env_path)

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
    "Cheer up!",
    "Hang in there!",
    "You are a great person / bot!"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random") # could also use any other quotes API
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(startswith))

client.run(os.getenv('TOKEN'))