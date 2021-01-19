import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Testing 123")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startwith('$hello'):
        await message.channel.send('Thrussy!')

client.run(os.getenv('TOKEN'))