# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

#Bot Setup
BOT_PREFIX = ("?", "!")
TOKEN = "NTU0Mzc2NDMxOTA4NTUyNzI0.D2b5RA.h6WxaqKJKVLylaiKj0C7QJdRw0c"

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
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with pathetic carbon-based life forms"))
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
