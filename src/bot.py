import os
import json
from discord.ext.commands import Bot

BOT_PREFIX = ("!")

# Load auth token
with open(os.path.join('data', 'auth.json')) as auth_file:
    TOKEN = json.load(auth_file)['token']

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def source():
    await client.say('This bot is supposed to be open source! I should post the code somewhere and put a link in here!')

@client.command(name='Doug',
                aliases=['doug'])
async def doug_command(context):
    my_message = "hello world!"

    await context.send(my_message)

client.run(TOKEN)
