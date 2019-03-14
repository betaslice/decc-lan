# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import os

#Bot Setup
BOT_PREFIX = ("?", "!")
TOKEN = os.environ['TOKEN']

client = Bot(command_prefix=BOT_PREFIX)

#Commands
@client.command(name='8ball',
                description="Answers your pathetic questions.",
                brief="Answers a question.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Absolutely not.',
        'My answer is NO.',
        'Why should I know?',
        'Possibly.',
        'The answer finna be yes.',
    ]
    await client.say(random.choice(possible_responses))

@client.command(name='rickroll',
                description="Links to the music video for Never Gonna Give You Up.",
                brief="Rickrolls chat.",
                aliases=['rickastley', 'rick'],
                pass_context=True)
async def rick_roll(context):
    await client.say("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@client.command(name='protegent',
                description="Links to the Protegent Antivirus Rap",
                brief="Protegent Antivirus Rap",
                aliases=['proto','rap','antivirus'],
                pass_context=True)
async def proto_rap(context):
    await client.say("https://www.youtube.com/watch?v=PIp06sdFHLM")


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.command(name="countryroads",
                description="take me home",
                brief="take me home",
                aliases=[],
                pass_context=True)
async def country_roads(context):
                await client.say('https://www.youtube.com/watch?v=IObnt8UFjVA')

@client.command(name="vaporwave",
                description"",
                brief="",
                aliases=[],
                pass_context=True)
async def vapor_wave(context):
    await client.say('https://www.youtube.com/watch?v=jjiq8VogmIk')
                

#Game Name
gamelist = ["3D Space Pinball", "Minesweeper", "Windows 98", "with pathetic life forms"]

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if 'r/' in message.content:
        newmessage = message.content.split()
        for word in newmessage:
                if 'r/' in word:
                    msg = ('https://reddit.com/' + word).format(message)
                    await client.send_message(message.channel, msg)
                    
async def on_ready():
    await client.change_presence(game=Game(name=random.choice(gamelist)))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

#Bot Execution
client.loop.create_task(list_servers())
client.run(TOKEN)
