import os
import discord

import requests
import json
import random

client = discord.Client()
my_secret = os.environ['TOKEN']


# arrays containing answers
xmasAnswers = ['Happy Chrismis!', 'Its Chrismin!', 'Merry Chrisis!', 'Merry Chrysler!']
coinflip = ['Heads', 'Not Sonic lol (Tails..)']


# gets a quote from zenquotes.io
def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)


# when bot is ready
@client.event   # Register an event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


# bot senses a message & responds
@client.event
async def on_message(message):
  # if message is from bot, return nothing
  if message.author == client.user:
    return

  # user sends "!hello", bot responds w/ "Hello!"
  if message.content.lower().startswith('!hello'):
    await message.channel.send('Hello!')

  # user sends "!ping", bot responds w/ "Pong" + bot latency and a gif
  elif message.content.lower().startswith('!ping'):
    await message.channel.send(f'Pong :ping_pong: (Bot latency: **{round(client.latency * 1000)}ms**)')
    await message.channel.send(file=discord.File('resources/pingpong.gif'))

  # user sends "!help", bot sends commandsfile
  elif message.content.lower().startswith("!help"):
			await message.channel.send(file=discord.File("commands.md"))

  # user sends "!coinflip", bot returns result
  elif message.content.lower().startswith("!coinflip"):
			await message.channel.send(random.choice(coinflip))

  # user sends "!github", bot responds w/ my GitHub profile
  elif message.content.lower().startswith("!github"):
			await message.channel.send('https://github.com/SindreKjelsrud')

  # someone writes "merry christmas", bot responds w/ legendary vine quote
  elif "merry christmas" in message.content.lower():
    await message.channel.send(random.choice(xmasAnswers) + ':santa:')

  # user sends "!inspire", bot inspires user
  elif message.content.lower().startswith("!inspire"):
    quote = get_quote()
    await message.channel.send(quote)


# run bot
client.run(my_secret)