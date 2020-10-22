from discord.ext import commands
import json
import os

config = json.load(open('config.json', 'r'))
prefix = config["prefix"]

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.send(f"**General Commands:**\n\nsoon...")

def setup(bot: commands.Bot):
    bot.add_cog(help_cog(bot))
