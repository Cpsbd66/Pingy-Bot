import os
from discord import Intents, Client, utils, Status
from keep_alive import keep_alive

Token = os.getenv("TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


@client.event
async def on_ready():
  await client.change_presence(status=Status.do_not_disturb)
  print(f'Logged in as {client.user.name}')

# The Code is of course correct but just commenting it, because we dont need it now
"""
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if str(message.guild.id) == os.getenv("SERVER") and str(
      message.channel.id) == os.getenv("CHANNEL"):
    user = utils.get(message.guild.roles, id=1119260509347262475) # competitive programmer
    await message.channel.send(f"{user.mention}", delete_after=0)
"""

keep_alive()
client.run(Token)
