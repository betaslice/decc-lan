# Work with Python 3.6
import discord

TOKEN = 'NTU0Mzc2NDMxOTA4NTUyNzI0.D2bvoQ.YMA9T4jolR_h3kYvzhc3n_gWjYw'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)