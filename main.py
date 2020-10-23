import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!p')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.command()
async def on_message(message):
    if '!p' in message.content:
        parrot(message)
    return


@client.event
async def parrot(message):
    command = message.split(" ")
    if command[1].isdigit:
        iterations = command[1]
        for i in range(1, (len(command))):
            separator = ', '
            statement = separator.join(command)

        for j in range(1, iterations):
            await client.say(statement)

    await client.process_commands(message)


client.run(TOKEN)
