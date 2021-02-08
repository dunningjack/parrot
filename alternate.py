import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.pornhub.com/video/search?search=' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/view_video.php\\?viewkey=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('http://www.pornhub.com/video/search?search=' + search_results[0])

client.run(TOKEN)
