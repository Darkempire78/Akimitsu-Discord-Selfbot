import os
import discord 
from random import randint
import asyncio
import json
from discord.ext import commands
from discord import File, Message
from discord.ext import tasks

config = json.load(open('config.json', 'r'))
prefix = config["prefix"]

class rpgCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #  Start tasks
        self.job.start()
        self.regen.start()
        # Config
        config = json.load(open('config.json', 'r')) 
        self.pokemonPrefix = config["pokemon_prefix"]
        self.channelId = config["command_channel"]

    @tasks.loop(minutes=5, seconds=10)
    async def job(self):
        channel = self.bot.get_channel(self.channelId)
        jobList = ["paysan", "pecheur", "chasseur", "bucheron", "mineur"]
        for i in jobList:
            await asyncio.sleep(randint(5,10))
            await channel.send(f"{self.pokemonPrefix}job {i}")

    @tasks.loop(hours=12, minutes=5)
    async def regen(self):
        channel = self.bot.get_channel(self.channelId)
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}regen")

    @job.before_loop
    async def before_job(self):
        await self.bot.wait_until_ready()
    
    @regen.before_loop
    async def before_regen(self):
        await self.bot.wait_until_ready()
    

def setup(bot: commands.Bot):
    bot.add_cog(rpgCog(bot))