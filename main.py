import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Testing 123")
    random.seed(1)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$roll'):
        splitRet = message.content.split()
        print(splitRet)
        s = int(splitRet[1], 10)

        finNum = random.randint(0,s)

        await message.channel.send(finNum)

client.run(os.getenv('TOKEN'))
