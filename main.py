import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Testing 123")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$roll'):
        splitRet = message.content.split()
        print(splitRet)
        s = int(splitRet[1], 10)
        random.seed(s)
        finNum = str(random.Random())

        await message.channel.send(finNum)

client.run(os.getenv('TOKEN'))
