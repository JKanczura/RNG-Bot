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

        finNum = random.randint(1,s)

        if (finNum == 1):
            await message.channel.send(f'{message.author.name} has death rolled a 1.')
        else:
            await message.channel.send(finNum)

client.run(os.getenv('TOKEN'))
