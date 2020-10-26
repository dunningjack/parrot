import os
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.CLient(TOKEN)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.content.startswith("!p"):
        command = [] = message.split(" ")
        iterations = command[1]
        length = len(command) - 1
        returnedmessage = []
        for i in range(2, length)
            returnedmessage.append(command[i])
        botresponse = returnedmessage.join(" ")

        for j in range(1, iterations):
            client.send_message(botresponse)

client.run(TOKEN)
