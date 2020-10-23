import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.startswith("!p"):
        parrot(message)
        return


def parrot(message):
    command = message.split(" ")
    if command[0].isdigit:
        iterations = command[0]
        for i in range(1, (len(command)) - 1):
            separator = ', '
            separator.join(command)


client.run(TOKEN)
