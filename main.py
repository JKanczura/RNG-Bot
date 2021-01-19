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
        splitRet = message.content.split(' ', 0)
        s = int(splitRet[1], 10)
        random.seed(s)

        await message.channel.send(random.Random())

client.run(os.getenv('TOKEN'))
