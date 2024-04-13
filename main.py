import os
from discord import Intents, Client, utils

Token = os.getenv("TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


@client.event
async def on_ready():
  print(f'Logged in as {client.user.name}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if str(message.guild.id) == os.getenv("SERVER") and str(
      message.channel.id) == os.getenv("CHANNEL"):
    user = utils.get(message.guild.roles, id= 1119260509347262475)
    await message.channel.send(f"{user.mention}")


client.run(Token)
