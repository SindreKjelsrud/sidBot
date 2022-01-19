import os
import discord
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()
my_secret = os.environ['TOKEN']


# arrays containing answers
xmasAnswers = ['Happy Chrismis!', 'Its Chrismin!', 'Merry Chrisis!', 'Merry Chrysler!']
coinflip = ['Heads', 'Not Sonic lol (Tails..)']
dogTitles = ['Who let the dogs out?:dog:', 'woof:dog:', 'Whos a good boy!:dog:', 'meow:cat:', 'Mr. GoodBoy:dog:', 'Bork Bork!:dog:']


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

  # user sends "!invbot", bot responds w/ invite link for bot
  elif message.content.lower().startswith("!invbot"):
    embedVar = discord.Embed(color=0x7B64FF)
      
    embedVar.add_field(name="Bot Invite Link", value="https://discord.com/oauth2/authorize?client_id=921786935662477412&permissions=274881309760&scope=bot", inline=False)

    await message.channel.send(embed=embedVar)

  # user sends "!help", bot sends commandsfile
  elif message.content.lower().startswith("!help"):
    embedVar = discord.Embed(title="List of sidBots features/commands:", description="--------------------------------", color=0x7B64FF)
      
    embedVar.add_field(name="!help", value="List of commands", inline=False)

    embedVar.add_field(name="!hello", value="Bot responds with 'Hello!'", inline=False)

    embedVar.add_field(name="!ping", value="Bot responds with 'Pong!' and botlatency + a gif from Ping Pong The Animation", inline=False)

    embedVar.add_field(name="!github", value="Flexes github link", inline=False)

    embedVar.add_field(name="!coinflip", value="Heads or Tails!", inline=False)

    embedVar.add_field(name="merry christmas", value="Someone writes 'merry christmas' and bot responds w/ legendary vine quote selected from an array", inline=False)

    embedVar.add_field(name="!inspire", value="Bot inspires user with a quote from zenquotes.io", inline=False)

    embedVar.add_field(name="!plsmeme", value="Bot supplies with premium memes from subreddits across Reddit from Huge RedditMemesAPI", inline=False)

    embedVar.add_field(name="!plsdog", value="Bot supplies with pictures of cute doggos across the whole internet through Dog API", inline=False)

    embedVar.add_field(name="!invbot", value="Bot sends invite link for itself", inline=False)

    await message.channel.send(embed=embedVar)

# keeps bot alive
keep_alive()

# run bot
client.run(my_secret)




###############################

#from requests import Request, Session
#from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

###############################

# crypto API
# def get_crypto():
#   url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#   parameters = {
#     'start':'1',
#     'limit':'5000',
#     'convert':'USD'
#   }
#   headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': '5c96c638-c66f-4ddb-9c5d-7a77d5d83258',
#   }

#   session = Session()
#   session.headers.update(headers)

#   try:
#     response = session.get(url, params=parameters)
  
  
#   #res = response.json()
#   #name = res['name']
#   #id = res['id']
#   #tags = res['tags']
#   #crypto = discord.Embed(title = f'{id}\nMiniable: {tags}')

#     json_data = json.loads(response.text)
#     return(json_data)
#   except (ConnectionError, Timeout, TooManyRedirects) as e:
#     return(e)

################################

  # crypto - *not working*
#  elif message.content.lower().startswith("!crypto"):
#    crypto = get_crypto()
#    await message.channel.send(crypto)
