import os
import discord
import time
import re

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
typerace_start = [False]

@client.event
async def on_ready():
    activity = discord.Game(name=".help", type=3)
    await client.change_presence(activity=activity)
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)


    print(f'{client.user.name} has connected to ' + f'{guild.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif len(message.content) <= 1:
        return
   
    elif message.content[0] == ".":  # command
        try:
            [command, action] = message.content[1:].split(maxsplit=1)
            if command[0] == ".": 
                return
            elif command.lower() == "ping":
                print("ping")
            elif command.lower() == "repeat":
                if "i'm" in action.lower() or "im" in action.lower() or "i am" in action.lower():
                    response = "We know"
                    await message.channel.send(response)
                else: 
                    await message.channel.send(action)
            else:
                await message.channel.send("Invalid command. Commands are:\n`rachit`\n`.repeat`")
        except ValueError as err:
            print("Value Error: " + str(err))
            if message.content == ".help":
                await message.channel.send("Commands are:\n`rachit`\n`.repeat`")
            else:
                await message.channel.send("Invalid command. Commands are:\n`rachit`\n`.repeat`")
    
    elif 'rachit' in message.content.lower():
        response = "Rachit is dum"
        await message.channel.send(response)

    elif message.content == "!typerace start":
        typerace_start[0] = True

    elif typerace_start[0]:
        try:
            text = re.findall("`(.*?)`",message.content)
            response = ""
            for x in text:
                if len(x) > 5:
                    if re.search(r'\S',x) != None:
                        if re.search(r'[,.?\\-]',x) != None:
                            response = x

            print(response)
            if response != "":
                response = re.sub('\s+',' ',response)
                await message.channel.send(response.encode('ascii', 'ignore').decode("utf-8").replace("\00"," "))
                typerace_start[0] = False
            else:
                await message.channel.send("Oh look at me I think making it into multiple messages is gonna stop the bot")
        except:
            print("Unexpected Error")

client.run(TOKEN)