'''
kanadeBotQOTD.py
By: Nanahira Monke Kanade Dev

Condensed version of Kanade Bot programmed for the purpose of QOTD.

Meant to be executed via crontab
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

@bot.event
async def on_ready():
	exit()

bot.run(TOKEN)