import discord
from discord.ext import tasks
from itertools import cycle
import time
import json
import os

token = "your bot token"
client = discord.Client()
status = cycle(['!하이픽셀', 'with Python', 'with Apple6050', 'with PyCharm', 'with Google Cloud', 'with Hypixel'])


@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_connect():
    print("Connected")


@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    change_status.start()
    print(f"[Hypixel Bot] [{time.time()}]")


@client.event
async def on_message(message):
    msg = message.content.split(" ")
    if message.content.startswith("!하이픽셀"):
        os.system("py refresh.py")
        with open("result.json") as a:
            json_data = json.load(a)
            hrr = json_data['session']
            hrrr = hrr['online']

        if hrrr == False:
            await message.channel.send("Apple6050님은 온라인이 아닙니다.")
        else:
            hrrrr = hrr['gameType']
            hrrrrr = hrr['mode']
        embed = discord.Embed(description=f"Apple6050님의 하이픽셀 상태 (True = 온라인)")
        embed.set_author(name=f"Hypixel")
        embed.add_field(name=f"온라인 상태", value=f"{hrrr}", inline=False)
        embed.add_field(name=f"게임", value=f"{hrrrr}", inline=False)
        embed.add_field(name=f"상태", value=f"{hrrrrr}", inline=False)
        await message.author.send(embed=embed)

    if (msg[0] == "!청소" and message.author.guild_permissions.manage_messages):
        try:
            await message.channel.purge(limit=int(msg[1]))
        except:
            await message.channel.send("Invalid command \:(")

    if message.content.startswith("!도움말"):
        embed = discord.Embed(description=f"!청소 (갯수), !하이픽셀")
        embed.set_author(name=f"도움말")
        await message.channel.send(embed=embed)


client.run(token)
