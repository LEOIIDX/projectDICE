'''
main.py

project DICE
'''
import os
import discord
import random
import re
import asyncio
import string
import math
import json

from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Project DICE\n')

bot = commands.Bot(command_prefix='di!',intents=intents)
bot.remove_command('help')

def roll():
	dice = random.randint(0,5)
	return dice
'''
exampleOne

Represents a comparison between two rolls.
Made more as a test of how I want the dice to be rolled
-leo
'''
def exampleOne():
	nameOne = 'Base'
	attackOne = [1, 2, 3, 4, 5, 6]
	defendOne = [0, 0, 1, 1, 2, 2]
	rollOne = attackOne[roll()]

	nameTwo = 'Straddle'
	attackTwo = [0, 1, 2, 5, 6, 7]
	defendTwo = [0, 0, 0, 3, 3, 3]
	rollTwo = defendOne[roll()]

	results = nameOne + ': ' + str(rollOne) + ' vs. ' + nameTwo +': '+ str(rollTwo)
	return results

@bot.event
async def on_ready():
	print('Bot is Ready!')

'''
COMMAND example

All current and future examples are called here
I do not plan to keep these examples and this command when DICE goes live
-leo
'''
@bot.command()
async def example(ctx, tag=None):
	match tag:
		case '1':
			await ctx.channel.send(exampleOne())
			return
		case _:
			await ctx.channel.send('invalid example')

bot.run(TOKEN)