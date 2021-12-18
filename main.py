import os
import discord

import random

client = discord.Client()
my_secret = os.environ['TOKEN']

xmasAnswers = ['Happy Chrismis!', 'Its Chrismin!', 'Merry Chrisis!', 'Merry Chrysler!']
coinflip = ['Heads', 'Not Sonic lol (Tails..)']

# when bot is ready
@client.event   # Register an event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# bot sense a message & responds
@client.event
async def on_message(message):
  # if message is from bot, return nothing
  if message.author == client.user:
    return

  # user sends "!hello", bot responds w/ "Hello!"
  if message.content.lower().startswith('!hello'):
    await message.channel.send('Hello!')

  # user sends "!ping", bot responds w/ "Pong" + bot latency
  elif message.content.lower().startswith('!ping'):
    await message.channel.send(f'Pong :ping_pong: (Bot latency: **{round(client.latency * 1000)}ms**)')

  # user sends "!help", bot sends commands file
  elif message.content.lower().startswith("!help"):
			await message.channel.send(file=discord.File("commands.md"))

  # user sends "!coinflip", bot sends commands file
  elif message.content.lower().startswith("!coinflip"):
			await message.channel.send(random.choice(coinflip))

  # user sends "!github", bot sends commands file
  elif message.content.lower().startswith("!github"):
			await message.channel.send('https://github.com/SindreKjelsrud')

  # someone writes "merry christmas", bot responds w/ legendary vine quote
  elif "merry christmas" in message.content.lower():
    await message.channel.send(random.choice(xmasAnswers) + ':santa:')


# run bot
client.run(my_secret)