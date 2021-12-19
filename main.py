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
dogTitles = ['Who let the dogs out?', 'woof', 'Whos a good boy!', 'meow', 'Mr. GoodBoy']


## APIs
# gets a quote from zenquotes.io
def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)

# gets a meme from Huge RedditMemesAPI
def get_meme():
  response = requests.get('https://memes.blademaker.tv/api?lang=en')
  res = response.json()
  title = res['title']
  ups = res['ups']
  downs = res['downs']
  sub = res['subreddit']
  meme = discord.Embed(title = f'{title}\nSubreddit: {sub}')
  meme.set_image(url = res['image'])
  meme.set_footer(text=f"👍:{ups}")
  return meme

# gets a dog from Dog API
def get_dog():
  response = requests.get('https://dog.ceo/api/breeds/image/random')
  res = response.json()
  dog = discord.Embed(title = random.choice(dogTitles))
  dog.set_image(url = res['message'])
  return dog

## BOT READY
@client.event   # Register an event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  activity = discord.Game(name = "!help")  # sets bot activity
  await client.change_presence(status = discord.Status.online, activity = activity)


## MESSAGE RESPONSES
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

  # user sends "!plsmeme", bot sends meme from random subreddit
  elif message.content.lower().startswith("!plsmeme"):
    meme = get_meme()
    await message.channel.send(embed = meme)

  # user sends "!plsdog", bot sends picture of dog from Dog API
  elif message.content.lower().startswith("!plsdog"):
    dog = get_dog()
    await message.channel.send(embed = dog)


# run bot
client.run(my_secret)