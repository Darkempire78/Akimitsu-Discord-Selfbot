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

class pokemonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #  Start tasks
        self.catch.start()
        self.hourly.start()
        self.daily.start()
        # Config
        config = json.load(open('config.json', 'r')) 
        self.pokemonPrefix = config["pokemon_prefix"]
        self.channelId = config["command_channel"]
        self.release = config["release"]
        self.releaseTypeAll = config["release_type_all"]

    @tasks.loop(minutes=16)
    async def catch(self):
        channel = self.bot.get_channel(self.channelId)
        # Catch (15m)
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}catch")

    @tasks.loop(hours=1, minutes=5)
    async def hourly(self): 
        channel = self.bot.get_channel(self.channelId)
        # Hourly
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}hourly")
        # Chest (1h30)
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}chest")
        # Release all duplicate pokemons
        if self.release == True:
            await asyncio.sleep(randint(5,10))
            await channel.send(f"{self.pokemonPrefix}release {self.releaseTypeAll} all")

    @tasks.loop(hours=24, minutes=5)
    async def daily(self): 
        channel = self.bot.get_channel(self.channelId)
        # Daily
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}daily")
        # Weekly
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}weekly")
        # Monthly
        await asyncio.sleep(randint(5,10))
        await channel.send(f"{self.pokemonPrefix}monthly")

    @catch.before_loop
    async def before_catch(self):
        await self.bot.wait_until_ready()
    
    @hourly.before_loop
    async def before_hourly(self):
        await self.bot.wait_until_ready()
    
    @daily.before_loop
    async def before_daily(self):
        await self.bot.wait_until_ready()

def setup(bot: commands.Bot):
    bot.add_cog(pokemonCog(bot))