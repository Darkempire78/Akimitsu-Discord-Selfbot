import os
import sys
import asyncio
import discord
import random
import json

from discord import File, Message
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks

config = json.load(open('config.json', 'r'))
prefix = config["prefix"]
token = config["token"]

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

# bot events
@bot.event
async def on_connect():
    print (f'Akimitsu SelfBot \nLogged in as: {bot.user}\nCurrent Prefix: {prefix}')

#Bot Events
# @bot.event
# async def on_message(message):
#     pass

# Load Cogs
try:
    if config["pokemonMode"] == True:
        bot.load_extension("cogs.pokemon")
    if config["rpgMode"] == True:
        bot.load_extension("cogs.rpg")
    bot.load_extension("cogs.help")
except:
    print("A Cog failed to load :/")
    pass

bot.run(token, bot=False)